from sentence_transformers import SentenceTransformer, util

from hack_uchi_ru_p2p.settings import MIN_COS_SIM


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def clear(cls):
        cls._instances = {}


class AIModel(metaclass=MetaSingleton):

    def __init__(self):
        self.model = None
        self.questions = None
        self.questions_dict = None
        self.embeddings = None

    def prepare_model(self, questions):
        self.model = SentenceTransformer('distiluse-base-multilingual-cased-v1', cache_folder='models/')
        self.questions = questions
        self.questions_dict = {q.text: q for q in self.questions}
        self.embeddings = self.model.encode([q.text for q in self.questions])

    def get_close_questions(self, question_text):
        question_text_vector = self.model.encode([question_text])[0]
        cos_sim = util.cos_sim(self.embeddings, question_text_vector)

        all_sentences = []
        # for i in range(len(cos_sim) - 1):
        #     all_sentences.append({
        #         'sentence': self.questions[i].text,
        #         'cos_sim': cos_sim[i]
        #     })
        for i in range(len(cos_sim) - 1):
            if cos_sim[i] >= MIN_COS_SIM:
                all_sentences.append({
                    'sentence': self.questions[i].text,
                    'cos_sim': cos_sim[i]
                })
        sorted_all_sentences = sorted(all_sentences, key=lambda x: x['cos_sim'], reverse=True)

        all_questions = []
        for index, sent in enumerate(sorted_all_sentences):
            if index > 2:
                break
            all_questions.append(self.questions_dict[sent['sentence']])

        return all_questions

from achievements.db_models.achievement_db_model import Achievement
from core.db_models.question_db_model import Question
from core.tools.message_sender import user_send_to_ws


def check_count_question(user, count):
    return Question.objects.filter(author=user).count() == count


MAP_TYPE = {
    1: check_count_question,
    10: check_count_question,
    50: check_count_question,
    100: check_count_question,
}


def check_ach_user(user, map_type):
    if MAP_TYPE[map_type](user, map_type):
        achievement = Achievement.objects.get(map_type=map_type)
        if not achievement in user.achievement.all():
            user.achievement.add(achievement)
            user.y_coin += achievement.y_coin
            user.faculty_count += achievement.f_coin
            user.save()
            user.faculty.score += achievement.f_coin
            user.faculty.save()
            user_send_to_ws(user, {'new_achievement': str(achievement.id)})

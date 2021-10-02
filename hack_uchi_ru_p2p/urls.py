from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.api_views.auth_api_view import UserAuthAPIView
from accounts.api_views.avatar_api_view import UserAvatarAPIView
from accounts.api_views.register_api_view import RegisterAPIView
from accounts.api_views.user_api_view import UserListView, UserDetailView
from achievements.api_views.achievement_api_view import AchievementRetrieveView, AchievementListView
from chat.api_views.chat_api_view import ChatAPIView
from chat.api_views.message_api_view import MessageChatListCreateView
from core.api_views.answer_api_view import AnswerListView, AnswerDetailAPIView
from core.api_views.faculty_api_view import FacultyListView, FacultyRetrieveView
from core.api_views.like_api_view import LikeAPIView
from core.api_views.question_api_view import QuestionListView, QuestionDetailAPIView, BestQuestionsAPIView
from core.api_views.subject_api_view import SubjectListView
from core.api_views.topic_api_view import TopicListView, BestTopicAPIView
from hack_uchi_ru_p2p import settings
from shop.api_views.purchases_api_view import PurchasesListView
from shop.api_views.shop_item_api_view import ShopItemListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('user/register/', RegisterAPIView.as_view()),
    path('user/auth/', UserAuthAPIView.as_view()),
    path('user/load_avatar/', UserAvatarAPIView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/', UserListView.as_view()),

    # faculty
    path('faculty/<int:pk>/', FacultyRetrieveView.as_view()),
    path('faculty/', FacultyListView.as_view()),

    # subject
    path('subject/', SubjectListView.as_view()),

    # topic
    path('topic/', TopicListView.as_view()),
    path('best_topic/', BestTopicAPIView.as_view()),

    # question
    path('question/<int:pk>/', QuestionDetailAPIView.as_view()),
    path('question/', QuestionListView.as_view()),
    path('best_question/', BestQuestionsAPIView.as_view()),

    # answer
    path('answer/<int:pk>/', AnswerDetailAPIView.as_view()),
    path('answer/', AnswerListView.as_view()),

    # like
    path('like/', LikeAPIView.as_view()),

    # chat
    path('chat/', ChatAPIView.as_view()),
    path('message/', MessageChatListCreateView.as_view()),

    # shop
    path('shop_items/', ShopItemListView.as_view()),
    path('purchases/', PurchasesListView.as_view()),

    # achievement
    path('achievement/<int:pk>/', AchievementRetrieveView.as_view()),
    path('achievement/', AchievementListView.as_view()),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

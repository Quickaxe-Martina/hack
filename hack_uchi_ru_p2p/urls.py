from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.api_views.auth_api_view import UserAuthAPIView
from accounts.api_views.avatar_api_view import UserAvatarAPIView
from accounts.api_views.register_api_view import RegisterAPIView
from accounts.api_views.user_api_view import UserListView, UserDetailView, UserAchievementAPIView
from accounts.api_views.users_dashboard_api_view import UserDashboardAPIView
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
    path('api/user/register/', RegisterAPIView.as_view()),
    path('api/user/auth/', UserAuthAPIView.as_view()),
    path('api/user/load_avatar/', UserAvatarAPIView.as_view()),
    path('api/user/<int:pk>/', UserDetailView.as_view()),
    path('api/user/', UserListView.as_view()),
    path('api/user_dashboard/', UserDashboardAPIView.as_view()),
    path('api/user_achievement/', UserAchievementAPIView.as_view()),

    # faculty
    path('api/faculty/<int:pk>/', FacultyRetrieveView.as_view()),
    path('api/faculty/', FacultyListView.as_view()),

    # subject
    path('api/subject/', SubjectListView.as_view()),

    # topic
    path('api/topic/', TopicListView.as_view()),
    path('api/best_topic/', BestTopicAPIView.as_view()),

    # question
    path('api/question/<int:pk>/', QuestionDetailAPIView.as_view()),
    path('api/question/', QuestionListView.as_view()),
    path('api/best_question/', BestQuestionsAPIView.as_view()),

    # answer
    path('api/answer/<int:pk>/', AnswerDetailAPIView.as_view()),
    path('api/answer/', AnswerListView.as_view()),

    # like
    path('api/like/', LikeAPIView.as_view()),

    # chat
    path('api/chat/', ChatAPIView.as_view()),
    path('api/message/', MessageChatListCreateView.as_view()),

    # shop
    path('api/shop_items/', ShopItemListView.as_view()),
    path('api/purchases/', PurchasesListView.as_view()),

    # achievement
    path('api/achievement/<int:pk>/', AchievementRetrieveView.as_view()),
    path('api/achievement/', AchievementListView.as_view()),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

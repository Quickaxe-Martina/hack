from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.api_views.auth_api_view import UserAuthAPIView
from accounts.api_views.avatar_api_view import UserAvatarAPIView
from accounts.api_views.register_api_view import RegisterAPIView
from accounts.api_views.user_api_view import UserListView, UserDetailView
from core.api_views.answer_api_view import AnswerListView, AnswerDetailAPIView
from core.api_views.faculty_api_view import FacultyListView
from core.api_views.like_api_view import LikeAPIView
from core.api_views.question_api_view import QuestionListView, QuestionDetailAPIView
from core.api_views.subject_api_view import SubjectListView
from core.api_views.topic_api_view import TopicListView
from hack_uchi_ru_p2p import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('user/register/', RegisterAPIView.as_view()),
    path('user/auth/', UserAuthAPIView.as_view()),
    path('user/load_avatar/', UserAvatarAPIView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/', UserListView.as_view()),

    # faculty
    path('faculty/', FacultyListView.as_view()),

    # subject
    path('subject/', SubjectListView.as_view()),

    # topic
    path('topic/', TopicListView.as_view()),

    # question
    path('question/<int:pk>/', QuestionDetailAPIView.as_view()),
    path('question/', QuestionListView.as_view()),

    # answer
    path('answer/<int:pk>/', AnswerDetailAPIView.as_view()),
    path('answer/', AnswerListView.as_view()),

    # like
    path('like/', LikeAPIView.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

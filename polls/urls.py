from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, VoteCreateView, ActivePollsView

router = DefaultRouter()
router.register(r'polls', PollViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('votes/', VoteCreateView.as_view(), name='vote-create'),
    path('active-polls/', ActivePollsView.as_view(), name='active-polls'),
]
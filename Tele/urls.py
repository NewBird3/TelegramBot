
from django.conf.urls import url
from .views import TelegramBotView


urlpatterns = [
     url(r'c817304a3d163ebd58b44dd446eba29572300724098cdbca1a/?$', TelegramBotView.as_view()),
]

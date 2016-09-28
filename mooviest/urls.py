"""mooviest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from api.viewsets import LangViewSet, CountryViewSet, CelebrityViewSet, Celebrity_langViewSet, RoleViewSet, Role_langViewSet, SagaViewSet, Saga_langViewSet, GenreViewSet, Genre_langViewSet, EmotionViewSet, Emotion_langViewSet, StreamingViewSet, SourceViewSet, MovieViewSet, Movie_langViewSet, RatingViewSet, CatalogueViewSet, Catalogue_langViewSet, ParticipationViewSet
from api.viewsets_users import UserViewSet
from rest_framework.routers import DefaultRouter
from api.viewsets_custom import CelebrityCustomViewSet, MovieByReleasedViewSet, MoviesAppByLangViewSet

from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'lang', LangViewSet)
router.register(r'country', CountryViewSet)
router.register(r'celebrity', CelebrityViewSet)
router.register(r'celebrity_lang', Celebrity_langViewSet)
router.register(r'role', RoleViewSet)
router.register(r'role_lang', Role_langViewSet)
router.register(r'saga', SagaViewSet)
router.register(r'saga_lang', Saga_langViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'genre_lang', Genre_langViewSet)
router.register(r'emotion', EmotionViewSet)
router.register(r'emotion_lang', Emotion_langViewSet)
router.register(r'streaming', StreamingViewSet)
router.register(r'source', SourceViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'movie_released', MovieByReleasedViewSet)
router.register(r'movie_lang', Movie_langViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'catalogue', CatalogueViewSet)
router.register(r'catalogue_lang', Catalogue_langViewSet)
router.register(r'participation', ParticipationViewSet)
router.register(r'user',UserViewSet)


urlpatterns = [

    # Apps URLs
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name = 'robots.txt', content_type = 'text/plain')),

    # API
    url(r'^api/',include(router.urls)),
    url(r'api_auth/',include('rest_framework.urls', namespace = 'rest_framework')),

    # App calls
    url('^api/movie_app_bylang', MoviesAppByLangViewSet.as_view()),

    # Home URLs
    url(r'^$', 'home.views.index', name = 'home'),

    # Movie URLs
    url(r'^movie/(?P<movie_id>[0-9]+)/$', 'movie.views.index', name = 'movie'),
    url(r'^movie/(?P<movie_id>[0-9]+)/change-collection$', 'movie.views.changeCollection', name = 'movie_changeCollection'),

    # Users URLs
    url(r'^login$', 'users.views.login', name = 'users_login'),
    url(r'^logout$', 'users.views.logout', name = 'users_logout'),
    url(r'^register$','users.views.register', name ='users_register'),
    url(r'^setting$','users.views.settingInfo', name ='users_settings'),
    url(r'^settings/password$','users.views.settingPassword', name = 'users_password'),
    url(r'^profile/(?P<user_id>[0-9]+)$','users.views.profile', name = 'users_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, re_path, include
from django.conf import settings
from django.contrib.auth import views as authViews
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # landing page
    # path('', views.landingPage, name='hello'),
    path('', views.homePage, name='home'),

    # authentication
    path('signup/', views.signUp, name='signUp'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.accDetails, name='accDetails'),
    
    # password reset
    path('password_reset/', authViews.PasswordResetView.as_view(template_name="main/password_reset.html"), name='reset_password'),
    path('password_reset_done/', authViews.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name='password_reset_confirm'),
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name='password_reset_complete'),

    # site navigation
    re_path(r'^search/$', views.searchResults, name='search'),
    path('note/<str:name>/', views.noteDetails, name='noteDetails'),
    path('download/<str:name>/', views.noteDownload, name='noteDownload'), 
    path('noteUpload/', views.noteUpload, name='noteUpload'),
    path('noteUpdate/<str:name>/<str:id>/', views.updateNote, name='updateNote'),
    path('deleteNote/<str:name>/<str:id>/', views.deleteNote, name='deleteNote'),
    path('deleteNoteHistory/<str:name>/', views.deleteNoteHistory, name='deleteNoteHistory'),
    path('modRequest/', views.modRequest, name='modRequest'),
    path('about/', views.about, name='about'),
] + static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)

# media url ( for development only, not to be used in production )
# if settings.DEBUG == True or settings.DEBUG == False: 
#         urlpatterns += static(settings.MEDIA_URL, 
#                               document_root=settings.MEDIA_ROOT)
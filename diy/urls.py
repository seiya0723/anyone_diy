from django.urls import path
from . import views

app_name    = "diy"
urlpatterns = [ 
    path(""                           , views.index               , name="index"            ),
    path("project/"                   , views.project             , name="project"          ),
    path("project_single/<uuid:pk>/"  , views.project_single      , name="project_single"   ),
    path("community/"                 , views.community           , name="community"        ),
    path("community_single/<uuid:pk>/", views.community_single    , name="community_single" ),
    path("mypage/"                    , views.mypage              , name="mypage"           ),
]


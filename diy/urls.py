from django.urls import path
from . import views

app_name    = "diy"
urlpatterns = [ 
    path(""                           , views.index               , name="index"            ),
    path("project/"                   , views.project             , name="project"          ),
    path("project_single/<uuid:pk>/"  , views.project_single      , name="project_single"   ),
    path("project_mod/<uuid:pk>/"     , views.project_mod         , name="project_mod"      ),

    path("favorite/"                  , views.favorite            , name="favorite"         ),

    path("community/"                 , views.community           , name="community"        ),
    path("community_single/<uuid:pk>/", views.community_single    , name="community_single" ),
    path("community_mod/<uuid:pk>/"   , views.community_mod       , name="community_mod"    ),

    path("community_topic/<uuid:pk>/" , views.community_topic     , name="community_topic"  ),

    path("mypage/"                    , views.mypage              , name="mypage"           ),
    path("user/<uuid:pk>"             , views.user                , name="user"             ),

]


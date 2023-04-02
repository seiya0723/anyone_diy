from django import forms

from .models import Category,Project,Material,Feedback,Favorite,FavoriteFolder,Community,CommunityTopic,CommunityMessage,Album


class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = [ "name" ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model   = Project
        fields  = [ "category","title","thumbnail","description","time","level","user","process" ]

class MaterialForm(forms.ModelForm):
    class Meta:
        model   = Material
        fields  = [ "name","amount","project","user" ]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model   = Feedback
        fields  = [ "comment","project","user","star" ]

class FavoriteFolderForm(forms.ModelForm):
    class Meta:
        model   = FavoriteFolder
        fields  = [ "title","user" ]

class FavoriteForm(forms.ModelForm):
    class Meta:
        model   = Favorite
        fields  = [ "project","user","favorite_folder" ]

class CommunityForm(forms.ModelForm):
    class Meta:
        model   = Community
        fields  = [ "name","user","members" ]
    
class CommunityTopicForm(forms.ModelForm):
    class Meta:
        model   = CommunityTopic
        fields  = [ "title","community","user" ]

class CommunityMessageForm(forms.ModelForm):
    class Meta:
        model   = CommunityMessage
        fields  = [ "community_topic","comment","user", ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model   = Album
        fields  = [ "image","user" ]



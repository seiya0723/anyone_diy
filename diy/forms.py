from django import forms

from .models import Category,Project,Material,Feedback,Favorite,FavoriteFolder,Community,CommunityTopic,CommunityMessage
from users.models import CustomUser

from django_summernote.widgets import SummernoteWidget
from django.conf import settings
import bleach

class HTMLField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    def to_python(self, value):
        value       = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES)



class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = [ "name" ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model   = Project
        fields  = [ "category","title","thumbnail","description","time","level","user","process" ]

    process     = HTMLField()
    description = forms.CharField(  widget  = forms.Textarea( attrs={ "maxlength":str(Project.description.field.max_length), } ),
                                    label   = Project.description.field.verbose_name 
                                    )


class MaterialForm(forms.ModelForm):
    class Meta:
        model   = Material
        fields  = [ "name","amount","project","user" ]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model   = Feedback
        fields  = [ "project","comment","user","star" ]

    comment     = forms.CharField(  widget  = forms.Textarea( attrs={ "maxlength":str(Feedback.comment.field.max_length), } ),
                                    label   = Feedback.comment.field.verbose_name 
                                    )



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

    comment = HTMLField()


"""
class AlbumForm(forms.ModelForm):
    class Meta:
        model   = Album
        fields  = [ "image","user" ]
"""

class CustomUserForm(forms.ModelForm):

    class Meta:
        model   = CustomUser
        fields  = ["first_name","last_name","handle_name","introduction","icon",]

    introduction    = HTMLField

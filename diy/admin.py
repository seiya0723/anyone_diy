from django.contrib import admin
from django.utils.html import format_html

from .models import Category,Project,Material,Feedback,Favorite,FavoriteFolder,Community,CommunityTopic,CommunityMessage,Information
from .forms import ProjectForm,CommunityMessageForm,FeedbackForm,InformationForm


class CategoryAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","name" ]




class ProjectAdmin(admin.ModelAdmin):

    form            = ProjectForm
    list_display    = [ "id","dt","category","title","format_thumbnail","description","time","level","user","process" ]

    def format_thumbnail(self,obj):
        if obj.thumbnail:
            return format_html(f'<img src="{obj.thumbnail.url}" alt="画像" style="width:15rem">')

    format_thumbnail.short_description      = Project.thumbnail.field.verbose_name
    format_thumbnail.empty_value_display    = "サムネイル無し"


class MaterialAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","name","amount","project","user" ]

class FeedbackAdmin(admin.ModelAdmin):
    form            = FeedbackForm
    list_display    = [ "id","dt","comment","project","user","star" ]

class FavoriteFolderAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","title","user" ]

class FavoriteAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","project","user","favorite_folder" ]

class CommunityAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","name","user","format_members" ]
    
    def format_members(self,obj):
        content     = ""
        if obj.members:
            for member in obj.members.all():
                content += f"{member.handle_name} "

        return content

    format_members.short_description      = Community.members.field.verbose_name
    format_members.empty_value_display    = "参加者無し"


class CommunityTopicAdmin(admin.ModelAdmin):
    list_display    = [ "id","dt","title","community","user" ]

class CommunityMessageAdmin(admin.ModelAdmin):
    form            = CommunityMessageForm
    list_display    = [ "id","dt","community_topic","comment","user", ]



class InformationAdmin(admin.ModelAdmin):
    form            = InformationForm
    list_display    = ["id","dt","overview","term","site_id"]



admin.site.register(Category            ,CategoryAdmin        )
admin.site.register(Project             ,ProjectAdmin         )
admin.site.register(Material            ,MaterialAdmin        )
admin.site.register(Feedback            ,FeedbackAdmin        )
admin.site.register(FavoriteFolder      ,FavoriteFolderAdmin  )
admin.site.register(Favorite            ,FavoriteAdmin        )
admin.site.register(Community           ,CommunityAdmin       )
admin.site.register(CommunityTopic      ,CommunityTopicAdmin  )
admin.site.register(CommunityMessage    ,CommunityMessageAdmin)
admin.site.register(Information         ,InformationAdmin      )

from django.contrib import admin

from .models import Category,Project,Process,Material,Feedback,Favorite,Community,CommunityMessage



class CategoryAdmin(admin.ModelAdmin):
	pass
class ProjectAdmin(admin.ModelAdmin):
	pass
class ProcessAdmin(admin.ModelAdmin):
	pass
class MaterialAdmin(admin.ModelAdmin):
	pass
class FeedbackAdmin(admin.ModelAdmin):
	pass
class FavoriteAdmin(admin.ModelAdmin):
	pass
class CommunityAdmin(admin.ModelAdmin):
	pass
class CommunityMessageAdmin(admin.ModelAdmin):
	pass


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Process)
admin.site.register(Material)
admin.site.register(Feedback)
admin.site.register(Favorite)
admin.site.register(Community)
admin.site.register(CommunityMessage)



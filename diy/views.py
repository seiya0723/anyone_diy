from django.shortcuts import render, redirect
from django.views import View

# DRF
#from rest_framework.views import APIView as View

# 検索+ページネーション
from django.db.models import Q
from django.core.paginator import Paginator 

# Ajax用
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
#TODO: 後にメール確認取れていない場合はリダイレクトさせるよう、LoginRequiredMixinを書き換える
# https://noauto-nolife.com/post/django-create-origin-mixin/


from .models import Category,Project,Material,Feedback,Favorite,Community,CommunityTopic,CommunityMessage
from .forms import CategoryForm,ProjectForm,MaterialForm,FeedbackForm,FavoriteForm,CommunityForm,CommunityTopicForm, CommunityMessageForm,CustomUserForm

from users.models import CustomUser

#TODO: 1ページに表示させるコンテンツ数
LIST_PER_PAGE   = 10

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        #TODO: コミュニティとプロジェクトの一部をコンテキストへ
        context["projects"]     = Project.objects.order_by("-dt")[:5]
        context["communities"]  = Community.objects.order_by("-dt")[:5]
    
        # トップページで検索をした場合、コミュニティ・プロジェクトの一部を表示？

        return render(request, "diy/index.html", context)

index   = IndexView.as_view()


class ProjectView(View):
    def get(self, request, *args, **kwargs):

        context = {}            
        query   = Q()

        if "search" in request.GET:
            words   = request.GET["search"].replace("　"," ").split(" ")

            for word in words:
                if word == "":
                    continue

                query &= Q( Q(title__contains=word) | Q(description__contains=word) )


        #TODO: ここにプロジェクトの詳細検索を受け付ける(難易度やフィードバックの点数などでも検索できるようにする。)
        projects    = Project.objects.filter(query).order_by("-dt")
        paginator   = Paginator(projects,LIST_PER_PAGE)

        if "project_page" in request.GET:
            context["projects"] = paginator.get_page(request.GET["project_page"])
        else:
            context["projects"] = paginator.get_page(1)

        
        # 投稿する内容
        context["form"]         = ProjectForm()
        context["categories"]   = Category.objects.order_by("-dt")


        return render(request, "diy/project.html", context)

    def post(self, request, *args, **kwargs):
        # ここでプロジェクトの投稿を受け付ける
        # プロジェクトの投稿とプロジェクトに紐づく素材の保存もセットでやる。
        # .getlist()を使う。

        copied          = request.POST.copy()
        copied["user"]  = request.user

        form    = ProjectForm(copied)

        if not form.is_valid():
            messages.error(request, "プロジェクトの投稿に失敗しました")
            return redirect("diy:project")

        project         = form.save()

        # 素材を使用しないプロジェクトの場合はMaterialの追加はせず終了する。
        names   = request.POST.getlist("name")
        amounts = request.POST.getlist("amount")

        for name,amount in zip(names, amounts):
            dic = {}
            dic["name"]     = name
            dic["amount"]   = amount
            dic["project"]  = project
            dic["user"]     = request.user

            form    = MaterialForm(dic)

            if form.is_valid():
                form.save()

        messages.success(request, "プロジェクトの投稿に成功しました")

        return redirect("diy:project")

project = ProjectView.as_view()


# TODO:【審議中】 これ、作るべきか？ ← プロジェクト新規作成フォームはどこに書く？
# ↑ マイページか、プロジェクト一覧ページにCSSのモーダルでも良いのでは？
#　↑　そもそもコミュニティの作成フォームもマイページに表示すれば良いのでは？
class ProjectCreateView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, "diy/project_create.html")

    def post(self, request, *args, **kwargs):
        # ここでプロジェクトの投稿を受け付ける
        # プロジェクトの投稿とプロジェクトに紐づく素材の保存もセットでやる。
        # .getlist()を使う。

        copied          = request.POST.copy()
        copied["user"]  = request.user

        form    = ProjectForm(copied)

        if not form.is_valid():
            messages.error(request, "プロジェクトの投稿に失敗しました")
            return redirect("diy:project")

        project         = form.save()

        # 素材を使用しないプロジェクトの場合はMaterialの追加はせず終了する。
        names   = request.POST.getlist("name")
        amounts = request.POST.getlist("amount")

        for name,amount in zip(names, amounts):
            dic = {}
            dic["name"]     = name
            dic["amount"]   = amount
            dic["project"]  = project
            dic["user"]     = request.user

            form    = MaterialForm(dic)

            if form.is_valid():
                form.save()

        messages.success(request, "プロジェクトの投稿に成功しました")

        return redirect("diy:project_create")

project_create  = ProjectCreateView.as_view()


# プロジェクトの編集・削除を受け付ける
class ProjectModView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):

        context = {}
        project = Project.objects.filter(id=pk, user=request.user).first()

        if not project:
            messages.error(request, "プロジェクトがありません")
            return redirect("diy:index")

        context["project"]  = project

        return render(request, "diy/project_mod.html", context)


    def post(self, request, pk, *args, **kwargs):
        data    = {}
        project = Project.objects.filter(id=pk, user=request.user).first()

        if not project:
            messages.error(request, "プロジェクトの編集に失敗しました")
            return JsonResponse(data)

        copied          = request.POST.copy()
        copied["user"]  = request.user

        form    = ProjectForm(copied, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, "プロジェクトの編集に成功しました")
        else:
            messages.error(request, "プロジェクトの編集に失敗しました")


        ## TODO:素材の編集処理はどう実現させる？ ← また別途ビューを作るか？

        return JsonResponse(data)

    def delete(self, request, pk, *args, **kwargs):

        data    = {}
        project = Project.objects.filter(id=pk, user=request.user).first()

        if project:
            project.delete()
            messages.success(request, "プロジェクトの削除に成功しました")
        else:
            messages.error(request, "プロジェクトの削除に失敗しました")

        return JsonResponse(data)

project_mod     = ProjectModView.as_view()


# プロジェクトの個別ページ

class ProjectSingleView(View):
    def get(self, request, pk, *args, **kwargs):

        #ここでプロジェクトの個別ページを表示。
        #フィードバックの一覧も表示

        context                 = {}
        context["project"]      = Project.objects.filter(id=pk).first()
        context["materials"]    = Material.objects.filter(project=pk).order_by("dt")

        feedbacks   = Feedback.objects.filter(project=pk).order_by("-dt")
        paginator   = Paginator(feedbacks,LIST_PER_PAGE)

        if "feedback_page" in request.GET:
            context["feedbacks"]    = paginator.get_page(request.GET["feedback_page"])
        else:
            context["feedbacks"]    = paginator.get_page(1)


        return render(request, "diy/project_single.html", context)

    def post(self, request, pk, *args, **kwargs):
        # TODO:ここでフィードバックを受け付ける

        copied              = request.POST.copy()
        copied["user"]      = request.user
        copied["project"]   = pk

        form    = FeedbackForm(copied)

        if form.is_valid():
            messages.success(request, "フィードバックを受け付けました！")
            form.save()
        else:
            messages.error(request, "フィードバックの投稿に失敗しました")

        return redirect("diy:project_single", pk)

    def delete(self, request, pk, *args, **kwargs):
        pass
    def put(self, request, pk, *args, **kwargs):
        pass
    def patch(self, request, pk, *args, **kwargs):
        pass

project_single  = ProjectSingleView.as_view()


# コミュニティ一覧表示
class CommunityView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        query   = Q()

        if "search" in request.GET:
            words   = request.GET["search"].replace("　"," ").split(" ")

            for word in words:
                if word == "":
                    continue

                query &= Q(name__contains=word)

        communities     = Community.objects.filter(query).order_by("-dt")

        #TODO: 1ページに表示させるコンテンツ数は？
        paginator       = Paginator(communities,LIST_PER_PAGE)

        if "community_page" in request.GET:
            context["communities"]  = paginator.get_page(request.GET["community_page"])
        else:
            context["communities"]  = paginator.get_page(1)


        return render(request, "diy/community.html", context)


    def post(self, request, *args, **kwargs):
        #TODO :ここでコミュニティの作成

        copied              = request.POST.copy()
        copied["user"]      = request.user

        form    = CommunityForm(copied)

        if form.is_valid():
            messages.success(request, "コミュニティの作成を受け付けました！")
            form.save()
        else:
            messages.error(request, "コミュニティの作成に失敗しました")

        return redirect("diy:community")


    def delete(self, request, *args, **kwargs):
        # コミュニティの削除
        pass

    def put(self, request, *args, **kwargs):
        # コミュニティの編集
        pass

    def patch(self, request, *args, **kwargs):
        # コミュニティに参加申請？
        pass
    

community   = CommunityView.as_view()


# コミュニティ個別ページ
class CommunitySingleView(View):

    def get(self, request, pk, *args, **kwargs):

        #ここでコミュニティの個別ページを表示。コミュニティ内のトピックも表示
        context                     = {}
        context["community"]        = Community.objects.filter(id=pk).first()
        community_topics            = CommunityTopic.objects.filter(community=pk).order_by("-dt")

        #TODO: 1ページに表示させるコンテンツ数は？
        paginator       = Paginator(community_topics,LIST_PER_PAGE)

        if "community_topic_page" in request.GET:
            context["community_topics"]  = paginator.get_page(request.GET["community_topic_page"])
        else:
            context["community_topics"]  = paginator.get_page(1)


        print(context["community_topics"])

        return render(request, "diy/community_single.html", context)

    def post(self, request, pk, *args, **kwargs):
        #TODO :ここでコミュニティのトピックの作成

        copied              = request.POST.copy()
        copied["community"] = pk
        copied["user"]      = request.user

        form    = CommunityTopicForm(copied)

        if form.is_valid():
            messages.success(request, "トピックの作成を受け付けました！")
            form.save()
        else:
            messages.error(request, "トピックの作成に失敗しました")

        return redirect("diy:community_single", pk)

community_single    = CommunitySingleView.as_view()


# コミュニティトピックの個別ページ
class CommunityTopicView(View):

    def get(self, request, pk, *args, **kwargs):

        context                     = {}
        context["community_topic"]  = CommunityTopic.objects.filter(id=pk).first()

        community_messages  = CommunityMessage.objects.filter(community_topic=pk).order_by("-dt")
        paginator           = Paginator(community_messages,LIST_PER_PAGE)

        if "community_message_page" in request.GET:
            context["community_messages"]  = paginator.get_page(request.GET["community_message_page"])
        else:
            context["community_messages"]  = paginator.get_page(1)

        context["form"]     = CommunityMessageForm()

        return render(request, "diy/community_topic.html", context)

    def post(self, request, pk, *args, **kwargs):

        copied                      = request.POST.copy()
        copied["community_topic"]   = pk
        copied["user"]              = request.user

        form    = CommunityMessageForm(copied)

        if form.is_valid():
            messages.success(request, "メッセージの投稿を受け付けました！")
            form.save()
        else:
            messages.error(request, "メッセージの投稿に失敗しました")

        return redirect("diy:community_topic", pk)

community_topic     = CommunityTopicView.as_view()


# マイページビュー
class MypageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        context             = {}
        context["form"]     = CustomUserForm()

        projects            = Project.objects.filter(user=request.user).order_by("-dt")
        paginator           = Paginator(projects,LIST_PER_PAGE)

        if "project_page" in request.GET:
            context["projects"] = paginator.get_page(request.GET["project_page"])
        else:
            context["projects"] = paginator.get_page(1)

    
        # TODO: 多対多のフィールドに含まれているかチェックするにはこれで良いのか？
        communities         = Community.objects.filter(members=request.user).order_by("-dt")
        paginator           = Paginator(communities,LIST_PER_PAGE)

        if "community_page" in request.GET:
            context["communities"]  = paginator.get_page(request.GET["community_page"])
        else:
            context["communities"]  = paginator.get_page(1)


        favorites           = Favorite.objects.filter(user=request.user).order_by("-dt")
        paginator           = Paginator(favorites,LIST_PER_PAGE)

        if "favorite_page" in request.GET:
            context["favorites"] = paginator.get_page(request.GET["favorite_page"])
        else:
            context["favorites"] = paginator.get_page(1)


        return render(request, "diy/mypage.html", context)

    def post(self, request, *args, **kwargs):

        user    = CustomUser.objects.filter(id=request.user.id).first()
        form    = CustomUserForm(request.POST, instance=user)

        if form.is_valid():
            messages.success(request, "ユーザー情報の編集を受け付けました！")
            form.save()
        else:
            messages.error(request, "ユーザー情報の編集に失敗しました")

        return redirect("diy:mypage")

mypage  = MypageView.as_view()


class UserView(View):
    def get(self, request, pk, *args, **kwargs):

        context             = {}
        context["user"]     = CustomUser.objects.filter(id=pk).first()

        projects            = Project.objects.filter(user=request.user).order_by("-dt")
        paginator           = Paginator(projects,LIST_PER_PAGE)

        if "project_page" in request.GET:
            context["projects"] = paginator.get_page(request.GET["project_page"])
        else:
            context["projects"] = paginator.get_page(1)

        # TODO: 多対多のフィールドに含まれているかチェックするにはこれで良いのか？
        communities         = Community.objects.filter(members=request.user).order_by("-dt")
        paginator           = Paginator(communities,LIST_PER_PAGE)

        if "community_page" in request.GET:
            context["communities"]  = paginator.get_page(request.GET["community_page"])
        else:
            context["communities"]  = paginator.get_page(1)

        return render(request, "diy/user.html", context)

user    = UserView.as_view()


# お気に入りフォルダ機能のオミット検討中
class FavoriteFolderView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        return render(request, "diy/favorite_folder.html")

    def post(self, request, *args, **kwargs):
        #TODO:お気に入りフォルダの新規作成。
        return redirect("diy:favorite_folder")

    def delete(self, request, *args, **kwargs):
        #TODO: お気に入りフォルダの削除
        return redirect("diy:favorite_folder")

favorite_folder = FavoriteFolderView.as_view()




class FavoriteView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        data    = {}

        copied          = request.POST.copy()
        copied["user"]  = request.user

        form    = FavoriteForm(copied)

        if form.is_valid():

            cleaned     = form.clean()
            # すでに存在する場合は削除する(お気に入り解除)
            favorites   = Favorite.objects.filter(project=cleaned["project"])

            if favorites:
                messages.success(request, "お気に入り解除しました！")
                favorites.delete()
            else:
                form.save()
                messages.success(request, "お気に入り登録しました！")

        else:
            messages.success(request, "お気に入り登録失敗しました")

        return JsonResponse(data)
    
    # オミット検討中
    def patch(self, request, *args, **kwargs):
        #TODO:指定したお気に入りフォルダへ移動させる
        return redirect("bbs:index")

favorite    = FavoriteView.as_view()

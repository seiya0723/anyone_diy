from django.shortcuts import render, redirect
from django.views import View


# DRF
# from rest_framework.views import APIView as View


# 検索+ページネーション
from django.db.models import Q
from django.core.paginator import Paginator 


# Ajax用
from django.http.response import JsonResponse
from django.template.loader import render_to_string





class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        #TODO: コミュニティとプロジェクトの一部をコンテキストへ


        return render(request, "diy/index.html")

    #TODO:トップページのPOSTは不要かも？
    def post(self, request, *args, **kwargs):
        return redirect("diy:index")

index   = IndexView.as_view()


# プロジェクトの個別ページ
class ProjectView(View):
    def get(self, request, pk, *args, **kwargs):

        #ここでプロジェクトの個別ページを表示。
        #フィードバックの一覧も表示

        """
        context                 = {}
        context["project"]      = Project.objects.filter(id=pk).first()
        context["feedbacks"]    = Feedback.objects.filter(project=pk).order_by("-dt")

        """


        return render(request, "diy/project.html")

    def post(self, request, pk, *args, **kwargs):
        # TODO:ここでフィードバックを受け付ける?

        return redirect("diy:project", pk)

    def delete(self, request, pk, *args, **kwargs):
        pass
    def put(self, request, pk, *args, **kwargs):
        pass
    def patch(self, request, pk, *args, **kwargs):
        pass

project = ProjectView.as_view()






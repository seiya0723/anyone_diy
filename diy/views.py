from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "diy/index.html")


    def post(self, request, *args, **kwargs):

        return redirect("diy:index")

index   = IndexView.as_view()



# プロジェクトの個別ページ

"""
class ProjectView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bbs/index.html")

    def post(self, request, *args, **kwargs):
        return redirect("bbs:index")
"""

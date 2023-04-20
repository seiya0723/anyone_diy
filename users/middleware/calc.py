class Totalling:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        
        # 認証済みであり、管理ユーザーのみ集計結果をリクエストオブジェクトに追加する。
        if request.user.is_authenticated and request.user.is_staff:
            
            from ..models import CustomUser

            from diy.models import Project

            
            # 総会員数
            request.ALL_USER    = CustomUser.objects.filter(is_active=True, is_staff=False).count()

            # 無料会員数
            request.FREE_USER   = CustomUser.objects.filter(is_active=True, is_staff=False, customer=None).count()

            # 有料会員数
            request.PAID_USER   = CustomUser.objects.filter(is_active=True, is_staff=False).exclude(customer=None).count()

            # プロジェクト数
            request.PROJECTS   = Project.objects.all().count()




        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


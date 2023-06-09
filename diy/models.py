from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.conf import settings


from django.contrib.sites.models import Site

from django.db.models import Avg

import uuid

MAX_STAR    = 5

class Category(models.Model):

    class Meta:
        verbose_name_plural = "カテゴリ"

    id      = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name    = models.CharField(verbose_name="カテゴリ名",max_length=20)

    def __str__(self):
        return self.name

    def str_id(self):
        return str(self.id)

    
class Project(models.Model):

    class Meta:
        verbose_name_plural = "プロジェクト"


    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    thumbnail   = models.ImageField(verbose_name="サムネイル",upload_to="diy/project/thumbnail",null=True,blank=True)

    category    = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.PROTECT)
    title       = models.CharField(verbose_name="タイトル",max_length=20)

    # 説明文はもう少し短くても良いのでは？作業工程をSummernoteを使用してwysiwygのTextFieldにする場合は。
    description = models.CharField(verbose_name="説明文",max_length=1000)

    time        = models.IntegerField(verbose_name="所要時間(分)", validators=[ MinValueValidator(0)  ])
    level       = models.IntegerField(verbose_name="作業難度", validators=[ MinValueValidator(1), MaxValueValidator(5) ])
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)

    process     = models.TextField(verbose_name="作業工程(作業内容)")



    #TODO: ここに星の平均点を出す。
    def avg_star_score(self):
        feedbacks   = Feedback.objects.filter(project=self.id).aggregate(Avg("star"))
        
        if feedbacks["star__avg"]:
            return feedbacks["star__avg"]
        else:
            return 0

    def avg_star_icon_few(self):
        feedbacks   = Feedback.objects.filter(project=self.id).aggregate(Avg("star"))
        avg         = feedbacks["star__avg"]

        #平均スコアなしの場合は0を返す
        if not avg:
            return 0

        few     = avg - int(avg)

        if 0.4 > few and few >= 0:
            return 0
        elif 0.6 > few and few >= 0.4:
            return 0.5
        else:
            return 1 

    def feedback_amount(self):
        return Feedback.objects.filter(project=self.id).count()



    def str_level(self):
        return str(self.level)
    
    
    def __str__(self):
        return self.title



class Material(models.Model):

    class Meta:
        verbose_name_plural = "素材"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name        = models.CharField(verbose_name="素材名",max_length=20)
    amount      = models.CharField(verbose_name="分量・数量",max_length=20)
    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


class Feedback(models.Model):

    class Meta:
        verbose_name_plural = "フィードバック"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    comment     = models.CharField(verbose_name="コメント",max_length=1000)
    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)
    star        = models.IntegerField(verbose_name="星",validators=[MinValueValidator(1),MaxValueValidator(MAX_STAR)])

    def star_icon(self):
        dic                 = {}
        dic["true_star"]    = self.star * " "
        dic["false_star"]   = (MAX_STAR - self.star) * " "

        return dic


# オミット予定
class FavoriteFolder(models.Model):

    class Meta:
        verbose_name_plural = "お気に入りフォルダ"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    title       = models.CharField(verbose_name="タイトル",max_length=20)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Favorite(models.Model):

    class Meta:
        verbose_name_plural = "お気に入り"

    id              = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt              = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    project         = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)
    
    favorite_folder = models.ForeignKey(FavoriteFolder, verbose_name="お気に入りフォルダ", on_delete=models.CASCADE, null=True,blank=True)



class Community(models.Model):

    class Meta:
        verbose_name_plural = "コミュニティ"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name        = models.CharField(verbose_name="コミュニティ名",max_length=20)
    thumbnail   = models.ImageField(verbose_name="サムネイル",upload_to="diy/community/thumbnail",null=True,blank=True)

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", verbose_name="投稿者",on_delete=models.CASCADE)
    members     = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+", verbose_name="メンバー")

    # 会員数の合計を計算
    def total_members(self):
        return len(self.members.all())

    def __str__(self):
        return self.name


class CommunityTopic(models.Model):

    class Meta:
        verbose_name_plural = "コミュニティトピック"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    title       = models.CharField(verbose_name="タイトル",max_length=20)

    thumbnail   = models.ImageField(verbose_name="サムネイル",upload_to="diy/topic/thumbnail",null=True,blank=True)
    community   = models.ForeignKey(Community,verbose_name="コミュニティ",on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class CommunityMessage(models.Model):

    class Meta:
        verbose_name_plural = "コミュニティメッセージ"

    id              = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt              = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    community_topic =  models.ForeignKey(CommunityTopic,verbose_name="コミュニティトピック",on_delete=models.CASCADE)
    comment         = models.TextField(verbose_name="コメント")
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)




# 会社概要と利用規約
class Information(models.Model):
    class Meta:
        verbose_name_plural = "会社概要と利用規約"

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    overview    = models.TextField(verbose_name="会社概要")
    term        = models.TextField(verbose_name="会社概要")

    site_id     = models.OneToOneField(Site,verbose_name="サイトID",on_delete=models.CASCADE,null=True,blank=True)



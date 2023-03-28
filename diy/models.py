from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.conf import settings

import uuid

class Category(models.Model):
    id      = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name    = models.CharField(verbose_name="カテゴリ名",max_length=20)

    
class Project(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    category    = models.ForeignKey(Category,verbose_name="カテゴリ名",on_delete=models.PROTECT)
    name        = models.CharField(verbose_name="プロジェクト名",max_length=20)
    description = models.CharField(verbose_name="説明文",max_length=1000)

    time        = models.IntegerField(verbose_name="所要時間", validators=[ MinValueValidator(0)  ])
    level       = models.IntegerField(verbose_name="作業難度", validators=[ MinValueValidator(1), MaxValueValidator(5) ])

    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


class Process(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    
    # Project投稿時にgetlistを使用して上から順番に番号を振る
    turn        = models.IntegerField(verbose_name="工程番号")
    description = models.CharField(verbose_name="説明文",max_length=500)

    image       = models.ImageField(verbose_name="画像",upload_to="diy/process/image/",null=True,blank=True)

    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


class Material(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    name        = models.CharField(verbose_name="素材名",max_length=20)
    amount      = models.CharField(verbose_name="分量・数量",max_length=20)

    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


class Feedback(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    comment     = models.CharField(verbose_name="コメント",max_length=1000)
    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)

    #star        = models.IntegerField(verbose_name="星",validators=[MinValueValidator(1),MaxValueValidator(5)])


class Favorite(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    project     = models.ForeignKey(Project,verbose_name="プロジェクト",on_delete=models.CASCADE)
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


class Community(models.Model):
    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name        = models.CharField(verbose_name="コミュニティ名",max_length=20)

    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)
    #members     = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="メンバー")

class CommunityMessage(models.Model):

    id          = models.UUIDField(verbose_name="ID",default=uuid.uuid4,primary_key=True,editable=False )
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    comment     = models.CharField(verbose_name="コメント",max_length=1000)

    #image         = models.ImageField(verbose_name="画像")
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)
    #community   = models.ForeignKey(Community,verbose_name="コミュニティ",on_delete=models.CASCADE)


from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=128)
    password = models.CharField('密码',max_length=128)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.username

class Subject(models.Model):
    no = models.AutoField(primary_key=True,verbose_name='编号')
    name = models.CharField(max_length=50,verbose_name='名称')
    intro = models.CharField(max_length=1000,verbose_name='介绍')
    is_hot = models.BooleanField(verbose_name='是否热门')

    class Meta:
        managed = False
        db_table = 'tb_subject'
        verbose_name='科目'
        verbose_name_plural = '科目'

class Teacher(models.Model):
    no = models.AutoField(primary_key=True,verbose_name='编号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    sex = models.BooleanField(default=True,verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='个人介绍')
    photo = models.ImageField(max_length=255, verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='sno')

    class Meta:
        managed = False
        db_table = 'tb_teacher'
        verbose_name='老师'
        verbose_name_plural = '老师'


class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name="问题内容")
    pub_date = models.DateField(verbose_name="发布日期")

    class Meta:
        managed = False
        db_table = 'glenapp_question'
        verbose_name = "问题"
        verbose_name_plural = "问题"

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # タスクの形式を定義
    TYPE_CHOICES = (
        ('text', 'テキスト'),
        ('checkbox', 'チェックボックス'),
        ('file', 'ファイル'),
    )
    name = models.CharField(max_length=30) # タスク名
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 作成者（講師）
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES) # 課題の種類
    closing = models.DateTimeField() # 締切日時（講師が設定）
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時（自動設定）
    text = models.TextField() # 課題の説明（講師が入力）
    # チェックボックス形式で提出させる場合
    checkboxes = models.ManyToManyField('CheckboxOption', blank=True) # チェックボックスを詰めるフィールド

    def __str__(self):
        return self.name

class CheckboxOption(models.Model):
    append_task = models.ForeignKey(Task, on_delete=models.CASCADE) # 対象タスク
    label = models.CharField(max_length=100) # ラベル（名前）

    def __str__(self):
        return self.label



class Submission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 提出者
    task = models.ForeignKey(Task, on_delete=models.CASCADE) # 対象のタスク
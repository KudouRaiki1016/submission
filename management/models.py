from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=30) # タスク名
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 作成者（タスクの）
    text = models.TextField() # テキスト（作成者が入力するタスクに関するテキスト）
    closing = models.DateTimeField() # 締切日時（作成者が設定する）
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時（作成時に自動設定される）
    def __str__(self):
        return self.name

class Submission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 提出者
    task = models.ForeignKey(Task, on_delete=models.CASCADE) # 対象のタスク
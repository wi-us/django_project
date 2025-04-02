from django.db import models
import datetime
from django.db.models import Sum
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''Данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100, blank=False)
    short_description = models.CharField('Краткое описание', max_length=200, blank=False)
    description = models.TextField('Текст записи', blank=False)
    author = models.CharField("Имя автора", max_length=100, default="wius", blank=True)
    date = models.DateField("Дата публикации", default=timezone.now(), blank=True)
    img = models.ImageField('Изображение', null=True, upload_to='image/%Y', default="image/defaul.png", blank=True)
    rating = models.FloatField('Рейтинг', max_length=5, default=0.0 ,editable=False)
    comments_number = models.IntegerField('Количество комментариев', default=0 ,editable=False)
    def __str__(self):
        return f'{self.title}, {self.author}'
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''Комментарий'''
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    date = models.DateField("Дата публикации комментария", default=datetime.datetime.now().date())
    time = models.TimeField("Время публикации комментария", default=datetime.datetime.now().time())
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.post}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
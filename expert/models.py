from django.db import models
from django.utils.translation import gettext_lazy as _


class People(models.Model):
    EVAL_CHOICES= (
        (5, '아주 높음'),
        (4, '높음'),
        (3, '보통'),
        (2, '약함'),
        (1, '취약')
    )
    name = models.CharField(max_length=100)
    writer = models.CharField(_('작성자'), max_length=100)
    affiliation = models.CharField(_('소속'), max_length=200)
    position = models.CharField(_('직책'), max_length=100)
    fields = models.CharField(max_length=50, help_text='주요분야 선택, 두개 이상 선택 가능')
    address = models.TextField(_('주소'), blank=True)
    ev1 = models.IntegerField(_('전문성'), choices=EVAL_CHOICES, help_text='5가지 선택지 중 하나를 선택해 주세요.')
    ev2 = models.IntegerField(_('성실성'), choices=EVAL_CHOICES, help_text='5가지 선택지 중 하나를 선택해 주세요.')
    etc = models.TextField(_('비고'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

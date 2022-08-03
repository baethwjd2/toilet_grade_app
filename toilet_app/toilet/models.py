from django.db import models

from core.models import CoreModel

class AbstractItem(CoreModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return self.name

class Toilet(CoreModel):

    GENDER = [
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        ('BOTH', 'BOTH')
    ]
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    gender = models.CharField(max_length=5, choices=GENDER)
    isBisexual = models.BooleanField(default=False)
    manToiletNum = models.IntegerField(default=0, null=True, help_text="남성용 대변기의 숫자")
    womanToiletNum = models.IntegerField(default=0, null=True, help_text="여성용 대변기의 숫자")
    urinalNum = models.IntegerField(default=0, null=True, help_text="소변기의 숫자")
    manDisabledToiletNum = models.IntegerField(default=0, null=True, help_text="남자 장애인용 대변기 숫자")
    womanDisabledToiletNum = models.IntegerField(default=0, null=True, help_text="여자 장애인용 대변기 숫자")
    disabledUrinalNum = models.IntegerField(default=0, null=True, help_text="장애인용 소변기 숫자")
    manChildToiletNum = models.IntegerField(default=0, null=True, help_text="남자 어린이용 대변기 숫자")
    womanChildToiletNum = models.IntegerField(default=0, null=True, help_text="여자 어린이용 대변기 숫자")
    childUrinalNum = models.IntegerField(default=0, null=True, help_text="어린이용 소변기 숫자")
    managementAgency = models.CharField(max_length=140, help_text="설치 기관명")
    phoneNumber = models.CharField(max_length=11)
    openTime = models.CharField(max_length=140)
    installationDate = models.CharField(max_length=140, null=False)
    latitude = models.DecimalField(help_text="위도", max_digits=500, decimal_places=2, null=True)
    longitude = models.DecimalField(help_text="경도", max_digits=500, decimal_places=2, null=True)
    distance = models.DecimalField(help_text="경도", max_digits=500, decimal_places=2, null=True, default=0)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile

# Create your models here.

# class User(AbstractUser):
#     pass

#-------------------------------------------------------------------------------------------------------------------------
class Airport(models.Model):
    icao_code = models.CharField(max_length=4, null=False, blank=False, unique=True) #valid upper case ENG alphabet
    city = models.CharField(max_length=30, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    runway_length = models.IntegerField(null=False)
    runway_direction = models.CharField(max_length=30,  null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.icao_code} {self.city} ({self.country})"

#-------------------------------------------------------------------------------------------------------------------------
class Flight(models.Model):
    
    origin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name="arivals")
    duration = models.IntegerField(help_text='duration in minute')

#-------------------------------------------------------------------------------------------------------------------------
class Division(models.Model):
    class Meta():
        ordering = ['id']
    department = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.department}"

#-------------------------------------------------------------------------------------------------------------------------
class Position(models.Model):
    class Meta():
        ordering = ['id']

    department = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='department_position', blank=False, null=False, default=None)
    position = models.CharField(max_length=50, default=None)

    def __str__(self):
        return f"{self.position}"

#-------------------------------------------------------------------------------------------------------------------------
class RankManager(models.Manager):
    def get_by_natural_key(self, airforce_rank):
        return self.get(airforce_rank=airforce_rank)

class Rank(models.Model):

    class Meta():
        ordering = ['id']
        unique_together = [['airforce_rank']]
    
    airforce_rank = models.CharField(max_length=20, null=False, blank=False)

    objects = RankManager()

    def natural_key(self):
        return (self.airforce_rank)

    def __str__(self):
        return f"{self.airforce_rank}"


#-------------------------------------------------------------------------------------------------------------------------
def validate_image(image):
    """ ทำการ valid รูปภาพที่ user จะโหลดให้ไม่เกิน 500 Kb"""
    file_size = image.file.size
    limit_kb = 500
    if file_size > limit_kb * 1024:
        raise ValidationError(
            _('%(image)s is not more than 500 Kb'),
            params={'image': image},
        )
#-------------------------------------------------------------------------------------------------------------------------
class ExtendedEncoder(DjangoJSONEncoder):
    """ต้อง เพิ่ม class นี้เพราะไฟล์รูปภาพไม่สามารถแปลงเป็น JSON ตรงๆได้เลย"""
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)

class PictureManager(models.Manager):
    def get_by_natural_key(self, employee_image):
        return self.get(employee_image=employee_image)


class Picture(models.Model):
    class Meta():
        ordering = ['id']
        unique_together = [['employee_image']]

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None, null=False, related_name='employee_picture')
    employee_image = models.ImageField('Image', upload_to='image/', validators=[validate_image])

    objects = PictureManager()

    def natural_key(self):
        return (self.employee_image)

    def __str__(self):
        return f"{self.employee_image}"

#-------------------------------------------------------------------------------------------------------------------------

class Employee(models.Model):
    
    class Meta():
        ordering = ['first_name_thai']

    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='rank', blank=True, null=True)
    first_name_eng = models.CharField(max_length=64, blank=True, null=True)
    last_name_eng = models.CharField(max_length=64, blank=True, null=True)
    first_name_thai = models.CharField(max_length=64, blank=True, null=True)
    last_name_thai = models.CharField(max_length=64, blank=True, null=True)
    date_birth = models.DateField(default=None, null=True, blank=True, help_text='ปี ค.ศ. / เดือน / วัน (ตัวอย่าง 1990-09-01)')

    line_id = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=10, help_text='fill 10 number', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    picture = models.ForeignKey('Picture', on_delete=models.SET_NULL, related_name='employee_picture', blank=True, null=True)

    division = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='employee_division', blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='employee_position', blank=True, null=True)
    position_other = models.CharField(max_length=200, blank=True, null=True, default=None)
    lucky_number = models.DecimalField(max_digits=4,decimal_places=0, blank=True, null=True)
    afaps = models.IntegerField(default=None, null=True)

    passport = models.CharField(max_length=9, default=None, blank=True, null=True)
    visa = models.CharField(max_length=14, default=None, blank=True, null=True)

    still_service = models.BooleanField(default=True)
    is_pilot = models.BooleanField(default=False, null=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.first_name_thai}  {self.last_name_thai}"
    
    # def serialize(self):
    #     # print(self.rank.airforce_rank)
    #     return {
    #         "pk": self.pk,
    #         "rank": self.rank.airforce_rank,
    #         "first_name_eng": self.first_name_eng,
    #         "last_name_eng": self.last_name_eng,
    #         "first_name_thai": self.first_name_thai,
    #         "last_name_thai": self.last_name_thai,
    #         "date_birth": self.date_birth,
    #         "line_id": self.line_id,
    #         "telephone": self.telephone,
    #         "email": self.email,
    #         "picture": f'{self.picture}',
    #         "division": f'{self.division}',
    #         "position": f'{self.position}',
    #         "position_other": self.position_other,
    #         "lucky_number": self.lucky_number,
    #         "afaps": self.afaps,
    #         "passport": self.passport,
    #         "visa": self.visa,
    #         "still_service": self.still_service,
    #         "is_pilot": self.is_pilot,
    #         "create_at": self.create_at,
    #         "update": self.update.strftime("%b %d %Y, %I:%M %p"),
    #     }



class Lessonlearn(models.Model):
    class Meta():
        ordering = ['id']

    MISSON_CHOICES = ( 
    ("1", "Domestic"), 
    ("2", "International"), 
    )

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None, null=False, related_name='employee_Lessonlearn')
    airport = models.ForeignKey('Airport', on_delete=models.CASCADE, default=None, null=False, related_name='airport_Lessonlearn')
    title = models.CharField(max_length=300, blank=True, default=None)
    lesson = models.TextField(blank=False)
    mission = models.CharField(max_length=20 ,choices = MISSON_CHOICES, null=False,default='Domestic')
    date_fly = models.DateTimeField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)
    
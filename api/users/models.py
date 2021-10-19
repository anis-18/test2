from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from PIL import Image , ImageDraw
# Create your models here.



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
GENDER_CHOICES = (
    ("М", "Мужмкой"),
    ("Ж", "Женский"),
    
)

class Watermark(object):
    def process(self, image):
        width, height = image.size
        position =(0,0)
        image = image.convert("RGBA")
        watermark = Image.open('media/apptrix.jpg').convert("RGBA")
        transparent = Image.new('RGBA', (width, height), (0,0,0,0))
        transparent.paste(image, (0,0))
        transparent.paste(watermark, position, mask=watermark)
        return transparent
                                


    
class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=100, verbose_name='email', unique=True)
    gender = models.CharField(
        max_length = 20,
        choices = GENDER_CHOICES,
        default = 'М'
        )  
    avatar= ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(400, 400), Watermark()],
                                           format='JPEG',
                                           options={'quality': 72})    
    likes = models.ManyToManyField('User', blank=True, related_name="like")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    



# Create your models here.

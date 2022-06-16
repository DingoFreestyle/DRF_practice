from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc =  models.CharField(max_length=150, null=True, unique=True)

    def __str__(self):
        return self.name



class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('유저 이름 넣으세요')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    realname = models.CharField("이름", max_length=20)

    # False명 계정 비활성화(어드민은 ㄴㄴ)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # ID는 'username'를 사용하겠다
    USERNAME_FIELD = 'username'

    # 뭔지 특별히 기억할 필요 없음 꼭 쓰기(권한 관련)
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="이름", on_delete=models.CASCADE, primary_key=True)
    text = models.TextField("상태 메세지")

    def __str__(self):
        return f"{self.user.username}의 프로필"


from django.db import models


# Create your models here.

class Statistika(models.Model):
    nom = models.CharField(max_length=200)
    soni = models.IntegerField()

    def __str__(self):
        return f"{self.nom} | {self.soni}"

    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural = "Statistika"


class Jamoa(models.Model):
    nom = models.CharField(max_length=200)
    logotip = models.ImageField(upload_to='jamoa_rasm')
    jamoa_haqida = models.TextField()
    rasm1 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    rasm2 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} | {self.logotip} | {self.jamoa_haqida} | {self.rasm1} | {self.rasm2} | {self.rasm3}"

    class Meta:
        verbose_name = 'Jamoa'
        verbose_name_plural = 'Jamoa'


class Tarif(models.Model):
    rasm = models.ImageField(upload_to='blog_rasm')
    nom = models.CharField(max_length=200)
    malumot = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.nom} | {self.malumot} "

    class Meta:
        verbose_name = 'Tarif'
        verbose_name_plural = 'Tarif'


class Xizmat(models.Model):
    rasm1 = models.ImageField(upload_to='blog_rasm')
    rasm2 = models.ImageField(upload_to='blog_rasm')
    rasm3 = models.ImageField(upload_to='blog_rasm')

    def __str__(self):
        return f"{self.rasm1} | {self.rasm2}"

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = "Xizmatlar"


class Malumot(models.Model):
    malumot = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.malumot}"

    class Meta:
        verbose_name = 'Malumot'
        verbose_name_plural = 'Xususiyat_malumot'


class Xususiyat(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='blog_rasm')

    def __str__(self):
        return f"{self.nom}"

    class Meta:
        verbose_name = 'Xususiyat'
        verbose_name_plural = "Xususiyat"


class Boglanish(models.Model):
    nom = models.CharField(max_length=300)
    link = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nom} | {self.link}"

    class Meta:
        verbose_name = 'Boglanish'
        verbose_name_plural = "Boglanish"


class Link(models.Model):
    youtube = models.CharField(max_length=300, null=True, blank=True)
    instagram = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    telegram = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.youtube} | {self.instagram} | {self.facebook} | {self.telegram}"

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Link'


class Blog(models.Model):
    name = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(max_length=200)
    description = models.TextField()
    kurishlar = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} | {self.date}"

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

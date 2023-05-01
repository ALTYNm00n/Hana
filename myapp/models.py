from django.db import models
from datetime import date
from django.core.exceptions import ValidationError



# Create your models here.

# Create a class for Menu Category
class Home_restaurant(models.Model):
    logo= models.ImageField (upload_to="image/",null=True, blank=True)
    name= models.CharField(max_length=120,verbose_name='Название',null=True, blank=True)
    description= models.TextField(verbose_name='Описание',null=True, blank=True)
    phone_number=models.CharField(max_length=120,verbose_name='Номер телефона')
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name= 'Главная страница'
        verbose_name_plural = 'Главная страница'


# Create a class for Menu items 
class MenuItem(models.Model):
    home_restaurant = models.ForeignKey(Home_restaurant, on_delete=models.CASCADE, related_name='menuitems',  blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name='названи еды')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена')
    image = models.ImageField(upload_to='MenuItem/',verbose_name='Фото')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюды'

# Create a class for comming soon items
class ComingSoon(models.Model):
    menu_category = models.ForeignKey(Home_restaurant, on_delete=models.CASCADE, related_name='comsoon', blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name='название')
    image = models.ImageField(upload_to='ComingSoon/',verbose_name='Фото')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата создание')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Скоро выйдет'
        verbose_name_plural = 'Скоро выйдет'


# Create a class for restaurant info
class RestaurantInfo(models.Model):
    home_restaurant = models.ForeignKey(Home_restaurant, on_delete=models.CASCADE, related_name='restaurants_infos',  blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, verbose_name='Заголовок')
    description =models.TextField(verbose_name='Описание2' ,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True, verbose_name= 'Адрес')
    phone = models.CharField(max_length=200,blank=True, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта',null=True,blank=True)
    hours = models.CharField(max_length=200,blank=True, verbose_name='время')
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О наc'

# Create a class for contact info
class ContactInfo(models.Model):
    home_restaurant = models.ForeignKey(Home_restaurant, on_delete=models.CASCADE, related_name='contactinfos',  blank=True, null=True)
    name = models.CharField(max_length=120,verbose_name='Название',null=True, blank=True)
    email = models.EmailField(verbose_name='Почта',null=True,blank=True)
    message = models.TextField(verbose_name='обращение для посетителей')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        

class ClientReview(models.Model):
    home_restaurant = models.ForeignKey(Home_restaurant, on_delete=models.CASCADE, related_name='client_rewiwes', blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name='Имя')
    review = models.TextField(verbose_name='Отзыв', blank=True)
    star_nbr = models.PositiveIntegerField(default=0, blank=True, verbose_name='Оценка')
    def __str__(self):
        return self.name
    def clean(self):
        if self.star_nbr > 5:
            raise ValidationError('Оценк должна быть от 1 до 5')
    

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = verbose_name + 'ы'
        
# Create a class for About info
# class AboutInfo(models.Model):
#     menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='aboutinfos')
#     title = models.CharField(max_length=200,blank=True)
#     description = description = models.TextField(verbose_name='описание')

#     def __str__(self):
#         return self.title

# # Create a class for Client review


#     def __str__(self):
#         return self.name

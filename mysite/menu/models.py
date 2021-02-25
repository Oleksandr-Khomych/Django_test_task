from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    url = models.URLField()
    parent_element = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.menu_id} #{self.url}: parent:{self.parent_element}'


class Language(models.Model):
    language = models.CharField(max_length=5, primary_key=True)
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.language_name} : {self.language}'


class Translate(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)


# from menu.models import Menu, Language, Translate

# l = Language(language="ua", language_name="Ukrainian")
# l = Language(language="eng", language_name="English")

# q = Menu(menu_id=1, url="/admin", parent_element=None)
# q = Menu(menu_id=2, url="/blog", parent_element=None)
# q = Menu(menu_id=3, url="/authors", parent_element=None)
# q = Menu(menu_id=4, url="/author1", parent_element=3)
# q = Menu(menu_id=5, url="/author2", parent_element=3)
# q = Menu(menu_id=6, url="/author3", parent_element=3)

# t = Translate(menu_id=Menu.objects.get(menu_id=1), language=Language.objects.get(language="eng"), text="Admin Panel")
# t = Translate(menu_id=Menu.objects.get(menu_id=2), language=Language.objects.get(language="eng"), text="Blog")
# t = Translate(menu_id=Menu.objects.get(menu_id=3), language=Language.objects.get(language="eng"), text="Authors")
# t = Translate(menu_id=Menu.objects.get(menu_id=4), language=Language.objects.get(language="eng"), text="Author1")
# t = Translate(menu_id=Menu.objects.get(menu_id=5), language=Language.objects.get(language="eng"), text="Author2")
# t = Translate(menu_id=Menu.objects.get(menu_id=6), language=Language.objects.get(language="eng"), text="Author3")
#
# t = Translate(menu_id=Menu.objects.get(menu_id=1), language=Language.objects.get(language="ua"), text="Адмін Панель")
# t = Translate(menu_id=Menu.objects.get(menu_id=2), language=Language.objects.get(language="ua"), text="Блог")
# t = Translate(menu_id=Menu.objects.get(menu_id=3), language=Language.objects.get(language="ua"), text="Автори")
# t = Translate(menu_id=Menu.objects.get(menu_id=4), language=Language.objects.get(language="ua"), text="Автори1")
# t = Translate(menu_id=Menu.objects.get(menu_id=5), language=Language.objects.get(language="ua"), text="Автори2")
# t = Translate(menu_id=Menu.objects.get(menu_id=6), language=Language.objects.get(language="ua"), text="Автори3")




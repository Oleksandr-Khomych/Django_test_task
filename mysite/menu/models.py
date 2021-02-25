from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_ukr_text = models.CharField(max_length=50)
    menu_eng_text = models.CharField(max_length=50)
    url = models.URLField()
    parent_element = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.menu_id}:{self.menu_eng_text}/{self.menu_ukr_text}  #{self.url}: parent:{self.parent_element}'

# q = Menu(menu_id=1, menu_ukr_text="Адмін Панель", menu_eng_text="Admin Panel", url="/admin", parent_element=None)
# q = Menu(menu_id=2, menu_ukr_text="Блог", menu_eng_text="Blog", url="/blog", parent_element=None)
# q = Menu(menu_id=3, menu_ukr_text="Автори", menu_eng_text="Authors", url="/authors", parent_element=None)
# q = Menu(menu_id=4, menu_ukr_text="Автор1", menu_eng_text="Author1", url="/author1", parent_element=3)
# q = Menu(menu_id=5, menu_ukr_text="Автор2", menu_eng_text="Author2", url="/author2", parent_element=3)
# q = Menu(menu_id=6, menu_ukr_text="Автор3", menu_eng_text="Author3", url="/author3", parent_element=3)

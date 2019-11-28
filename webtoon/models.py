
# Create your models here.


from django.db import models


# Create your models here.
class WebToon(models.Model):
    webtoon_id = models.CharField(max_length=100, primary_key=True)
    site_name = models.CharField(max_length=50)
    webtoon_name = models.CharField(max_length=200)
    webtoon_author = models.CharField(max_length=100)
    webtoon_img_url = models.CharField(max_length=300)
    webtoon_views = models.IntegerField(default=0)
    webtoon_update = models.IntegerField(default=0)
    webtoon_status = models.IntegerField(default=0)
    webtoon_mon = models.IntegerField(default=0)
    webtoon_tue = models.IntegerField(default=0)
    webtoon_wed = models.IntegerField(default=0)
    webtoon_thu = models.IntegerField(default=0)
    webtoon_fri = models.IntegerField(default=0)
    webtoon_sat = models.IntegerField(default=0)
    webtoon_sun = models.IntegerField(default=0)

    def __str__(self):
        return self.site_name + " : " + self.webtoon_name


class Comment(models.Model):
    webtoon_id = models.CharField(max_length=100)
    comment_text = models.CharField(max_length=300)
    create_date_time = models.DateTimeField()
    rank = models.IntegerField(default=5)

    def __str__(self):
        return self.comment_text

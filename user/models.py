import re
from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=25,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.message

class slider(models.Model):
    headlines=models.TextField()
    slider_Dec=models.TextField()
    slider_picture=models.ImageField(upload_to='static/slider/',null=True)
    def __str__(self):
        return self.headlines

class category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    category_picture=models.ImageField(upload_to='static/categroy/',null=True)
    def __str__(self):
        return self.category_name

class city(models.Model):
    city_name=models.CharField(max_length=100,null=True)
    city_picture=models.ImageField(upload_to='static/city/',null=True)
    def __str__(self):
        return self.city_name

class mynews(models.Model):
    news_category=models.ForeignKey(category,on_delete=models.CASCADE)
    news_city=models.ForeignKey(city,on_delete=models.CASCADE)
    news_picture=models.ImageField(upload_to='static/news/',null=True)
    news_headlines=models.TextField()
    news_description=models.TextField()
    news_date=models.DateField()

    def __str__(self):
        return str(self.news_headlines)


class vnews(models.Model):
    vcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    headlines=models.TextField(null=True)
    news=models.TextField(null=True)
    vlink=models.CharField(max_length=300,null=True)
    news_data=models.DateField()

    def __str__(self):
        return str(self.headlines)

    def save(self, *args, **kwargs):
        self.vlink = self.convert_to_embed(self.vlink)
        super().save(*args, **kwargs)

    @staticmethod
    def convert_to_embed(url):
        if not url:
            return url

        # Agar already embed link hai to kuch mat karo
        if "embed" in url:
            return url

        video_id = None

        # watch?v=VIDEO_ID  ya  youtu.be/VIDEO_ID  dono handle karega
        match = re.search(r"(?:v=|youtu\.be/|embed/)([0-9A-Za-z_-]{11})", url)
        if match:
            video_id = match.group(1)

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"

        return url  # agar match na mile to jo tha wahi rehne do


class jobs(models.Model):
    job_title=models.CharField(max_length=200,null=True)
    job_link=models.CharField(max_length=200,null=True)
    job_picture=models.ImageField(upload_to='static/job',null=True)


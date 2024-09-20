import re

from django.db import models
from django.db.models import Max
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class PracticeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'


class StaticFilesModel(models.Model):
    image = models.ImageField(upload_to="images/")
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.image.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255, primary_key=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("changelogs-tag", kwargs={"tag_slug": self.slug})

    class Meta:
        ordering = ["slug"]


class ChangeLogManager(models.Manager):
    def get_last_modified(self):
        return self.filter(published_at__lte=timezone.now(), is_visible=True).aggregate(
            last_mod=Max("published_at")
        )["last_mod"]


class ChangeLog(models.Model):
    title = models.CharField(max_length=255)
    published_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    url_slug = models.SlugField(unique=True, blank=True, max_length=255)
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True, editable=False)
    is_visible = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    objects = ChangeLogManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.url_slug:
            published_at = self.published_at if self.published_at else timezone.now()

            title_with_date = f"{published_at.date().isoformat()} {self.title}"
            self.url_slug = slugify(title_with_date)

        self.short_description = self.description.split("---")[0]
        super(ChangeLog, self).save(*args, **kwargs)

    def has_more(self):
        if self.short_description is None:
            return True

        return self.description.strip() != self.short_description.strip()

    def get_absolute_url(self):
        return reverse("changelogs-detail", kwargs={"slug": self.url_slug})

    @property
    def markdown_image(self):
        image_urls = re.findall(r"!\[.*\]\((.+)\)", self.description)
        if len(image_urls) > 0:
            # remove title form url if there is any
            return image_urls[0].split(' "')[0]

        image_urls = re.findall(
            r"<img\s[^>]*?src\s*=\s*['\"]([^'\"]*?)['\"][^>]*?>", self.description
        )

        if len(image_urls):
            return image_urls[0]

        return ''

    @property
    def og_description(self):
        from django.template.defaultfilters import truncatewords_html

        description = self.description

        description = re.sub(r"!\[.*\]\((.+)\)", "", description)
        description = (
            description.replace("#", "").replace("*", "").replace("\n- ", "\n ")
        )
        description = re.sub(r"\s+", " ", description).strip()

        # Remove image tags
        description = re.sub("<[^<]+?>", "", description)
        return truncatewords_html(description, 30)

    class Meta:
        ordering = ["-published_at"]

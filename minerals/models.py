from django.db import models
from slugify import slugify


class Mineral(models.Model):
    name = models.TextField()
    slug = models.TextField()
    image_filename = models.TextField()
    image_caption = models.TextField()
    category = models.TextField()
    formula = models.TextField()
    strunz_classification = models.TextField()
    unit_cell = models.TextField()
    color = models.TextField()
    crystal_habit = models.TextField()
    mohs_scale_hardness = models.TextField()
    crystal_system = models.TextField()
    crystal_symmetry = models.TextField()
    cleavage = models.TextField()
    luster = models.TextField()
    streak = models.TextField()
    diaphaneity = models.TextField()
    optical_properties = models.TextField()
    refractive_index = models.TextField()
    specific_gravity = models.TextField()
    group = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # credit: https://stackoverflow.com/a/32333011/4373927
    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

from django.db import models

# Create fyour models here.
class LawFirm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    year_of_exp = models.PositiveIntegerField(verbose_name="Years of Experience")
    specialization = models.CharField(max_length=255)
    total_cases = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='lawfirm_images/', blank=True, null=True)

class AllCases(models.Model):
    case_title = models.CharField(max_length=100)
    case_description = models.TextField()
    case_image = models.ImageField(upload_to='caseimage/', blank=True, null=True)


from django.db import models



class ContactForm(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    email = models.CharField(max_length=255, unique=True, blank=False, primary_key=True)
    write_here = models.TextField(blank=True)

    class Meta:
        db_table = "portfolio_table"

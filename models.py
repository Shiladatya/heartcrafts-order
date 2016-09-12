from django.db import models
class Lin(models.Model):
	text = models.CharFiels(max_length=255)

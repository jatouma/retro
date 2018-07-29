from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Board(models.Model):
	sprint = models.CharField(max_length=64, unique=True)
	is_started = models.BooleanField(default=False)

	def __str__(self):
		return f"Sprint: {self.sprint}"

#Sticky is short for Sticky Note, Physical sticky notes are used on physical retro boards.
class Sticky(models.Model):
	parent_board = models.ForeignKey(Board, on_delete=models.PROTECT, default=1)
	user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
	note = models.CharField(max_length=512)
	created = models.DateTimeField(auto_now_add=True)

	def get_submitter(self):
		if self.user is not None:
			return self.user
		return "Anon"

	class Meta:
		abstract = True

class ActionItem(Sticky):
	is_completed = models.BooleanField(default=False)

	def __str__(self):
		return f"Action Item: {self.note}"

class Positive(Sticky):
	pass

	def __str__(self):
		return f"Positive: {self.note}"

class Delta(Sticky):
	pass

	def __str__(self):
		return f"Delta: {self.note}"




# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course_Manager(models.Manager):
	def basic_validation(self,postData):
		message=''
		if 'title' in postData:
			title = postData['title'].strip()
			if len(title)<5 :
				message = "Please enter more than 5 characters for the Title:"
				return message
		
		if 'description' in postData:
			desc = postData['description'].strip()
			if len(desc) < 15:
				message="Please enter more than 15 characters for the course description."
				return message
	
		return message

class Course(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Course_Manager()

class Description(models.Model):
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	course = models.OneToOneField(Course, related_name="desc", on_delete=models.CASCADE)
	objects = Course_Manager()

class Comment(models.Model):
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	coursecomment = models.ForeignKey(Course, related_name="comment", on_delete=models.CASCADE)
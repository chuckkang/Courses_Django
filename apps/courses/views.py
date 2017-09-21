from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
def index(request):
	context = GetCourseData()
	return render(request, "courses/index.html", context)


def delete(request, id):
	course_delete = {'course': GetCourseByID(id)}
	return render(request, "courses/delete.html", course_delete)

def delete_course(request):
	if request.method=="POST":
		if request.POST['confirm']=="yes":
			x = Course.objects.get(id=int(request.POST['course_id']))
			x.delete()
			messages.add_message(request, messages.INFO, "you course has been deleted")
	return redirect("/")
def comments(request, id):
	# if (Comment.objects.get(course=id).exists()):
	# 	print x, "ADSFASDFASDFASDFFDSA"
	# else:
	# 	print x, "132412341324"
	# print type(Comment.objects.get(course=id)), "THIS EXISTS"
	coursedata = Course.objects.get(id=8)
	x = Comment.objects.filter(coursecomment=coursedata)
	# Comment.objects.create(comment="THIS IS A ANOtheR CoMMENT", course=coursedata)
	# print Comment.objects.filter(coursecomment=int(id)), "Comment.objects.get(coursecomment=coursedata)"
	print x
	context = {
		'course': Course.objects.get(id=id),
		'description' : Description.objects.get(course=coursedata),
		'comments' : x
	}
	return render(request, 'courses/comments.html', context)
def add_comment(request):
	if request.POST['id']:
		course = Course.objects.get(id=request.POST['id'])
		comment = Comment.objects.create(comment=request.POST['comment'].strip(), coursecomment=course)
		messages.add_message(request, messages.INFO, "You have submitted your comments")

	return redirect("/comments/"+request.POST['id'])


def add_course(request):
	errMessage = ''
	isValid = False
	requestdata = {}
	if (request.method=="POST"):
		errMessage = Course.objects.basic_validation(request.POST)
		title = request.POST['title'].strip()
		description = request.POST['description'].strip()
		if (errMessage):
			messages.add_message(request, messages.INFO, errMessage)
		else:
			isValid = True
			key = Course.objects.create(title=title)
			objDesc = Description.objects.create(description=description,  course=key)
			messages.add_message(request, messages.INFO, "Your course has been added")

	return redirect ("/")

def GetCourseData():
	course_data = {'course_data': Course.objects.all()}
	return course_data

def GetCourseByID(id):
	course_data = Course.objects.get(id=id)
	return course_data
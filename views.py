from django.shortcuts import render
from.models import Contact,Blogs

def index(request):
	return render(request, 'mysite/index.html')

def about(request):
	return render(request, 'mysite/about.html')

def contact(request):
	if request.method == "POST":
		#DOSOMETHING
		email_r = request.POST.get('email')
		subject_r = request.POST.get('subject')
		message_r = request.POST.get('message')

		c = Contact(email= email_r,subject = subject_r ,message = message_r)
		c.save()

		return render(request, 'mysite/thanks.html')
	else:
		return render(request, 'mysite/contact.html')


def blogs(request):
	return render(request, 'mysite/blogs.html')

from django.shortcuts import render
# from django.template import loader

from django.http import HttpResponse

from .models import Classes, Student


# Create your views here.
def index(request):
    return HttpResponse("<h1 align='center'>FIRST RESPONSE 200</h1>")

def classesListing(request):
    classes = Classes.objects.all()
    
    context = {'classList': classes}
    return render(request, 'classesListing.html', context)
    # return HttpResponse("<h1 align='center'>Classes:</h1>")


def listStudents(request,className):
    listStud = '' # Student.objects.aggregate({'sClass': className})
    lis = Student.objects.all()
    
    context = {'listStud': lis, 'clName': Classes.objects.get(id=className)}
    return render(request, 'studentList.html', context)
    # return HttpResponse("You're looking at students of section %s." %className)

def studentDetails(request, studentid):
    lis = Student.objects.get(sRollNo=studentid)

    context = {'stud': lis}
    return render(request, 'student.html', context)

def newStudentAdd(request):
    listClass = Classes.objects.all()
    lisData = False
    POST_DATA = request.POST

    if(POST_DATA):
        lisData = True
        if(POST_DATA['Name'] != '' and POST_DATA['clss'] != '' and POST_DATA['number'] != ''):
            stud = Student(None, POST_DATA['Name'], POST_DATA['clss'], POST_DATA['number'])
            stud.save()

    context = {'listClass': listClass, 'showMsg': lisData}

    return render(request, 'addNewStud.html', context)


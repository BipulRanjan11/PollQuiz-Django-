from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *


def Test(request):
    return render(request, 'main/login.html', {})


@login_required
def view_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('demo:login'))


def Login(request):
    if request.method == 'POST':

        if 'register' in request.POST:
            user = User()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.username = request.POST['email']
            user.mobile = request.POST['mobile']
            user.set_password('password@123')
            user.save()
            userndpassword = UserNdPassword()
            userndpassword.username = user.email
            userndpassword.password = 'password@123'
            userndpassword.save()
            user.save()

        if 'login' in request.POST:

            username = request.POST["username"]
            password = request.POST["password"]
            print(username)
            print(password)
            if username is None or password is None:
                return HttpResponse('Please provide both username and password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET['next'])

                # return HttpResponse('valid Credentials')
                return redirect('dashboard/')
            else:
                return HttpResponse('Invalid Credentials')

    return render(request, 'main/login.html', {})


@login_required
def Dashboard(request):
    ques = Question.objects.all()
    context = {
        "ques":ques
    }

    return render(request, "main/dashboard.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'main/details.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'main/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('demo:results', args =(question.id, )))

@api_view(['POST'])
# @csrf_exempt
def save_question_result(request):
    data1 = dict(request.data)
    print(data1)
    question = data1.get('question')
    answer = data1.get('answer[]')
    print(answer)

    if question is None and answer is None:
        payload = {'data' : 'both question uid and answer uid are required' , 'status' : False}

        return Response(payload)

    question_obj = Question.objects.create(question_text = question[0], pub_date = datetime.now())
    for each in answer:
        print(each)
        Choice.objects.create(choice_text = each, question =question_obj )
        # answer_obj.counter += 1
        # answer_obj.save()

    payload = { 'status' : True}

    return Response(payload)

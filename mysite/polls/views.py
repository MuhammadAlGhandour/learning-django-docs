from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        '''
        Return the published questions (not including those set to be published in the future + the questions without choices)
        '''
        # here's the code i wrote to exclude the questions without choices
        # the logic works fine when i run the server, but in tests.py doesn't work
        # BY THE WAY i made the ordering of the questions using "class Meta" in models.py file go check it out
        # the old line was "return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")"
        questions_list = []
        for question in Question.objects.all():
            if len(question.choice_set.all()) != 0 and question.pub_date <= timezone.now():
                questions_list.append(question)
        return questions_list


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        """
        Excludes any question that aren't published yet> *in the future*
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk = question_id)
    try:        
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls.detail.html",
                        {
                            "question": question,
                            "error_message": "You didn't select a choice.",
                        },
                    )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

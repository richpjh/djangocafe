from django.shortcuts import render, redirect
from .models import Question, Choice

def home(request):
    return render(request, 'home.html')

def order(request):
    if request.method == "POST":
        if 'yes' in request.POST:
            questions = Question.objects.all()
            return render(request, 'menu.html', {'questions': questions})
        else:
            return render(request, 'goodbye.html')
    return render(request, 'order.html')

def order_details(request, question_id):
    if request.method == "POST":
        choices = request.POST.getlist('choices')
        total_price = 0
        selected_choices = Choice.objects.filter(id__in=choices)
        for choice in selected_choices:
            total_price += choice.price  # 가정: Choice 모델에 'price' 필드가 있다고 가정합니다.
        return render(request, 'order_summary.html', {'choices': selected_choices, 'total_price': total_price})
    else:
        question = Question.objects.get(id=question_id)
        return render(request, 'order_details.html', {'question': question})

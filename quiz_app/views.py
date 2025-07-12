from django.shortcuts import render, redirect
from .models import Question, Option
from .forms import QuizForm
import csv
import os
from django.conf import settings
from django.utils import timezone

def quiz_view(request):
    questions = list(Question.objects.all())

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            total = len(questions)
            result_data = []

            for question in questions:
                selected_option_id = int(form.cleaned_data.get(f"question_{question.id}"))
                selected_option = Option.objects.get(id=selected_option_id)
                is_correct = selected_option.is_correct
                if is_correct:
                    score += 1
                result_data.append({
                    'question': question.text,
                    'selected_option': selected_option.text,
                    'correct': 'Yes' if is_correct else 'No'
                })

            # Save to CSV
            timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
            filename = f"quiz_result_{timestamp}.csv"
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['question', 'selected_option', 'correct'])
                writer.writeheader()
                for row in result_data:
                    writer.writerow(row)

            return render(request, 'quiz_app/result.html', {
                'score': score,
                'total': total,
                'filename': filename
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_app/quiz.html', {'form': form})

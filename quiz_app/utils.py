import csv
import os
from django.conf import settings

def round_robin(questions, student_id):
    index = sum(ord(c) for c in student_id) % len(questions)
    return questions[index:] + questions[:index]

def save_result_to_csv(student_id, answers, score):
    file_path = os.path.join(settings.MEDIA_ROOT, 'results', 'marks.csv')
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            header = ['student_id'] + [f'q{i+1}' for i in range(len(answers))] + ['score']
            writer.writerow(header)

        writer.writerow([student_id] + list(answers.values()) + [score])

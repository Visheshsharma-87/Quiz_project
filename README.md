# 📝 Django Quiz System

A university-level quiz server built with Django, designed to handle simultaneous exam sessions for 200+ students. This system is ideal for academic institutions to conduct secure, scalable, and organized online exams.

## 🚀 Features

- 🔒 Admin Panel: Upload and manage quizzes.
- 🎯 Round-Robin Question Distribution: Every student gets a different set of questions.
- 📊 Results Stored Securely: CSV format stored server-side, invisible to students.
- 👨‍💻 Student Dashboard: Attempt assigned quizzes with time limits.
- 💡 Real-Time Evaluation: Score calculated and saved instantly after submission.
- 🔄 Attempt Locking: Students can’t retake the quiz once submitted.
- 🧠 Scalable: Tested for 200+ concurrent students.

## 🏗️ Tech Stack

- **Backend:** Django 4.x
- **Database:** SQLite (can be switched to PostgreSQL/MySQL easily)
- **Frontend:** HTML5, CSS3, JavaScript
- **Language:** Python 3.11+

## 📁 Folder Structure

Quiz_project/
│
├── quiz_app/ # Main application folder
│ ├── templates/ # HTML templates
│ ├── static/ # Static files (CSS, JS)
│ ├── models.py # DB Models for Quiz, Questions, Attempts
│ ├── views.py # Core logic for quiz handling
│ ├── urls.py # App-specific routes
│ └── ...
│
├── Quiz_project/ # Project settings folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── db.sqlite3 # Default database
├── manage.py # Django CLI
├── results/ # Stores CSV result files
└── README.md # Project documentation

bash
Copy
Edit

## ⚙️ How to Run Locally

1. **Clone the repo:**
   git clone https://github.com/Visheshsharma-87/Quiz_project.git
   cd Quiz_project
Create virtual environment & activate:

Edit
python -m venv venv
venv\Scripts\activate  # Windows
Install dependencies:

pip install -r requirements.txt
Apply migrations:

python manage.py migrate
Create superuser (admin):

python manage.py createsuperuser
Run the server:

python manage.py runserver
Visit: http://127.0.0.1:8000/ in your browser.

🧪 Demo Use-Case
Admin uploads questions and assigns to students.

Students visit login page and attempt quiz.

Once submitted, scores are calculated and stored in /results/quiz_results.csv.
# Quizard (SmartQuiz)

A simple Django web app for studying and taking quizzes. Pick a subject, pick a topic, answer multiple-choice questions — or build your own quiz bank through the admin.

Built with **Django 5.2** and **SQLite**.

## Features

- **Home page** with quick links to Study, Take Quiz, and Create Quiz.
- **Quiz browser** — select a subject, then a topic, then load its questions with choices.
- **Study materials** section (placeholder, ready to be filled in).
- **Create quiz** page (placeholder for authoring UI).
- **Django admin** for managing subjects, topics, questions, and answer choices.

## Project structure

```
quizard/
├── manage.py
├── db.sqlite3
├── quizard/          # project: settings, root urls, views, wsgi/asgi
├── templates/        # shared layout.html + home.html
├── quizapp/          # core models (Subject, Topic, Question, Choice) + quiz views
├── study/            # study materials app
└── take_quiz/        # quiz-taking app
```

### Data model

```
Subject 1──* Topic 1──* Question 1──* Choice (is_correct)
```

## Getting started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone <repo-url>
cd quizard/quizard

pip install django requests

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/

### Adding content

1. Go to http://127.0.0.1:8000/admin/
2. Create a **Subject**, then a **Topic** under it.
3. Add **Questions** to the topic and their **Choices**, ticking `is_correct` on the right answer.
4. Visit **Take Quiz** on the site to try them out.

## URLs

| Path | View | Description |
| --- | --- | --- |
| `/` | `quizard.views.homePage` | Landing page |
| `/quizapp/` | `quizapp.views.home` | Quiz app home |
| `/quizapp/take-quiz/` | `quizapp.views.take_quiz` | Browse subjects/topics and load questions |
| `/quizapp/create-quiz/` | `quizapp.views.create_quiz` | Create-quiz page |
| `/study/` | `study.views.studyer` | Study materials |
| `/take_quiz/` | `take_quiz.views.take_quiz` | Quiz-taking page |
| `/admin/` | Django admin | Manage quiz content |

## Notes & roadmap

- Answer scoring/auto-grading is not implemented yet — questions and choices are displayed, but submissions aren't graded.
- The create-quiz UI is a stub; quizzes are currently authored via the admin.
- `quizapp` and `take_quiz` define the same models; consolidating them into one app would remove the duplication.
- The project runs with `DEBUG = True` and the default insecure `SECRET_KEY` — change both before deploying.

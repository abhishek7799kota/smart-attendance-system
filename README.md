# Smart Attendance Management System

This is a Django-based web application developed to manage student attendance efficiently using real-world academic rules.

The system allows teachers to mark and view attendance, while students can view their attendance using their roll number.

---

## Project Features

### Teacher Features
- Teacher login using Django authentication
- Mark attendance for a selected date
- Attendance is not allowed on Sundays
- Attendance is not allowed on 2nd and 4th Saturdays
- View attendance reports with percentage calculation

### Student Features
- No login required
- Students can view attendance using roll number
- Displays total classes, present days, and attendance percentage

### Admin Features
- Add and manage students
- Manage attendance records
- Create teacher accounts using Django admin panel

---

## Technologies Used
- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- Git and GitHub

---

## Project Structure

Smart_Attendance_System/
├── attendance_project/
│ ├── manage.py
│ ├── attendance/ # Django App
│ └── attendance_project/ # Django Project
├── screenshots/
├── .gitignore
├── README.md




---

## How to Run the Project

1. Open terminal in the folder containing `manage.py`

2. Activate virtual environment:
```bash
venv\Scripts\activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Application URLs

Teacher Login: http://127.0.0.1:8000/teacher-login/

Teacher Dashboard: /teacher/

Mark Attendance: /mark/

Attendance Report: /report/

Student Attendance: /student/

Admin Panel: /admin/

Author

Kota Abhishek
B.Tech Student

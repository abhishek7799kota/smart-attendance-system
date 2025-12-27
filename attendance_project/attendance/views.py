from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from .models import Student, Attendance


def teacher_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'teacher_login.html', {'error': 'Invalid credentials'})
    return render(request, 'teacher_login.html')


def student_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and not user.is_staff:
            login(request, user)
            return redirect('student_dashboard')
        return render(request, 'student_login.html', {'error': 'Invalid credentials'})
    return render(request, 'student_login.html')


def user_logout(request):
    logout(request)
    return redirect('teacher_login')


@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})


def is_second_or_fourth_saturday(selected_date):
    """
    Returns True if the date is 2nd or 4th Saturday
    """
    if selected_date.weekday() != 5:  # Not Saturday
        return False

    day = selected_date.day
    week_number = (day - 1) // 7 + 1
    return week_number in [2, 4]


def mark_attendance(request):
    students = Student.objects.all()
    error = None

    selected_date_str = request.POST.get('attendance_date')

    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
    else:
        selected_date = date.today()

    # ❌ SUNDAY CHECK
    if selected_date.weekday() == 6:
        error = "Attendance cannot be marked on Sundays."

    # ❌ 2nd & 4th SATURDAY CHECK
    elif is_second_or_fourth_saturday(selected_date):
        error = "Attendance cannot be marked on 2nd and 4th Saturdays."

    # ✅ ALLOWED DAYS
    if request.method == 'POST' and not error:
        for student in students:
            status = request.POST.get(str(student.id))

            Attendance.objects.update_or_create(
                student=student,
                date=selected_date,
                defaults={'status': status}
            )

        return redirect('dashboard')

    return render(request, 'mark_attendance.html', {
        'students': students,
        'selected_date': selected_date,
        'error': error
    })


@login_required
def attendance_report(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')

    report = []
    for student in Student.objects.all():
        total = Attendance.objects.filter(student=student).count()
        present = Attendance.objects.filter(student=student, status='Present').count()
        percentage = (present / total * 100) if total else 0

        report.append({
            'student': student,
            'total': total,
            'present': present,
            'percentage': round(percentage, 2)
        })

    return render(request, 'attendance_report.html', {'report': report})


@login_required
def student_dashboard(request):
    student = Student.objects.filter(roll_number=request.user.username).first()
    total = Attendance.objects.filter(student=student).count()
    present = Attendance.objects.filter(student=student, status='Present').count()
    percentage = (present / total * 100) if total else 0

    return render(request, 'student_dashboard.html', {
        'student': student,
        'percentage': round(percentage, 2)
    })
from django.shortcuts import render
from .models import Student, Attendance

def student_attendance(request):
    result = None
    error = None

    if request.method == "POST":
        roll = request.POST.get("roll_number")

        student = Student.objects.filter(roll_number=roll).first()

        if not student:
            error = "Invalid Roll Number"
        else:
            total = Attendance.objects.filter(student=student).count()
            present = Attendance.objects.filter(
                student=student, status='Present'
            ).count()

            percentage = (present / total * 100) if total > 0 else 0

            result = {
                'student': student,
                'total': total,
                'present': present,
                'percentage': round(percentage, 2)
            }

    return render(request, 'student_attendance.html', {
        'result': result,
        'error': error
    })

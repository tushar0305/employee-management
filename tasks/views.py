from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TaskForm
from .models import Student, Task

def home(request):
    students = Student.objects.all()
    tasks = Task.objects.all()
    context = {'students': students, 'tasks': tasks}
    return render(request, 'index.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'delete_student.html', {'student': student})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    students = Student.objects.all()
    if request.method == 'POST':
        selected_students = request.POST.getlist('students')
        for student_id in selected_students:
            student = Student.objects.get(id=student_id)
            if student not in task.students.all():
                task.students.add(student)
        for student in task.students.all():
            if str(student.id) not in selected_students:
                task.students.remove(student)
        # Save the task instance after adding/removing assigned students
        task.save()
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_detail.html', {'form': form, 'task': task, 'students': students})

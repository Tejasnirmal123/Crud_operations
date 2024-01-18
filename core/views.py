from django.shortcuts import redirect, render
from .models import Student
from .forms import AddStudentForm

# Create your views here.
def Home(request):
    stu_data = Student.objects.all()
    return render(request, 'core/home.html', {'studata':stu_data})

def Add_Student(request):
    fm = AddStudentForm()
    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    return render(request, 'core/add_student.html', {'form':fm})

def Delete_Student(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')
    

    

def editStudent(request,pk):
    stu = Student.objects.get(id=pk)
    fm = AddStudentForm(instance=stu)
        
    if request.method == 'POST':
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    return render(request, 'core/edit_student.html', {'form':fm})    





    





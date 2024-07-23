from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm

def register_student(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Student registered successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

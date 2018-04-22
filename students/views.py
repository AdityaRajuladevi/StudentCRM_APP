from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from students.forms import StudentForm
from .models import Student
from contacts.models import Contact

# Create your views here.
@login_required()
def home(request):
    return render(request, "students/index.html")



class StudentList(ListView):
    model = Student
    paginate_by = 12
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        try:
            a = self.request.GET.get('student',)
        except KeyError:
            a = None
        if a:
            student_list = Student.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            student_list = Student.objects.filter(owner=self.request.user)
        return student_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentList, self).dispatch(*args, **kwargs)

@login_required()
def student_detail(request, uuid):
    student = Student.objects.get(uuid=uuid)
    if student.owner != request.user:
            return HttpResponseForbidden()
    #print(student)
    contacts = Contact.objects.filter(student=student)
    variables = {
        'student': student,
        'contacts': contacts,
    }
    return render(request, 'students/student_detail.html', variables)

@login_required()
def student_cru(request, uuid=None):

    if uuid:
        student = get_object_or_404(Student, uuid=uuid)
        if student.owner != request.user:
            return HttpResponseForbidden()
    else:
        student = Student(owner=request.user)

    if request.POST:
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.owner = request.user
            student.save()
            redirect_url = reverse(
                'student_detail',
                args=(student.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = StudentForm(instance=student)

    variables = {
        'form': form,
        'student': student
    }

    if request.is_ajax():
        template = 'students/student_item_form.html'
    else:
        template = 'students/student_cru.html'

    return render(request, template, variables)
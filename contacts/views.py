from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.http import Http404
from django.views.generic.edit import DeleteView

from .models import Contact
from .forms import ContactForm
from students.models import Student


@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request,
                'contacts/contact_detail.html',
                {'contact': contact}
    )

@login_required()
def contact_cru(request, uuid=None, student=None):

    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        if contact.owner != request.user:
            return HttpResponseForbidden()
    else:
        contact = Contact(owner=request.user)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # make sure the user owns the student
            student = form.cleaned_data['student']
            if student.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # return the user to the student detail view
            if request.is_ajax():
                return render(request,
                              'contacts/contact_item_view.html',
                              {'student':student, 'contact':contact}
                )
            else:
                reverse_url = reverse(
                      'student_detail',
                    args=(student.uuid,)
                )
                return HttpResponseRedirect(reverse_url)

        else:
            # if the form isn't valid, still fetch the student so it can be passed to the template
            student = form.cleaned_data['student']
    else:
        form = ContactForm(instance=contact)

    # this is used to fetch the student if it exists as a URL parameter
    if request.GET.get('student', ''):
        student = Student.objects.get(id=request.GET.get('student', ''))

    variables = {
        'form': form,
        'contact': contact,
        'student': student
    }

    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
        template = 'contacts/contact_cru.html'

    return render(request, template, variables)

class ContactMixin(object):
    model = Contact

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Contact'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactMixin, self).dispatch(*args, **kwargs)

class ContactDelete(ContactMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(ContactDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
            student = Student.objects.get(id=obj.student.id)
        self.student = student
        return obj

    def get_success_url(self):
        return reverse(
            'student_detail',
            args=(self.student.uuid,)
        )
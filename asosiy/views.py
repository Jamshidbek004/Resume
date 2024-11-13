from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ResumeForm, TajribaForm, MalakaForm, WebsiteForm, ContactForm
from .models import Resume, Tajriba, Malaka, Website
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def asosiy(request):
    users = request.user  # Joriy foydalanuvchi
    # Foydalanuvchiga tegishli ma'lumotlarni olish
    resumes = Resume.objects.filter(user=users)
    tajribalar = Tajriba.objects.filter(user=users)
    malakalar = Malaka.objects.filter(user=users)
    saytlar = Website.objects.filter(user=users)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Xabaringiz yuborildi!")
            return redirect('asosiy')  # Redirect to the contact page after submission
    else:
        form = ContactForm()

    context = {
        'resumes': resumes,
        'tajribalar': tajribalar,
        'malakalar': malakalar,
        'saytlar': saytlar,
        'form': form
    }

    return render(request, 'resume.html', context=context)

@login_required(login_url='login')
def malumot(request):
    # Barcha ma'lumotlarni olish
    users = request.user  # Joriy foydalanuvchi
    # Foydalanuvchiga tegishli ma'lumotlarni olish
    resumes = Resume.objects.filter(user=users)
    tajribalar = Tajriba.objects.filter(user=users)
    malakalar = Malaka.objects.filter(user=users)
    saytlar = Website.objects.filter(user=users)
    context = {
        'resumes': resumes,
        'tajribalar': tajribalar,
        'malakalar': malakalar,
        'saytlar': saytlar,
    }
    return render(request, 'malumot.html', context)


@login_required(login_url='login')
def generate_qr_code(request):
    # Foydalanuvchiga mos asosiy sahifa URL manzilini olish
    user_url = request.build_absolute_uri('/') + f"user/{request.user.username}/"

    # QR kod yaratish
    qr = qrcode.make(user_url)
    qr_image = BytesIO()
    qr.save(qr_image, "PNG")
    qr_image.seek(0)

    # QR kodni ko'rsatish
    return HttpResponse(qr_image, content_type="image/png")

@login_required
def add_website(request):
    if request.method == 'POST':
        form3 = WebsiteForm(request.POST)
        if form3.is_valid():
            website = form3.save(commit=False)
            website.user = request.user
            website.save()
            return redirect('add_website')  # Saytlar ro‘yxati sahifasiga qaytarish
    else:
        form3 = WebsiteForm()
    return render(request, 'add_website.html', {'form3': form3})
@login_required(login_url='login')
def add_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)  # Formdan obyekt yaratib olish
            resume.user = request.user  # Joriy foydalanuvchini user maydoniga o‘rnatish
            resume.save()  # Resume obyektini saqlash
            messages.success(request, 'Rezume muvaffaqiyatli saqlandi!')
            return redirect('add_resume')
    else:
        form = ResumeForm()
    return render(request, 'addresume.html', {'form': form})
@login_required
def add_tajriba(request):
    if request.method == 'POST':
        form1 = TajribaForm(request.POST)
        if form1.is_valid():
            tajriba = form1.save(commit=False)  # Formdan obyekt yaratib olish
            tajriba.user = request.user  # Joriy foydalanuvchini user maydoniga o‘rnatish
            tajriba.save()  # Resume obyektini saqlash
            messages.success(request, 'Tajriba muvaffaqiyatli saqlandi!')
            return redirect('add_tajriba')
    else:
        form1 = TajribaForm()
    return render(request, 'addtajriba.html', {'form1': form1})
@login_required
def add_malaka(request):
    if request.method == 'POST':
        form2 = MalakaForm(request.POST)
        if form2.is_valid():
            malaka = form2.save(commit=False)  # Formdan obyekt yaratib olish
            malaka.user = request.user  # Joriy foydalanuvchini user maydoniga o‘rnatish
            malaka.save()
            messages.success(request, 'Malaka muvaffaqiyatli saqlandi!')
            return redirect('add_malaka')
    else:
        form2 = MalakaForm()
    return render(request, 'malaka.html', {'form2': form2})

class ResumeEditView(UpdateView):
    model = Resume
    fields = ['kim', 'ozi_haqida']
    template_name = 'resume_edit.html'
    success_url = reverse_lazy('malumot')  # Tahrirlagandan keyin qaysi sahifaga o'tishi

class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'resume_confirm_delete.html'
    success_url = reverse_lazy('malumot')  # O'chirgandan keyin qaysi sahifaga o'tishi

# Tajriba uchun tahrirlash va o'chirish
class TajribaEditView(UpdateView):
    model = Tajriba
    fields = ['kompaniya', 'yil', 'kim']
    template_name = 'tajriba_edit.html'
    success_url = reverse_lazy('malumot')

class TajribaDeleteView(DeleteView):
    model = Tajriba
    template_name = 'tajriba_confirm_delete.html'
    success_url = reverse_lazy('malumot')

# Malaka uchun tahrirlash va o'chirish
class MalakaEditView(UpdateView):
    model = Malaka
    fields = ['nomi', 'daraja']
    template_name = 'malaka_edit.html'
    success_url = reverse_lazy('malumot')

class MalakaDeleteView(DeleteView):
    model = Malaka
    template_name = 'malaka_confirm_delete.html'
    success_url = reverse_lazy('malumot')


class SaytEditView(UpdateView):
    model = Website
    fields = ['name', 'link1', 'link2']
    template_name = 'sayt_edit.html'
    success_url = reverse_lazy('malumot')


class SaytDeleteView(DeleteView):
    model = Website
    template_name = 'sayt_confirm_delete.html'
    success_url = reverse_lazy('malumot')



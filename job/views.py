from django.shortcuts import render, redirect
from .models import Job, Apply, Category, JOB_TYPE
from django.core.paginator import Paginator
from .form import ApplyForm


def job_list(request):
    job_list= Job.objects.all() 

    # Get filter parameters from request
    search = request.GET.get('search')
    location = request.GET.get('location')
    experience = request.GET.get('experience')
    job_type = request.GET.get('job_type')
    category = request.GET.get('category')

    # Apply filters
    if search:
        job_list = job_list.filter(title__icontains=search)
    if location:
        job_list = job_list.filter(location__icontains=location)
    if experience:
        job_list = job_list.filter(experience=experience)
    if job_type:
        job_list = job_list.filter(job_type=job_type)
    if category:
        job_list = job_list.filter(category__id=category)

    paginator = Paginator(job_list, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Get distinct values for filters from database
    locations = Job.objects.values_list('location', flat=True).distinct()
    experiences = Job.objects.values_list('experience', flat=True).distinct()
    job_types = Job.objects.values_list('job_type', flat=True).distinct()
    categories = Category.objects.all() 
    
    context= {'jobs': page_obj, 'num':job_list, 'locations': locations, 'experiences': experiences, 'job_types': job_types, 'categories': categories}
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail= Job.objects.get(slug= slug)


    if request.method=='POST':
        name= request.POST.get("name")
        email= request.POST.get("email")
        webiste= request.POST.get("webiste")
        cv= request.POST.get("cv")
        cover_letter= request.POST.get("cover_letter")
        job = job_detail

        data= Apply(name=name, email=email, webiste=webiste, cv=cv, cover_letter=cover_letter, job=job)
        data.save()

    else:
        form = ApplyForm()
    context= {'job': job_detail}
    return render(request, 'job/job_detail.html', context)


def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        job_type = request.POST['job_type']
        location = request.POST['location']
        salary = request.POST['salary']
        experience = request.POST['experience']
        vacancy = request.POST['vacancy']
        category_id = request.POST['category']
        new_category_name = request.POST.get('new_category', '').strip()
        description = request.POST['description']
        image = request.FILES['image']

        # Handle new category
        if new_category_name:
            # Check if the category already exists
            category, created = Category.objects.get_or_create(name=new_category_name)
        else:
            # Use the existing category
            category = Category.objects.get(id=category_id)

        job = Job(
            title=title,
            job_type=job_type,
            location=location,
            salary=salary,
            experience=experience,
            vacancy=vacancy,
            category=category,
            description=description,
            image=image,
        )
        job.save()

        return redirect('jobs:job_list')  # Redirect to the job list page or wherever you want

    categories = Category.objects.all()
    return render(request, 'job/post_job.html', {'categories': categories, 'JOB_TYPE': JOB_TYPE})
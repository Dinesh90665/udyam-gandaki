
from .models import Training
from .models import Job
from datetime import datetime
trainings = [
    {"title": "Plumbing Level-1", "provider": "CTEVT", "duration": "3 months", "location": "Pokhara", "description": "Basic plumbing skills for households"},
    {"title": "Electrical Basics", "provider": "CTEVT", "duration": "2 months", "location": "Pokhara", "description": "Learn wiring, safety, and repair"},
    {"title": "Carpentry Level-1", "provider": "Local NGO", "duration": "3 months", "location": "Syangja", "description": "Furniture building and woodwork"},
    {"title": "Welding & Fabrication", "provider": "Private Co", "duration": "4 months", "location": "Kaski", "description": "Basic welding techniques"},
    {"title": "IT & Digital Literacy", "provider": "CTEVT", "duration": "1 month", "location": "Pokhara", "description": "Computers, MS Office, internet"},
]
def insert_trainings():
    for r in trainings:
        Training.objects.update_or_create(
            title=r['title'],  
            defaults={
                'provider': r['provider'],
                'duration': r['duration'],
                'location': r['location'],
                'description': r['description'],
            }
        )


from .models import Job
from django.contrib.auth.models import User

jobs = [
    {
        "title": "Software Engineer",
        "description": "Develop and maintain web applications using Python and Django.",
        "location": "Kathmandu",
        "pay_rate": "₹60,000/month",
        "employer": "dinesh"
    },
    {
        "title": "Data Entry Clerk",
        "description": "Input data into spreadsheets and maintain records accurately.",
        "location": "Pokhara",
        "pay_rate": "₹15,000/month",
        "employer": "john"
    },
    {
        "title": "Graphic Designer",
        "description": "Create visual concepts and design marketing materials.",
        "location": "Lalitpur",
        "pay_rate": "₹25,000/month",
        "employer": "rita"
    },
    {
        "title": "Digital Marketing Intern",
        "description": "Assist in social media campaigns and SEO optimization.",
        "location": "Bhaktapur",
        "pay_rate": "₹12,000/month",
        "employer": "sita"
    },
    {
        "title": "Electrician",
        "description": "Install and repair electrical wiring, fixtures, and equipment.",
        "location": "Chitwan",
        "pay_rate": "₹20,000/month",
        "employer": "ram"
    },
]

def insert_jobs():
    for j in jobs:
        # Get the User object for the employer
        try:
            employer_user = User.objects.get(username=j['employer'])
        except User.DoesNotExist:
            print(f"User {j['employer']} does not exist. Skipping job {j['title']}.")
            continue

        Job.objects.update_or_create(
            title=j['title'],
            defaults={
                'employer': employer_user,
                'description': j['description'],
                'location': j['location'],
                'pay_rate': j['pay_rate'],
            }
        )

# Usage:
# python manage.py shell
# >>> from core.insert_jobs import insert_jobs
# >>> insert_jobs()

from django.shortcuts import render
from .models import Student
from faker import Faker
import random
from .thread import CreateStudentThead, SaveCamPic

fake = Faker()


def home(request):
    count = 100

    CreateStudentThead(count).start()
    # for i in range(count):
    #     print(i)
    #     Student.objects.create(
    #         student_name = fake.name(),
    #         student_email = fake.email(),
    #         address = fake.address(),
    #         age = random.randint(20, 30)
    #     )

    # Saving Pic from Cam using threading and opencv 
    SaveCamPic().start()

    return render(request, "base.html")
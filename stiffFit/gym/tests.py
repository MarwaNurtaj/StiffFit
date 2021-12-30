from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from gym.models import *
#from stiffFit.gym.views import trainee

# Create your tests here.


class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Banners.objects.create( alt_text='bob')
        Trainer.objects.create( trainer='bob' , category='Yega Trainer' , email='bob@gmail.com' , phone='0711956465')
        Trainee.objects.create(trainee='bob' , age='20', email='bob@gmail.com')
        Package.objects.create(package='light_package' , price='10' , type='Gym')
        Page.objects.create(title='yoga', detail='yoga is good')
        Enquiry.objects.create(full_name='bob builder', email='bob@gmail.com',detail='how to exercise')
        Faq.objects.create(quest='DO I NEED TO WORK OUT EVERY DAY?',ans='yes')
    

    def test_Trainer_name(self):
        user = Trainer.objects.create(trainer='bob' , category='Yoga Trainer' , email='bob@gmail.com' , phone='0711956465')
        object_name = f'{user.trainer}'
        self.assertEqual('bob', object_name, "Testing name")


    def test_Trainer_email(self):
        user = Trainer.objects.create(trainer='bob' , category='Yoga Trainer' , email='bob@gmail.com' , phone='0711956465')
        object_name = f'{user.email}'
        self.assertEqual('bob@gmail.com', object_name, "Testing failed")    

    def test_trainee_name(self):
        user=Trainee.objects.create(trainee='bob' , age='20', email='bob@gmail.com')
        object_name = f'{user.trainee}'
        self.assertEqual('bob', object_name, "Testing failed")

    def test_package_name(self):
        user=Package.objects.get(id=1)
        field_label = user._meta.get_field('package').verbose_name
        self.assertEqual(field_label, 'package', "Testing package in user")

    def test_page_title(self):
        user = Page.objects.get(id=1)  
        field_label = user._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title', "Testing title in Page")

    def test_Faq_ans(self):
        user=Faq.objects.create(quest='DO I NEED TO WORK OUT EVERY DAY?',ans='yes')
        object_name = f'{user.ans}'
        self.assertEqual('yes', object_name, "Testing failed")


    def test_faq_ques(self):
        user=Faq.objects.get(id=1)
        field_label = user._meta.get_field('quest').verbose_name
        self.assertEqual(field_label, 'quest', "Testing package in user")

    def test_enquire_email(self):
        user=Enquiry.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email', "Testing package in user")

    def test_Enquiry_email(self):
        user=Enquiry.objects.create(full_name='bob builder', email='bob@gmail.com',detail='how to exercise')
        object_name = f'{user.full_name}'
        self.assertEqual('bob builder', object_name, "Testing failed")


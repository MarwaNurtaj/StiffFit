from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from gym.models import *
#from stiffFit.gym.views import trainee

# Create your tests here.


class TestClass(TestCase):
 #models unit test
    @classmethod
    def setUpTestData(cls):
        Banners.objects.create( alt_text='bob')
        Trainer.objects.create( trainer='bob' , category='Yega Trainer' , email='bob@gmail.com' , phone='0711956465')
        
        Package.objects.create(package='light_package' , price='10' , type='Gym')
        Page.objects.create(title='yoga', detail='yoga is good')
        Enquiry.objects.create(full_name='bob builder', email='bob@gmail.com',detail='how to exercise')
        Faq.objects.create(quest='DO I NEED TO WORK OUT EVERY DAY?',ans='yes')
        Page.objects.create(title='yoga' , detail='yoga is healthy')


    def test_Trainer_email(self):
        user = Trainer.objects.create(trainer='bob' , category='Yoga Trainer' , email='bob@gmail.com' , phone='0711956465')
        object_name = f'{user.email}'
        self.assertEqual('bob@gmail.com', object_name, "Testing failed")    

    def test_page_name(self):
        user=Page.objects.get(id=1)
        field_label = user._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title', "Testing page in user")

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

    #url unit test

    def test_notifs_url_name(self):
        response = self.client.get('/notifs')
        self.assertEqual(response.status_code, 200)
    
    def test_trainer_url_name(self):
        response = self.client.get('/trainer/')
        self.assertEqual(response.status_code, 200)
    
    def test_faq_url_name(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
    
    def test_token_url_name(self):
        response = self.client.get('/token/')
        self.assertEqual(response.status_code, 200)

    def test_gallery_url_name(self):
        response = self.client.get('/gallery')
        self.assertEqual(response.status_code, 200)
    
    def test_pricing_url_name(self):
        response = self.client.get('/pricing')
        self.assertEqual(response.status_code, 200)

    def test_trainerlogin_url_name(self):
        response = self.client.get('/trainerlogin')
        self.assertEqual(response.status_code, 200)

    def test_message_url_name(self):
        response = self.client.get('/messages')
        self.assertEqual(response.status_code, 200) 

    def test_trainerDashboard_name(self):
        response = self.client.get('/trainer_dashboard')
        self.assertEqual(response.status_code, 200)

    def test_trainer_dashboard_url_name(self):
        response = self.client.get('/trainer_dashboard')
        self.assertEqual(response.status_code, 200)     
     # just for testing test class

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
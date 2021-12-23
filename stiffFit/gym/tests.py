from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from gym.models import *
#from stiffFit.gym.views import trainee

# Create your tests here.


class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
      #  Banners.objects.create( alt_text='bob')
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

 #  UserModel.objects.create(name='Alice', email='alice@gmail.com')
       # UserContact.objects.create(messengerName='Alice', messengerEmail='alice@gmail.com', message='Test Contact')
      #  UserFeedback.objects.create( messengerName='Alice', messengerEmail='alice@gmail.com', message='Test Feedback')
      #  PostModel.objects.create(title='Test Title', description='Test Description', location='Test Location')

 #   def test_Banner_alt_text(self):
  #      user = Banners.objects.get(id=1)
   #     field_label = user._meta.get_field('alt_text').verbose_name
        # print("Method: testing name field")
    #    self.assertEqual(field_label, 'alt_text', "Testing name in user")
  #  def test_userobject_name_email(self):
   #     user = UserModel.objects.create(name='Bob', email='bob@gmail.com')
    #    object_name = f'{user.name}'
     #   object_email = f'{user.email}'
      #  # print("Method: Checking/Matching name and email")
       # self.assertEqual('Bob', object_name, "Testing Name")
        #self.assertEqual('bob@gmail.com', object_email, "Testing Email")

  #  def test_contact_user_name(self):
   #     user = UserContact.objects.get(id=1)
    #    name = user._meta.get_field('messengerName').verbose_name
     #   # print("Method: testing name field")
      #  self.assertEqual(name, 'messengerName', "Testing name in user contact")

#    def test_user_contactobject(self):
 #       contact = UserContact.objects.create(
  #          messengerName='Charlie', messengerEmail='charlie@gmail.com', message='Testing Contact')
   #     object_name = f'{contact.messengerName}'
    #    object_email = f'{contact.messengerEmail}'
     #   object_message = f'{contact.message}'
        # print("Method: Checking/Matching name, email and message")
#        self.assertEqual('Charlie', object_name, "Testing Name")
 #       self.assertEqual('charlie@gmail.com', object_email, "Testing Email")
  #      self.assertEqual('Testing Contact', object_message, "Testing Contact")

 #   def test_feedback_user_name(self):
  #      user = UserFeedback.objects.get(id=1)
   ##     name = user._meta.get_field('messengerName').verbose_name
     #   # print("Method: testing name field")
      #  self.assertEqual(name, 'messengerName', "Testing name in user feedback")

#    def test_user_feedbackobject(self):
 #       feedback = UserFeedback.objects.create(
  #          messengerName='Charlie', messengerEmail='charlie@gmail.com', message='Testing Feedback')
   #     object_name = f'{feedback.messengerName}'
    #    object_email = f'{feedback.messengerEmail}'
     #   object_message = f'{feedback.message}'
        # print("Method: Checking/Matching name, email and message")
  #      self.assertEqual('Charlie', object_name, "Testing Name")
   #     self.assertEqual('charlie@gmail.com', object_email, "Testing Email")
    #    self.assertEqual('Testing Feedback', object_message, "Testing Feedback")

#    def test_user_post_title(self):
 #       post = PostModel.objects.get(id=1)
  #      title = post._meta.get_field('title').verbose_name
   ##    self.assertEqual(title, 'title', "Testing title in user posts")

 #   def test_user_postobject(self):
  #      post = PostModel.objects.create(
   #         title='Test Title', description='Test Description', location='Test Location')
    #    object_title = f'{post.title}'
     #   object_description = f'{post.description}'
      #  object_location = f'{post.location}'
        # print("Method: Checking/Matching title, description and location")
    #    self.assertEqual('Test Title', object_title, "Testing Title")
     #   self.assertEqual('Test Description', object_description, "Testing Description")
      #  self.assertEqual('Test Location', object_location, "Testing Location")

    # def test_createRestaurant(self):
    #     res1 = Restaurant.objects.create(
    #         Rid=9, Rname='Burger Lab', Aname='Gulshan')
    #     res = Restaurant.objects.get(Rid=9)
    #     object1 = res.Rname
    #     print("Method: Creating object of Restaurant Class")
    #     self.assertEqual('Burger Lab', object1, "Testing Restaurant Name")
    #     self.assertNotEqual('Gulshan', object1, "Testing False Area Name")

    # def test_deleteRestaurant(self):
    #     res1 = Restaurant.objects.create(
    #         Rid=10, Rname='Burger Lab', Aname='Gulshan')
    #     res = Restaurant.objects.get(Rid=10)
    #     object1 = res.Rname
    #     print("Method: Deleting object of Restaurant Class")
    #     self.assertEqual('Burger Lab', object1, "Testing Restaurant Name")
    #     views.deleteRes1(10)
    #     self.assertNotEqual('Burger Lab', res1, "Deleting Restaurant Name")

    # def test_DublicateRestaurant(self):
    #     res1 = Restaurant.objects.create(Rid=10, Rname='KFC', Aname='Gulshan')
    #     object1 = res1.Rname
    #     print("Method: Checking Dublicate value")
    #     res2 = Restaurant.objects.create(Rid=11, Rname='KFC', Aname='Gulshan2')
    #     self.assertNotEqual('KFC', object1, "Dublicate Restaurant Name")

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)
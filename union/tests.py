from django.test import TestCase
from .models import StudentUnion,Business
from django.contrib.auth.models import User
# Create your tests here.
class StudentUnionTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_union= StudentUnion(union_admin=self.new_user,union_name='Wazazi',union_location='Chuom')
        self.new_union.save()



    # Tear Down method
    def tearDown(self):
        StudentUnion.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_union,StudentUnion))    

    # Testing Save Method
    def test_create_StudentUnion_method(self):
        self.new_union1= StudentUnion(union_admin=self.new_user,union_name='Wazazi',union_location='Chuom')
        self.new_union1.create_studentunion()
        unions = StudentUnion.objects.all()
        self.assertTrue(len(unions) == 2)  



    # Testing delete method
    def test_delete_studentunion(self):
        StudentUnion.delete_studentunion(self.new_union.id)
        unions = StudentUnion.get_all_vs()
        self.assertTrue(len(unions) == 0)     

    # Testing get all StudentUnions Method
    def test_get_all_studentunions_method(self):
        unions = StudentUnion.get_all_studentunions()
        self.assertTrue(len(unions) == 1) 


    # Testing find StudentUnion Method
    def test_find_studentunion_method(self):
        union = StudentUnion.find_studentunion(self.new_union.id)
        self.assertEqual(union.id,self.new_union.id)   





class BusinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_union= StudentUnion(union_admin=self.new_user,union_name='Wazazi',union_location='Chuom')
        self.new_union.save()

        self.new_bs=Business(user=self.new_user,studentunion=self.new_union,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs.save()


    # Tear Down method
    def tearDown(self):
        Business.objects.all().delete()
        StudentUnion.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_bs,Business))    

    # Testing Save Method
    def test_create_business_method(self):
        self.new_bs1= Business(user=self.new_user,studentunion=self.new_union,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        bss = Business.objects.all()
        self.assertTrue(len(bss) == 2)  



    # Testing delete method
    def test_delete_business(self):
        self.new_bs.delete_business()
        bss = Business.objects.all()
        self.assertTrue(len(bss) == 0)     

    # Testing get all Business By Union Method
    def test_get_all_bs_by_union_method(self):
        self.new_union1= StudentUnion(union_admin=self.new_user,union_name='Wazazi',union_location='Chuom')
        self.new_union1.save()
        self.new_bs1= Business(user=self.new_user,studentunion=self.new_union1,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        bss = Business.get_all_bs_by_union(self.new_union1.id)
        self.assertTrue(len(bss) == 1) 


    # Testing find Business Method
    def test_find_business_method(self):
        bs = Business.find_business(self.new_bs.id)
        self.assertEqual(bs.id,self.new_bs.id)   

    # Testing search business by name method
    def test_search_project(self):
        self.new_union1= StudentUnion(union_admin=self.new_user,union_name='Wazazi',union_location='Chuom')
        self.new_union1.save()
        self.new_bs1= Business(user=self.new_user,studentunion=self.new_union1,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        self.new_bs2= Business(user=self.new_user,studentunion=self.new_union1,bs_name='Shoe repair',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs2.create_business()
        bss=Business.search_business('wat',self.new_union.id)
        bsss=Business.search_business('Sho',self.new_union.id)
        self.assertFalse(len(bsss) > 0)  
        self.assertTrue(len(bss) > 0) 







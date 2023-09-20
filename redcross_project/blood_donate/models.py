from django.db import models

# Create your models here.

class aboutus(models.Model):
    heading=models.CharField(max_length=100)
    subtitle1=models.CharField(max_length=2000)
    subtitle2=models.CharField(max_length=2000)
    content1=models.CharField(max_length=2000)
    content2=models.CharField(max_length=2000)
    content3=models.CharField(max_length=2000)
    content4=models.CharField(max_length=2000)
    content5=models.CharField(max_length=2000)
    image1=models.ImageField(upload_to="images/")
    image2=models.ImageField(upload_to="images/")

class Meta:
    db_table="aboutus"

class HomeNav_drop(models.Model):
    nav_name = models.CharField(max_length=200, db_index=True)
    nav_url=models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', related_name='subdrop', blank=True, null=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    
    def is_active(self, request_path):
        # Check if any child items are active
        if self.subdrop.filter(nav_url=request_path).exists():
            return True
        return False
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
       
        
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.nav_name

        
    
class appfooter(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    url=models.CharField(max_length=100)
    icon=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
class Meta:
       db_table="appfooter"


class appfooter1(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    url=models.CharField(max_length=100)
    icon=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
class Meta:
       db_table="appfooter1"

class appdown(models.Model):
    heading=models.CharField(max_length=100)
    app=models.ImageField(upload_to="media/")
    url=models.CharField(max_length=100,default="")
class meta:
    db_table="appdown"

class gettouch(models.Model):
    heading=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
class Meta:
    db_table="gettouch"

class socialicon(models.Model):
    icon1=models.ImageField(upload_to="media/")
    url1=models.CharField(max_length=100)
class Meta:
    db_table="socialicon"


    
class events(models.Model):
    content=models.CharField(max_length=2000)
    image=models.ImageField(upload_to="media/")
    heading=models.CharField(max_length=100)

class Meta:
    db_table="events"

class pre_registataion_QA_1(models.Model):
    question_1=models.CharField(max_length=100)
class Meta:
    db_table="pre_registataion_QA_1"

class pre_registataion_QA_2(models.Model):
    question_2=models.CharField(max_length=100)
class Meta:
    db_table="pre_registataion_QA_2"

class pre_registataion_QA_3(models.Model):
    question_3=models.CharField(max_length=100)
class Meta:
    db_table="pre_registataion_QA_3"

class pre_registataion_QA_4(models.Model):
    question_4=models.CharField(max_length=100)
class Meta:
    db_table="pre_registataion_QA_4"


class blood(models.Model):
    photo=models.ImageField(upload_to="images/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        db_table = 'blood_donate_blood'
    def __str__(self):
        return f"Blood Image {self.id}"
    


class Announcement(models.Model):
    content = models.TextField()
    name=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.content[:50]  
    




class basic_requirements(models.Model):
    id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=200)
    icon=models.ImageField(upload_to="media/")
    points=models.CharField(max_length=2000)
    points=models.CharField(max_length=350)
    point1=models.CharField(max_length=350)
    point2=models.CharField(max_length=350)
    point3=models.CharField(max_length=350)
    point4=models.CharField(max_length=350)
    point5=models.CharField(max_length=350)
    point6=models.CharField(max_length=350)
    point7=models.CharField(max_length=350)
    point8=models.CharField(max_length=350)      
    point9=models.CharField(max_length=350)
    images=models.ImageField(upload_to="media/")

class Meta:
    db_table="basic_requirements"



class additional_requirements(models.Model):
    image=models.ImageField(upload_to="images/")
    point2=models.CharField(max_length=1000)
    point3=models.CharField(max_length=1000)
    point4=models.CharField(max_length=1000)
    point5=models.CharField(max_length=1000)
    point6=models.CharField(max_length=1000)
    point7=models.CharField(max_length=1000)
    point8=models.CharField(max_length=1000)
    point9=models.CharField(max_length=1000)
    point1=models.CharField(max_length=1000)
    image1=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100)
class Meta:
    db_table='additional_requirements'

    
class patient_request(models.Model):
    patient_name=models.CharField(max_length=100)
    contact_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    mobilenumber=models.CharField(max_length=100)
    hospitalname=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    bloodgroup=models.CharField(max_length=100)
    bloodrequirements=models.CharField(max_length=100)
    bloodtypes=models.CharField(max_length=100)
class Meta:
    db_table="patient_request"


    
class Address(models.Model):
   country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
   state = models.ForeignKey('cities_light.Region',on_delete=models.SET_NULL, null=True, blank=True)
   district = models.ForeignKey('cities_light.SubRegion',on_delete=models.SET_NULL, null=True, blank=True)

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Donor(models.Model):
    

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    aadhar = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=258)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    otp = models.CharField(max_length=4)
    in_hidden=models.BooleanField(default=False)
    

    


    def __str__(self):
        return self.user.username
    
    def days_until_next_donation(self):
        today = timezone.now().date()
        last_donation = self.lastdonatedetails_set.order_by('-donation_date').first()
        
        if last_donation:
            next_donation_date = last_donation.donation_date + timezone.timedelta(days=90)  # Assuming a 90-day gap
            
            if next_donation_date <= today:
                return 0
            else:
                return (next_donation_date - today).days
        else:
            # No donation record found, return 0 or any other default value as needed
            return 0

    def is_eligible(self):
        today = timezone.now().date()
        last_donation = self.lastdonatedetails_set.order_by('-donation_date').first()

        if last_donation:
            next_donation_date = last_donation.donation_date + timezone.timedelta(days=90)  # Assuming a 90-day gap

            return next_donation_date <= today
        else:
            # No donation record found, return False or any other default value as needed
            return False
        
    def has_filled_form(self):
        """
        Check if a donor has filled out the form.
        A donor is considered to have filled out the form if they have related records in the lastdonatedetails model.
        """
        # Check if there are any related records in the lastdonatedetails model
        return self.lastdonatedetails_set.exists()
            
class bloodtype(models.Model):
    BId=models.CharField(max_length=10)
    Description=models.CharField(max_length=1000)
    point1=models.CharField(max_length=1000)
    point2=models.CharField(max_length=1000)
    point3=models.CharField(max_length=1000)
    point4=models.CharField(max_length=1000)
    point5=models.CharField(max_length=1000)
    point6=models.CharField(max_length=1000)
    Bloodtype=models.CharField(max_length=10)
    image=models.ImageField(upload_to="media/")

class Meta:
    db_table="bloodtype"

class blood_types(models.Model):
    heading=models.CharField(max_length=200)
    image=models.ImageField(upload_to="media/")
    content=models.CharField(max_length=2000)
    
class Meta:
    db_table='blood_types'


class donators(models.Model):
    
    image=models.ImageField(upload_to="media/")
    heading=models.CharField(max_length=100)
    content1=models.CharField(max_length=1000)
    content=models.CharField(max_length=2000)
   
class Meta:
    db_table="donators"


class Announcements(models.Model):
    Title=models.CharField(max_length=200)
    Content=models.CharField(max_length=700)
class Meta:
    db_table="Announcements"

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class video(models.Model):
    video_url=models.CharField(max_length=100)
class Meta:
    db_table="video"
class contactus(models.Model):
    name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField()
    enquirytype=models.CharField(max_length=1000,default='')
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=1000)

class Meta:
    db_table='contactus'


class historyblood(models.Model):
    heading=models.CharField(max_length=200)
    points=models.CharField(max_length=250)
    images=models.ImageField(upload_to="media/")
    point1=models.CharField(max_length=200)
    point2=models.CharField(max_length=250)
    point3=models.CharField(max_length=250)
    point4=models.CharField(max_length=250)
    point5=models.CharField(max_length=250)
    image=models.ImageField(upload_to="media/")
    subhead=models.CharField(max_length=200)
    cnt1=models.CharField(max_length=250)
    cnt2=models.CharField(max_length=250)
    cnt3=models.CharField(max_length=250)
    cnt4=models.CharField(max_length=250)
    cnt5=models.CharField(max_length=250)
    
   
class Meta:
    db_table='historyblood'

class donation_process(models.Model):
    heading=models.CharField(max_length=100)
    point1=models.CharField(max_length=300)
    point2=models.CharField(max_length=300)
    point3=models.CharField(max_length=300)
    point4=models.CharField(max_length=300)
    image=models.ImageField(upload_to="image/")

class Meta:
    db_table='donation_process'
from django.utils import timezone

class lastdonatedetails(models.Model):
    donor = models.ForeignKey(Donor , on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    patient_name=models.CharField(max_length=100 , null=True, blank=True)
    place=models.CharField(max_length=200)
    donation_date = models.DateField(default=timezone.now)
    uploade_image = models.ImageField(upload_to='media')

    
class Meta:
    db_table="lastdonatedetails"

class tips_donation(models.Model):
   # heading1=models.CharField(max_length=100)
   subHeading=models.CharField(max_length=100)
   point1=models.CharField(max_length=1000,default="")
   point2=models.CharField(max_length=1000,default="")
   point3=models.CharField(max_length=1000,default="")
class Meta:
   db_table="tips_donation"
   
class content(models.Model):
   img1=models.ImageField(upload_to="images/")
   Heading1 =models.CharField(max_length=1000)
   description=models.CharField(max_length=3000)
   text=models.CharField(max_length=3000,default="")
   point1=models.CharField(max_length=1000,default="")
   point2=models.CharField(max_length=1000,default="")
   point3=models.CharField(max_length=1000,default="")  
class Meta:
   db_table="content"
class contactus(models.Model):
    ENQUIRYTYPE_CHOICES = [
        ('Blood Donor', 'Blood Donor'),
        ('Blood Type', 'Blood Type'),
       
    ] 
      
    name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField()
    enquirytype=models.CharField(max_length=1000,default='Blood Donor',choices=ENQUIRYTYPE_CHOICES)
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=1000)

class Meta:
    db_table='contactus'
class Contactusadmin(models.Model):

    email=models.EmailField(max_length=50)
    contactno=models.BigIntegerField()
    website=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    map=models.CharField(max_length=1000)

class Meta:
    db_table="Contactusadmin"
class contact(models.Model):
    heading=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
class Meta:
    db_table="contact"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aread= models.CharField(max_length=10)
    awrite=models.CharField(max_length=10)
    aupdate=models.CharField(max_length=10)
    aremove=models.CharField(max_length=10)
    aconta=models.CharField(max_length=10)
    mobileno=models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.user.username
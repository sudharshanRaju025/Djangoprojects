from django.db import models
from django.utils import timezone

# Create your models here.

class LeadModule(models.Model):
    id=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    cc=models.BigIntegerField()
    contact_no=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    fee_coated=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    date=models.DateField(default=timezone.now)

    LEAD_STATUS_CHOICES=[
        ("None","None"),
        ("Not contacted","Not contacted"),
        ("Attempted","Attempted"),
        ("warm lead","warm lead"),
        ("opportunity","opportunity"),
        ("attendedemo","attendedemo"),
        ("visited","visited"),
        ("registered","registered"),
        ("coldlead","coldlead"),
    ]

    LEAD_SOURCE_CHOICES = [
        ('None', 'None'),
        ('WalkIn', 'WalkIn'),
        ('StudentReferral', 'StudentReferral'),
        ('Demo', 'Demo'),
        ('WebSite', 'WebSite'),
        ('WebsiteChat', 'WebsiteChat'),
        ('InboundCall', 'InboundCall'),
        ('GoogleAdWords', 'GoogleAdWords'),
        ('FacebookAds', 'FacebookAds'),
        ('GoogleMyBusiness', 'GoogleMyBusiness'),
        ('WhatsAppDigitalLync', 'WhatsAppDigitalLync'),
    ]

    BATCH_TIMING_CHOICES = [
        ('7AM_8AM', '7AM_8AM'),
        ('8AM_9AM', '8AM_9AM'),
        ('9AM_10AM', '9AM_10AM'),
        ('10AM_11AM', '10AM_11AM'),
        ('11AM_12PM', '11AM_12PM'),
        ('12PM_1PM', '12PM_1PM'),
        ('1PM_2PM', '1PM_2PM'),
        ('2PM_3PM', '2PM_3PM'),
        ('3PM_4PM', '3PM_4PM'),
        ('4PM_5PM', '4PM_5PM'),
        ('5PM_6PM', '5PM_6PM'),
        ('6PM_7PM', '6PM_7PM'),
        ('7PM_8PM', '7PM_8PM'),
        ('8PM_9PM', '8PM_9PM'),
    ]

    TECH_STACK_CHOICES = [
        ('CloudOps', 'CloudOps'),
        ('Salesforce', 'Salesforce'),
        ('FullStack', 'FullStack'),
        ('DataStack', 'DataStack'),
        ('ServiceNow', 'ServiceNow'),
        ('BusinessStack', 'BusinessStack'),
        ('CareerCounselling', 'CareerCounselling'),
    ]

    CLASS_MODE_CHOICES = [
        ('HYDClassRoom', 'HYDClassRoom'),
        ('BLRClassRoom', 'BLRClassRoom'),
        ('IndiaOnline', 'IndiaOnline'),
        ('InternationalOnline', 'InternationalOnline'),
    ]

    COURSES_CHOICES = [
        ('Angulaar', 'Angulaar'),
        ('AWS', 'AWS'),
        ('AWSWithDevOps', 'AWSWithDevOps'),
        ('Azure', 'Azure'),
        ('AzureDevOps', 'AzureDevOps'),
        ('BusinessAnlayst', 'BusinessAnlayst'),
        ('CloudOpsMasters', 'CloudOpsMasters'),
        ('DevOps', 'DevOps'),
        ('FrontEndAngular', 'FrontEndAngular'),
        ('FrontEndReact', 'FrontEndReact'),
        ('FullStackJAVA', 'FullStackJAVA'),
        ('FullStackMEAN', 'FullStackMEAN'),
        ('FullStackMERN', 'FullStackMERN'),
        ('FullstackPython', 'FullstackPython'),
        ('FullStackReactJAVA', 'FullStackReactJAVA'),
        ('Java', 'Java'),
        ('NeedCounselling', 'NeedCounselling'),
        ('Others', 'Others'),
        ('PowerBI', 'PowerBI'),
        ('Python', 'Python'),
        ('React', 'React'),
        ('SalesForceAdmin', 'SalesForceAdmin'),
        ('SalesforceDeveloper', 'SalesforceDeveloper'),
        ('ServiceNow', 'ServiceNow'),
        ('AzureDataEngineer', 'AzureDataEngineer'),
        ('Tableau', 'Tableau'),
        ('Testing', 'Testing'),
    ]


    lead_source=models.CharField(
        max_length=20,
        choices= LEAD_SOURCE_CHOICES ,
        default="None",
    )

    batch_timigs=models.CharField(
        max_length=10,
        choices=BATCH_TIMING_CHOICES,
        default="None",
    )

    class_mode=models.CharField(
        max_length=20,
        choices= CLASS_MODE_CHOICES,
        default="HYDclassrrom",
    )

    lead_status=models.CharField(
        max_length=20,
        choices= LEAD_STATUS_CHOICES,
        default="None",
    )

    courses=models.CharField(
        max_length=20,
        choices= COURSES_CHOICES,
        default="None",
    )

    tech_stack=models.CharField(
        max_length=20,
        choices=TECH_STACK_CHOICES ,
        default="None",
    )

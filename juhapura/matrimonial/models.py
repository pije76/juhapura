# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from countries_plus.models import Country
from juhapura.users.models import User


# Create your models here.
class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    city_state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'
        ordering = ['city_name']

    def __str__(self):
        return ' - '.join([self.city_name, self.city_state])


class Profile(models.Model):	
	
    gender_list = [('M','Male'), ('F','Female')]

    marital_status_list = [ (0, 'Never married'),
        (1, 'Divorcee'),
        (2, 'Seperated'),
        (3, 'Widow/Widower'),
        (4, 'Anulled')
        ]
    height_list = [(0,"Select Option"),
            ("1.37","1.37m (4' 6\")"),
            ("1.38","1.38m"),
            ("1.39","1.39m"),
            ("1.4","1.40m (4' 7\")"),
            ("1.41","1.41m"),
            ("1.42","1.42m (4' 8\")"),
            ("1.43","1.43m"),
            ("1.44","1.44m"),
            ("1.45","1.45m (4' 9\")"),
            ("1.46","1.46m"),
            ("1.47","1.47m (4' 10\")"),
            ("1.48","1.48m"),
            ("1.49","1.49m"),
            ("1.5","1.50m (4' 11\")"),
            ("1.51","1.51m"),
            ("1.52","1.52m (5' 0\")"),
            ("1.53","1.53m"),
            ("1.54","1.54m"),
            ("1.55","1.55m (5' 1\")"),
            ("1.56","1.56m"),
            ("1.57","1.57m (5' 2\")"),
            ("1.58","1.58m"),
            ("1.59","1.59m"),
            ("1.6","1.60m (5' 3\")"),
            ("1.61","1.61m"),
            ("1.62","1.62m"),
            ("1.63","1.63m (5' 4\")"),
            ("1.64","1.64m"),
            ("1.65","1.65m (5' 5\")"),
            ("1.66","1.66m"),
            ("1.67","1.67m"),
            ("1.68","1.68m (5' 6\")"),
            ("1.69","1.69m"),
            ("1.7","1.70m (5' 7\")"),
            ("1.71","1.71m"),
            ("1.72","1.72m"),
            ("1.73","1.73m (5' 8\")"),
            ("1.74","1.74m"),
            ("1.75","1.75m (5' 9\")"),
            ("1.76","1.76m"),
            ("1.77","1.77m"),
            ("1.78","1.78m (5' 10\")"),
            ("1.79","1.79m"),
            ("1.8","1.80m (5' 11\")"),
            ("1.81","1.81m"),
            ("1.82","1.82m"),
            ("1.83","1.83m (6' 0\")"),
            ("1.84","1.84m"),
            ("1.85","1.85m (6' 1\")"),
            ("1.86","1.86m"),
            ("1.87","1.87m"),
            ("1.88","1.88m (6' 2\")"),
            ("1.89","1.89m"),
            ("1.9","1.90m"),
            ("1.91","1.91m (6' 3\")"),
            ("1.92","1.92m"),
            ("1.93","1.93m (6' 4\")"),
            ("1.94","1.94m"),
            ("1.95","1.95m"),
            ("1.96","1.96m (6' 5\")"),
            ("1.97","1.97m"),
            ("1.98","1.98m (6' 6\")"),
            ("1.99","1.99m"),
            ("2","2.00m"),
            ("2.01","2.01m (6' 7\")"),
            ("2.02","2.02m"),
            ("2.03","2.03m (6' 8\")"),
            ("2.04","2.04m"),
            ("2.05","2.05m"),
            ("2.06","2.06m (6' 9\")"),
            ("2.07","2.07m"),
            ("2.08","2.08m (6' 10\")"),
            ("2.09","2.09m"),
            ("2.1","2.10m"),
            ("2.11","2.11m (6' 11\")"),
            ("2.12","2.12m"),
            ("2.13","2.13m (7' 0\")"),
            ("2.14","2.14m"),
            ("2.15","2.15m"),
            ("2.16","2.16m (7' 1\")"),
            ]

    reason_registration_list = [
        (1, 'I\'m registring to find myself a partner'),
        (2, 'I\'m registring to find my friend a partner'),
        (3, 'I\'m registring to find my son a partner'),
        (4, 'I\'m registring to find my daughter a partner'),
        (5, 'I\'m registring to find my brother a partner'),
        (6, 'I\'m registring to find my sister a partner')
        ]

    income_list = [
        (0,'Prefer not to say'),
        (1,'Under Rs 50,000'),
        (2,'Rs 50,000 - Rs 1,00,000'),
        (3,'Rs 1,00,000 - Rs 3,00,000'),
        (4,'Rs 3,00,000 - Rs 5,00,000'),
         (4,'Rs 5,00,000 - Rs 10,00,000'),
        (6,'Above Rs 10,00,000'),
        ]

    occupation_list = [
	    (0,'Select Occupation'),
	    (3,"Accountant"),
	    (4,"Acting Professional"),
	    (5,"Actor"),
	    (6,"Administration Professional"),
	    (7,"Advertising Professional"),
	    (100,"Advocate"),
	    (8,"Air Hostess"),
	    (9,"Architect"),
	    (10,"Artisan"),
	    (11,"Audiologist"),
	    (102,"Autocade Engineer"),
	    (12,"Banker"),
	    (13,"Beautician"),
	    (14,"Biologist / Botanist"),
	    (95,"Business"),
	    (15,"Business Person"),
	    (16,"Chartered Accountant"),
	    (17,"Civil Engineer"),
	    (18,"Clerical Official"),
	    (19,"Commercial Pilot"),
	    (20,"Company Secretary"),
	    (21,"Computer Professional"),
	    (22,"Consultant"),
	    (23,"Contractor"),
	    (24,"Cost Accountant"),
	    (25,"Creative Person"),
	    (26,"Customer Support Professional"),
	    (27,"Defense Employee"),
	    (28,"Dentist"),
	    (29,"Designer"),
	    (105,"Diploma Electronic &amp; comm. Engineering"),
	    (106,"Diploma Electronic &amp; comm. Engineering"),
	    (118,"Diploma in Hotel Management"),
	    (117,"Diploma in Hotel Managment"),
	    (30,"Doctor"),
	    (31,"Economist"),
	    (93,"Education officer."),
	    (121,"Educational Evelution Work"),
	    (94,"Electrical Engineer"),
	    (32,"Engineer"),
	    (33,"Engineer (Mechanical)"),
	    (34,"Engineer (Project)"),
	    (35,"Entertainment Professional"),
	    (36,"Event Manager"),
	    (37,"Executive"),
	    (38,"Factory worker"),
	    (39,"Farmer"),
	    (40,"Fashion Designer"),
	    (103,"Film Director"),
	    (41,"Finance Professional"),
	    (42,"Flight Attendant"),
	    (43,"Government Employee"),
	    (44,"Health Care Professional"),
	    (45,"Home Maker"),
	    (46,"Hotel &amp; Restaurant Professional"),
	    (98,"House Hold work"),
	    (47,"Human Resources Professional"),
	    (104,"Insurance Adviser"),
	    (48,"Interior Designer"),
	    (49,"Investment Professional"),
	    (50,"IT / Telecom Professional"),
	    (114,"Job"),
	    (97,"Job in Bank"),
	    (101,"Job In Call Centre."),
	    (119,"Job in Infrastructure Company"),
	    (109,"Job in Multi National Company"),
	    (96,"Job in Private Company"),
	    (99,"Job in Private Office"),
	    (51,"Journalist"),
	    (107,"Lab Technician"),
	    (52,"Lawyer"),
	    (53,"Lecturer"),
	    (54,"Legal Professional"),
	    (113,"Librerian"),
	    (55,"Manager"),
	    (56,"Marketing Professional"),
	    (57,"Media Professional"),
	    (58,"Medical Professional"),
	    (108,"Medical Representative"),
	    (59,"Medical Transcriptionist"),
	    (60,"Merchant Naval Officer"),
	    (2,"Non-mainstream professional"),
	    (1,"Not working"),
	    (61,"Nurse"),
	    (62,"Occupational Therapist"),
	    (63,"Optician"),
	    (64,"Pharmacist"),
	    (65,"Physician Assistant"),
	    (66,"Physicist"),
	    (67,"Physiotherapist"),
	    (68,"Pilot"),
	    (69,"Politician"),
	    (70,"Production professional"),
	    (71,"Professor"),
	    (72,"Psychologist"),
	    (73,"Public Relations Professional"),
	    (74,"Real Estate Professional"),
	    (120,"Relationship Manager"),
	    (75,"Research Scholar"),
	    (112,"Research Scientist"),
	    (77,"Retail Professional"),
	    (76,"Retired Person"),
	    (78,"Sales Professional"),
	    (79,"Scientist"),
	    (122,"Searching Job"),
	    (80,"Self-employed Person"),
	    (81,"Social Worker"),
	    (82,"Software Consultant"),
	    (111,"Software Engineer"),
	    (83,"Sportsman"),
	    (84,"Student"),
	    (85,"Teacher"),
	    (86,"Technician"),
	    (87,"Training Professional"),
	    (88,"Transportation Professional"),
	    (110,"Tuition Class"),
	    (115,"Typiest"),
	    (89,"Veterinary Doctor"),
	    (90,"Volunteer"),
	    (116,"Web Designer"),
	    (91,"Writer"),
	    (92,"Zoologist"),
	    (123,"Other")
	    ]

    qualification_list = [
        (0,"Select Qualification"),
        (1,"Alim / Alima"),
        (2,"B. Architect"),
        (3,"B.E  (Chemical)"),
        (4,"B.E  Bio Medical Instrumentation Engineer"),
        (5,"B.E ( Automobile Engineering )"),
        (6,"B.E ( Civil Engineer )"),
        (7,"B.E ( Computer Engineer )"),
        (8,"B.E ( Electrical )"),
        (9,"B.E ( Electronics &amp; Communication )"),
        (10,"B.E ( I.T )"),
        (11,"B.E ( Manufacturing )"),
        (12,"B.E ( Software Engineer )"),
        (13,"B.E (Electronics)"),
        (14,"B.E (Industrial)"),
        (15,"B.E (Instrumentation &amp; Control)"),
        (16,"B.E (Mechanical)"),
        (17,"B.E Metallurgy"),
        (18,"B.E Structural Engineer"),
        (19,"B.E Textile Engineer"),
        (20,"B.E.( Plastic )"),
        (21,"B.E.(Production)"),
        (22,"B.H.M.S"),
        (23,"B.P.Ed"),
        (24,"B.Tech"),
        (25,"Bachelor in Hotel Management"),
        (26,"Bachelor in Interior Designing"),
        (27,"Bachelor in Prosthetics and Orthotics"),
        (28,"Bachelor of an Airhostess"),
        (29,"Bachelor of Arts"),
        (30,"Bachelor of Business Administration"),
        (31,"Bachelor of Commerce"),
        (32,"Bachelor of Computer Applications"),
        (33,"Bachelor of Computer Science"),
        (34,"Bachelor of Design"),
        (35,"Bachelor of Education"),
        (36,"Bachelor of Engineering civil"),
        (37,"Bachelor of Home Science"),
        (38,"Bachelor of Management Science for Finance"),
        (39,"Bachelor of Medicine in Electro-Homoeopathy"),
        (40,"Bachelor of Nursing"),
        (41,"Bachelor of Occupational Therapy"),
        (42,"Bachelor of Optometrist"),
        (43,"Bachelor of Pharmacy"),
        (44,"Bachelor of Physiotherapy"),
        (45,"Bachelor of Science"),
        (46,"Bachelor of Veterinary Science and Animal Husbandry"),
        (47,"Bachelors  in  Hospitality &amp; Tourism  Management"),
        (48,"Bachelors of Psychology"),
        (49,"BAMS"),
        (50,"BDS"),
        (51,"BE ( Environmental Engineering)"),
        (52,"BSW"),
        (53,"BUMS"),
        (54,"Chartered Accountant"),
        (55,"Company Secretary"),
        (56,"DHMS"),
        (57,"Dialysis Technician Course"),
        (58,"Diploma  in Mechanical  Engineering"),
        (59,"Diploma  in Multimedia"),
        (60,"Diploma Computer Engineer"),
        (61,"Diploma Electronic &amp; comm. Engineering"),
        (62,"Diploma in Automobiles Engineer"),
        (63,"Diploma in Beauty Parlor"),
        (64,"Diploma in Ceramic Engineer"),
        (65,"Diploma in Chemical Engineering"),
        (66,"Diploma in Civil Engineer"),
        (67,"Diploma In Computer Application"),
        (68,"Diploma in Electrical  Engineering"),
        (69,"Diploma in Fashion Designing"),
        (70,"Diploma in Home Science"),
        (71,"Diploma in Hotel managment"),
        (72,"Diploma in Medical Laboratory Technology"),
        (73,"Diploma in Nursing"),
        (74,"Diploma in Pharmacy"),
        (75,"Diploma in Plastic Engineering"),
        (76,"Diploma in Software Engineering"),
        (77,"Diploma"),
        (78,"Fashion Designing"),
        (79,"Fine Arts"),
        (80,"General Nursing &amp; Midwifery"),
        (81,"H.S.C."),
        (82,"I.T Professional"),
        (83,"ITI - Industrial Training Institute"),
        (84,"LLB"),
        (85,"LLM"),
        (86,"M. Lib"),
        (87,"M.B.A"),
        (88,"M.B.B.S."),
        (89,"M.C.A"),
        (90,"M.Com."),
        (91,"M.D ( Anesthesia )"),
        (92,"M.D (Physician)"),
        (93,"M.D (Pidiatric)"),
        (94,"M.E  (Chemical)"),
        (95,"M.E ( I.T)"),
        (96,"M.E ( Mechanical )"),
        (97,"M.E (Electronic &amp; Communication )"),
        (98,"M.E Civil ( Geotech )"),
        (99,"M.E. ( Structure )"),
        (100,"M.E.(Production)"),
        (101,"M.Ed ( Masters in Education )"),
        (102,"M.Pharmacy"),
        (103,"M.Phil"),
        (104,"M.S.W ( Master in Social Work )"),
        (105,"M.Sc ( I.T )"),
        (106,"M.Tech"),
        (107,"Master  Degree  in Development  Communication"),
        (108,"Master  of   Fine Arts"),
        (109,"Master in Computer Science"),
        (110,"Master Of Accounting and Financial Management"),
        (111,"Master of Arts"),
        (112,"Master of Computer Engineering"),
        (113,"Master of E-Commerce"),
        (114,"Master of MASS Comunication"),
        (115,"Master of PhysioTherapy"),
        (116,"Master of Science"),
        (117,"Masters in Clinical Psychology"),
        (118,"Masters in Project Management &amp; Security System"),
        (119,"MD( Pidiatric)"),
        (120,"MDS ( Master of Dental surgery )"),
        (121,"NDDY ( Naturopathy Doctor )"),
        (122,"Occupational Theraphy"),
        (123,"P.G  in Human Resaurce Management"),
        (124,"P.T.C"),
        (125,"PGDIT"),
        (126,"Ph.D"),
        (127,"S.S.C."),
        (128,"Sanitary inspector"),
        (129,"School level"),
        (130, "Other")
    	]

    body_type_list = [
        (1, 'Athletic'),
        (2, 'Average'),
        (3, 'Slim'),
        (4, 'Heavy')
        ]

    complexion_list = [
        (1,'Dark'),
        (2,'Fair'),
        (3,'Wheatish Brown'),
        ]

    mother_tongue_list = [
        (1,'Hindi'),
        (2,'Bengali'),
        (3,'Telugu'),
        (4,'Marathi'),
        (5,'Tamil'),
        (6,'Urdu'),
        (7,'Gujarati'),
        (8,'Kannada'),
        (9,'Malayalam'),
        (10,'Odia'),
        (11,'Punjabi'),
        (12,'Assamese'),
        (13,'Maithili'),
        (14,'Bhili/Bhilodi'),
        (15,'Santali'),
        (16,'Kashmiri'),
        (17,'Nepali'),
        (99,'Other')
        ]

    yes_no_list = [
	    (1,'Yes'),
	    (0,'No')
	    ]

    weight_list = [(0,'Select Option')] +[(i,i) for i in range(35, 121)]

    user = models.ForeignKey(User)

    first_name = models.CharField(_('Name of User'), 
        blank=True, 
        max_length=255)

    surname = models.CharField(_('Name of User'), 
        blank=True, 
        max_length=255)

    dob = models.DateField(_('Date of Birth'), 
        null=True)

    gender = models.CharField(choices=gender_list, default = 'M', null = True, max_length=1)

    location = models.CharField(_('Location'), 
        blank=True, max_length=255)

    marital_status = models.IntegerField(choices=marital_status_list, 
        null = True)

    address_line1 = models.CharField(_('Address Line 1'), 
        blank = True, 
        max_length=255)

    address_line2 = models.CharField(_('Address Line 2'), 
        blank = True, 
        max_length=255)

    address_line3 = models.CharField(_('Address Line 3'), 
        blank = True, 
        max_length=255)

    city = models.ForeignKey(Cities, null=True, 
        db_constraint=False, on_delete=models.CASCADE)

    country = models.ForeignKey(Country,to_field="name", 
        db_constraint=False, on_delete=models.CASCADE, 
        default = "India")

    height = models.CharField(choices=height_list,
        blank = True, null=True, max_length=10)

    weight = models.IntegerField(choices=weight_list,
        blank = True, null=True)

    body_type = models.IntegerField(choices=body_type_list, 
        null=True)

    complexion = models.IntegerField(choices=complexion_list, 
        null=True)

    mother_tongue = models.IntegerField(choices=mother_tongue_list, 
        null=True)

    about_me = models.TextField(null=True)

    looking_for = models.TextField(null=True)

    reason_registration = models.IntegerField(choices=reason_registration_list, 
        null=True
        )

    #qualification & work

    qualification = models.IntegerField(choices=qualification_list, 
        null=True
        )

    qualification_summary = models.TextField(null=True)

    occupation = models.IntegerField(choices=occupation_list, 
        null=True
        )

    occupation_summary = models.TextField(null=True)

    income = models.IntegerField(choices=income_list, 
        null=True
        )

    #religion
    hijab = models.IntegerField(choices=yes_no_list, 
        null=True
        )

    beard  = models.IntegerField(choices=yes_no_list, 
        null=True
        )

    cast = models.CharField(_('Cast'), 
        blank = True, 
        max_length=255)

    sub_cast = models.CharField(_('Sub cast'), 
        blank = True, 
        max_length=255)

    # Family background
    father_name = models.CharField(_('Father name'), 
        blank=True, 
        max_length=255)

    mother_name = models.CharField(_('Father name'), 
        blank=True, 
        max_length=255)

    contact_no = models.CharField( 
        blank=True, 
        max_length=15)

    mobile_no = models.CharField(
        blank=True, null=True,
        max_length=15)

    family_summary = models.TextField(null=True)


class ProfileImage(models.Model):
    profile_image = models.FileField(upload_to='profile_images', blank=True, null=True)
    profile = models.ForeignKey(Profile)  
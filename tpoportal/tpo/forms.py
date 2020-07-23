from django import forms
from django.core.validators import RegexValidator
import MySQLdb

passcode = "prayas123"
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets  are allowed.')
def getdepts():
	db= MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
	c=db.cursor()
	c.execute("SELECT * from department ; ")
	lis = []
	tup = ("-1","None")
	lis.append(tup)
	for x in c :
		tup = (x[0],x[1]) 
		lis.append(tup)
	return lis

def getclasses():
	db= MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
	c=db.cursor()
	c.execute("SELECT * from class ; ")
	lis = []
	tup = ("-1","None")
	lis.append(tup)
	for x in c :
		tup = (x[0],x[1]) 
		lis.append(tup)
	return lis

class RegisterForm(forms.Form):
	roll = forms.CharField(max_length=20 , help_text="Roll Number",required = True)

	fname = forms.CharField(max_length=30 , help_text="First Name",required = True,validators=[alpha])

	lname = forms.CharField(max_length=30 , help_text="Last Name",required = True,validators=[alpha])

class HelpForm(forms.Form):
	name=forms.CharField(max_length=40,help_text='Name',validators=[alpha])
	contact=forms.CharField(max_length=20,required=False,help_text='Contact')
	email=forms.EmailField(help_text='E-Mail Address')
	designation=forms.CharField(max_length=40,help_text='Designation',validators=[alpha])
	help_id=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	admin_id=forms.IntegerField(widget=forms.HiddenInput(),initial=0)

class PostForm(forms.Form):
	admin_id=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	date = forms.DateField(help_text='Date(YYYY-MM-DD)')
	content = forms.CharField(max_length=4000,help_text='Post',widget=forms.Textarea)	


class CompanyForm(forms.Form):
	admin_id=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	name = forms.CharField(max_length=40,help_text='Name of the Company')		
	type = forms.CharField(max_length=20,help_text='Type Internship/Placement',validators=[alpha])		
	desc = forms.CharField(max_length=2000,help_text='Job Description')	

class StudWillForm(forms.Form):
	rollno = forms.CharField(max_length=20, help_text="Roll Number", initial="")
	department = forms.ChoiceField( help_text="Department",required=False)
	class_stud = forms.ChoiceField( help_text="Class", initial="",required=False)
	fname = forms.CharField(max_length=30, help_text="First Name", initial="",validators=[alpha])
	mname = forms.CharField(max_length=30, help_text="Middle Name", initial="",required=False,validators=[alpha])
	lname = forms.CharField(max_length=30, help_text="Last Name", initial="",validators=[alpha])
	gender = forms.CharField(max_length=1, help_text="Gender", initial="M/F",required=False)
	email = forms.EmailField(help_text="E-Mail", initial="")
	mtongue = forms.CharField(max_length=40, help_text="Mother Tongue", initial="",required=False,validators=[alpha])
	paddr = forms.CharField(max_length=200, help_text="Permanent Address", initial="",required=False)
	taddr = forms.CharField(max_length=200, help_text="Temporary Address", initial="",required=False)

	contact = forms.CharField(max_length=20, help_text="Contact No.", initial="",required=False)
	#resume = forms.CharField(max_length=10, help_text="Resume", initial="",required=False)
	backlogs = forms.CharField(max_length=100, help_text="Backlogs", initial="",required=False)
	interests = forms.CharField(max_length=200, help_text="Interests", initial="",required=False)
	#profile_picture = forms.CharField(max_length=10, help_text="Profile Picture", initial="",required=False)
	def __init__(self, *args, **kwargs):
        	super(StudWillForm, self).__init__(*args, **kwargs)
        	self.fields['class_stud'] = forms.ChoiceField(choices = getclasses(),help_text="Class",required=False ,initial=getclasses()[1][0] )

        	self.fields['department'] = forms.ChoiceField(choices = getdepts(),help_text="Department",required=False ,initial=getdepts()[1][0] )


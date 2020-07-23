from django.shortcuts import render

import MySQLdb,os

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from tpo.forms import HelpForm, PostForm, CompanyForm,StudWillForm,RegisterForm
from django.core.files.storage import FileSystemStorage
import re,datetime,time

passcode = "prayas123"

def tpr(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        sql = """select t.roll_number , s.first_name , s.EMail , d.dept_NAME from TPR t , department d , 
                student s  where t.dept_id = d.dept_id and s.roll_number = t.roll_number  ;"""

        lis = []
        try :
                c.execute(sql)
                lis =c.fetchall()

        except:
                db.close()
                return HttpResponse("Some error occured")
        db.close()
        context = RequestContext(request,{'tab':lis})
        return render_to_response('tpo/tpr.html',context_instance=context)


def adminregister(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if('admin' not in request.session): return HttpResponse("Some Error Occured")
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        if (request.method == 'POST') :
                name,email,typ  = request.POST.get("name") ,request.POST.get("email"),request.POST.get("type")
                pata = re.compile("^[a-zA-Z]*$")
                if(pata.search(name)==None or pata.search(typ)== None) :
                        db.close()
                        return HttpResponse("Please ensure name and type contains only characters")
                sql = """ select * from admin where EMail = "%s" ; """ %(email)
                try:
                        if(c.execute(sql)!=0) : return HttpResponse("Person already registered")
                        else:
                                
                                sql = """ insert into admin(name,EMail,type) values ("%s","%s","%s") ; """ %(name,email,typ)
                                c.execute(sql)
                                db.commit()
                                return admin(request)

                                
                except : return HttpResponse("Some Error Occured")                



        context = RequestContext(request)
        return render_to_response('tpo/adminregister.html',context_instance=context)


def admintpr(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if('admin' not in request.session): return HttpResponse("Some Error Occured")

        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        if (request.method == 'POST') :
                roll,dept = request.POST.get("roll") ,int(request.POST.get("dept"))
                sql = """ select * from student where roll_number = "%s" and dept_id = %d ; """ %(roll,dept)
                try:
                        if(c.execute(sql)==0) : return HttpResponse("Either no such student or student doesnt belong to this dept.")
                        else:
                                sql = """ select * from TPR where roll_number = "%s" ; """ %(roll)
                                if(c.execute(sql)==0):
                                        sql = """ insert into TPR values ("%s",%d) ; """ %(roll,dept)
                                        c.execute(sql)
                                        db.commit()
                                        return admin(request)

                                else : return HttpResponse("Student is already a TPR")
                except : return HttpResponse("Some Error Occured")                


        c.execute("select * from department;")
        depts= []
        for x in c.fetchall():
                tup = (x[0],x[1])
                depts.append(tup)

        context = RequestContext(request,{'depts':depts})
        return render_to_response('tpo/admintpr.html',context_instance=context)


def post(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        sql = " select a.name , a.Email , p.Date , p.Content  from post p  , admin a where p.admin_id = a.admin_id order by p.Date desc ;"
        posts = []
        try :
                c.execute(sql)
                posts =c.fetchall()

        except:
                db.close()
                return HttpResponse("Some error occured")
        db.close()
        context = RequestContext(request,{'posts':posts})
        return render_to_response('tpo/post.html',context_instance=context)


def studentgrade(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")
        
        if(request.method=='POST') :
                sem,cgpa = int(request.POST.get("sem")) ,float(request.POST.get("cgpa")) 
                roll = request.session['student'][0]


                db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                c=db.cursor()
                sql = """SELECT * from cgpa where semester = %d and roll_number = "%s" ;  """ %(sem,roll)
                try:
                        if(c.execute(sql)!=0):
                                sql = """ update cgpa set spi = %.2f where semester = %d and roll_number = "%s" ; """ %(cgpa,sem,roll)
                        else:
                                sql = """ insert into cgpa values(%d,"%s",%.2f) ; """ % (sem,roll,cgpa)
                        print sql
                        c.execute(sql)
                        db.commit()
                        db.close()
                        return student(request)
                except: 
                        db.close()
                        return HttpResponse("Some Error Occured") 



        context = RequestContext(request)
        return render_to_response('tpo/grade.html' , context_instance = context)


def resume_upload(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        dir =os.path.join(BASE_DIR,'media')
        #print(dir)
        print(os.path.exists(os.path.join(dir,str(request.session['student'][0])+".pdf")))
        if request.method == 'POST' and request.FILES['resume']:
                resume = request.FILES['resume']
                fs = FileSystemStorage()
                try:
                        fname,ftype = resume.name.rsplit('.',1)
                        if(ftype!='pdf'): return HttpResponse("Improper File Format")
                except: return HttpResponse("Improper File Format") 
                if(os.path.exists(os.path.join(dir,str(request.session['student'][0])+".pdf"))): os.remove(os.path.join(dir,str(request.session['student'][0])+".pdf"))
                else :
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()
                        sql = """ update student set resume="Y" where roll_number = '%s' ; """ % (request.session['student'][0])
                        c.execute(sql)
                        db.commit()
                        db.close()


                filename = fs.save(str(request.session['student'][0])+".pdf", resume)
                uploaded_file_url = fs.url(filename)
                return render(request, 'tpo/resume.html', {
                        'uploaded_file_url': uploaded_file_url })
        return render(request, 'tpo/resume.html')


def picture_upload(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        dir =os.path.join(BASE_DIR,'media')
        #print(dir)
        print(os.path.exists(os.path.join(dir,str(request.session['student'][0])+".pdf")))
        if request.method == 'POST' and request.FILES['picture']:
                picture = request.FILES['picture']
                fs = FileSystemStorage()
                ftype=''
                try:
                        fname,ftype = picture.name.rsplit('.',1)
                        if(not (ftype=='jpg' or ftype=='jpeg')): return HttpResponse("Improper File Format. Upload a jpg/jpeg image. "+ftype+" is not allowed")
                except: return HttpResponse("Improper File Format") 
                if(os.path.exists(os.path.join(dir,str(request.session['student'][0])+"p."+ftype))): os.remove(os.path.join(dir,str(request.session['student'][0])+"p."+ftype))
                else :
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()
                        sql = """ update student set profile_picture="Y" where roll_number = '%s' ; """ % (request.session['student'][0])
                        c.execute(sql)
                        db.commit()
                        db.close()
                filename = fs.save(str(request.session['student'][0])+"p."+ftype, picture)
                uploaded_file_url = fs.url(filename)
                return render(request, 'tpo/picture.html', {
                        'uploaded_file_url': uploaded_file_url })
        return render(request, 'tpo/picture.html')

def home(request):
        context = RequestContext(request, {'request': request, 'user': request.user})
   	if(request.user == None):
                return render_to_response('tpo/home.html',context_instance=context)					
        if(request.user != None and not request.user.is_anonymous()):
                #print (request.user.is_anonymous())
                return main(request)
        return render_to_response('tpo/home.html',context_instance=context)


def main(request):
	
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        c.execute(""" SELECT * from help ;""")
        help_list =[]
        for x in c.fetchall():
                help_list.append(x)
        db.close() 
        if(request.user== None) : return HttpResponse("Some Error Occured")
        if(request.user.is_anonymous()):
                return HttpResponse("Some Error Occured")  
        #print '\n'
        #print request.user.email
        #print '\n'   

        
        
        #print '\n'
        #print global_user.email
        #print '\n'

        context  = RequestContext(request,{'help': help_list, 'user':request.user})
        return render_to_response('tpo/main.html',context_instance=context)

def register(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        
        if (request.method=='POST') : 
                form = RegisterForm(request.POST)
                if(form.is_valid()):
                        #print form.cleaned_data
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()
                        op = form.cleaned_data

                        sql = """ insert into student (roll_number,first_name,last_name,EMail) values ("%s", "%s","%s","%s") 
                                """ % (op['roll'], op['fname'] , op['lname'] ,request.user.email)
                        try:
                                c.execute(sql)
                                db.commit()
                                db.close()
                        except:
                                db.close()
                                return HttpResponse("Some Error Occured")
                        return HttpResponse("Done")
                else :
                        return HttpResponse(form.errors)
        
        try:
                email_name , email_provider = request.user.email.rsplit('@',1)
        except :
                return HttpResponse("Some Error Occured")

        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        try:
            sql = """SELECT * from student where EMail = "%s" """ % (request.user.email)
            if (c.execute(sql)==0):
                    if(email_provider=='itbhu.ac.in') :
                            email2 = email_name+'@i'+ email_provider
                            sql = """SELECT * from student where EMail = "%s" """ % (email2)
                            if(c.execute(sql)!=0):
                                    return HttpResponse("User Already registered")
            else:
                    return HttpResponse("User Already registered")
        except:
            db.close()
            return HttpResponse("Some Error Occurred")
        form = RegisterForm()
        context = RequestContext(request,{'form':form})
        return render_to_response('tpo/register.html',context_instance=context)




def student(request):
        #print "111111" + str(request.user) + "1111111"

        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        #if global_user.email != email:
        #        return HttpResponse("Please login first")

        try:
                email_name , email_provider = request.user.email.split('@')
        except :
                return HttpResponse("Some Error Occured")

        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        sql = " SELECT * from student where EMail = '%s' ; " % (request.user.email)
        try:
            if(c.execute(sql) !=1):
                    if(email_provider=='itbhu.ac.in'):
                            email2 = email_name+'@i'+ email_provider
                            sql = " SELECT * from student where EMail = '%s' ; " % (email2)
                            c.execute(sql)
        except:
                db.close()
                return HttpResponse("Some Error Occurred")
        lis = c.fetchall()
        if(len(lis)!=1): return HttpResponse("Some Error Occured")


	context  = RequestContext(request,{ 'student': lis[0]})
        request.session['student'] = lis[0]

	return render_to_response('tpo/student.html',context_instance=context)	

def studwillcomp(request,comp_id):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        comp_id = int(comp_id)
        sql = """ SELECT * from company where comp_id  = %d ; """  %(comp_id)
        try:
                if ( c.execute(sql)!=1) : return HttpResponse("Some Error Occured")
        except: return HttpResponse("Some Error Occured")
        company = c.fetchone()
        roll = request.session['student'][0]
        sql = """ SELECT * from willingness where comp_id = %d and roll_number = "%s" ; """ %(comp_id,roll)
        cnt = c.execute(sql)
        if(cnt==0):
                # insert
                try:
                        sql = """ INSERT into willingness values (%d, "%s" , "%s") ; """ %(comp_id,roll,"willing_sent")
                        c.execute(sql)
                        db.commit()
                except :
                        db.close()
                        return HttpResponse("Some Error Occured")
        elif(cnt!=1) : return HttpResponse("Some Error Occured")
        else :
                sql = """ delete from willingness where comp_id = %d and roll_number = "%s" ; """ %(comp_id,roll)
                try:
                        c.execute(sql)
                        db.commit()
                except:
                        db.close()
                        return HttpResponse("Some Error Occured")
        db.close()
        return studwill(request)

def studwill(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        try:
                sql = "SELECT * from cgpa where semester = 0 and roll_number = '%s' ; " % (request.session['student'][0])
                c.execute(sql)
                cg = float(c.fetchone()[2]) 
                sql = "SELECT * from recruitment where dept_id = %d and class_id = %d and cgpa <= %f ; " % (request.session['student'][1],request.session['student'][2],cg)
                c.execute(sql)
        except : return HttpResponse("Please upload cgpa, department and class first")
        comp_list = c.fetchall()
        companies = []
        #statuses =[]
        roll = request.session['student'][0]
        for x in comp_list :
                try:
                        cid = x[0]
                        sql = """ SELECT * from company where comp_id  = %d ; """  %(cid)
                        if( c.execute(sql) !=1) : return HttpResponse("Some Error Occured")

                        tc = list(c.fetchone())
                        sql = """ SELECT * from willingness where comp_id = %d and roll_number = "%s" ; """ %(cid,roll)
                        if(c.execute(sql)==0): 
                                #ans = (cid,roll,"Not Willing")
                                tc.append("Not Willing")
                                #statuses.append(ans)
                        else:

                                tc.append(c.fetchone()[2])
                        companies.append(tc)
                except:
                        db.close()
                        return HttpResponse("Some Erro Occured")
        db.close()
        
        context = RequestContext(request,{'student': request.session['student'] , 'companies': companies })
        print companies

        return render_to_response('tpo/studwill.html',context_instance=context)

def studentupdate(request):
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        if 'student' not in request.session : return HttpResponse("Some Error Occured")

        stud = request.session['student']
        if( request.method == 'POST') :
                form = StudWillForm(request.POST)
                upd = {}
                if(form.is_valid()):
                        fd = form.cleaned_data
                        print "hell"
                        print stud[1]
                        print stud[2]

                        if(fd['rollno']!=stud[0]) : upd['roll_number'] =fd['rollno']
                        if(int(fd['department'])!=-1):
                                if(int(fd['department'])!=stud[1]) : upd['dept_id'] =int(fd['department'])
                        if(int(fd['class_stud'])!=-1):
                                if(int(fd['class_stud'])!=stud[2]) : upd['class_id'] =int(fd['class_stud'])
                        if(fd['fname']!=stud[3]) : upd['first_name'] =fd['fname']
                        if(fd['mname']!=stud[4]) : upd['middle_name'] =fd['mname']
                        if(fd['lname']!=stud[5]) : upd['last_name'] =fd['lname']
                        if(fd['gender']!=stud[6]) : upd['gender'] =fd['gender']
                        if(fd['email']!=stud[7]) : upd['EMail'] =fd['email']
                        if(fd['mtongue']!=stud[8]) : upd['Mother_Tongue'] =fd['mtongue']
                        if(fd['paddr']!=stud[9]) : upd['Address_temp'] =fd['paddr']
                        if(fd['taddr']!=stud[10]) : upd['Address_perm'] =fd['taddr']
                        if(fd['contact']!=stud[11]) :
                                pat = re.compile("^(\+91-)?[0-9]{10}$")
                                pat2 = re.compile("^0[0-9]{10}$")
                                if(pat.search(fd['contact'])== None and pat2.search(fd['contact'])==None) : return HttpResponse("Enter Valid Phone Number")
                                upd['contact'] =fd['contact']
                        if(fd['backlogs']!=stud[13]) : upd['backlogs'] =fd['backlogs']
                        if(fd['interests']!=stud[14]) : upd['interests'] =fd['interests']

                        #print upd
                        if(len(upd.keys())==0) : return student(request)
                        newroll = fd['rollno']
                        sql = """ update student set  """
                        for key in upd.keys():
                                if(key != 'dept_id' and key!='class_id'): sql += """ %s = "%s" """ %(key,upd[key])
                                else : sql += """ %s = %d """ %(key,int(upd[key]))

                                sql += ","
                        sql = sql[:-1]
                        sql += """  where roll_number = %s ;""" %(stud[0])
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()

                        try:
                                c.execute(sql)
                                db.commit()
                        except : return HttpResponse("Some Error Occured")

                        sql = """ select * from student where roll_number = %s """ %(newroll)
                        if(c.execute(sql)!=1) :return HttpResponse("Some Diff Error Occured")
                        request.session['student'] = c.fetchall()[0]
                        db.close()
                        if(newroll !=stud[0]):
                                BASE_DIR = os.path.dirname(os.path.dirname(__file__))
                                dir =os.path.join(BASE_DIR,'media')
                                if(stud[12]=='Y') : 
                                        os.rename(os.path.join(dir,stud[0]+".pdf"),os.path.join(dir,newroll+".pdf"))
                                if(stud[15]=='Y'):
                                        if(os.path.exists(os.path.join(dir,stud[0]+"p.jpg"))):
                                                os.rename(os.path.join(dir,stud[0]+"p.jpg"),os.path.join(dir,newroll+"p.jpg"))
                                        elif(os.path.exists(os.path.join(dir,stud[0]+"p.jpeg"))) :
                                                os.rename(os.path.join(dir,stud[0]+"p.jpeg"),os.path.join(dir,newroll+"p.jpeg"))



                        return student(request)

                return HttpResponse(form.errors)
        
        form = StudWillForm(initial={'rollno':stud[0] ,
                                        'department' : stud[1] ,
                                        'class_stud' : stud[2] ,
                                        'fname' : stud[3] , 
                                        'mname' : stud[4] ,
                                        'lname' : stud[5] ,
                                        'gender' : stud[6] ,
                                        'email' : stud[7] ,
                                        'mtongue' : stud[8] ,
                                        'paddr' : stud[9] ,
                                        'taddr' : stud[10] ,
                                        'contact' : stud[11] ,
                                       # 'resume' : student[12] ,
                                        'backlogs' : stud[13] ,
                                        'interests' : stud[14] ,
                                        #'profile_picture' : student[15] ,
                                })
        context = RequestContext(request, { 'form': form})
        return render_to_response('tpo/studentupdate.html',context_instance=context)

def admin(request):
        #print request.user
        #if global_user == None: return HttpResponse("Some Error Occured")
	#email = 'prayas.jain.cse14@iitbhu.ac.in'
        if request.user == None: return HttpResponse("Some Error Occured")
        if request.user.is_anonymous():  return HttpResponse("Some Error Occured")
        #if global_user.email != email:
        #        return HttpResponse("Please login first")
        try:
                email_name , email_provider = request.user.email.split('@')
        except :
                return HttpResponse("Some Error Occured")
                        
        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
        c=db.cursor()
        sql = " SELECT * from admin where EMail = '%s' ; " % (request.user.email)
        try:
                if(c.execute(sql) !=1):
                        if(email_provider=='itbhu.ac.in'):
                                email2 = email_name+'@i'+ email_provider
                                sql = " SELECT * from admin where EMail = '%s' ; " % (email2)
                                c.execute(sql)

        except:
                db.close()
                return HttpResponse("Some Error Occured")
        lis = c.fetchall()
        if(len(lis)!=1): return HttpResponse("Some Error Occured")




        #print sql
        #print lis[0]
        context  = RequestContext(request,{'admin': lis[0]})
        request.session['admin'] = lis[0]
        db.close()
	return render_to_response('tpo/admin.html',context_instance=context)

def adminhelp(request):
        
        #print admin_id
        if('admin' not in request.session): return HttpResponse("Some Error Occured")
        #print request.user
        #print request.session['admin']
        if(request.method == 'POST'):
                form =  HelpForm(request.POST)
                if(form.is_valid()):
                        #print form 
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()
                        pat = re.compile("^(\+91-)?[0-9]{10}$")
                        pat2 = re.compile("^0[0-9]{10}$")
                        if(pat.search(str(form.cleaned_data['contact']))== None and pat2.search(str(form.cleaned_data['contact']))==None) : return HttpResponse("Enter Valid Phone Number")
                        

                        sql = """ insert into help (admin_id ,name, contact, EMAil, Designation ) values (%d, "%s" , "%s" ,"%s", "%s") ; """ % (request.session['admin'][0],
                                str(form.cleaned_data['name']),str(form.cleaned_data['contact']) ,str(form.cleaned_data['email']) ,
                                str(form.cleaned_data['designation'])) 

                        try:
                                c.execute(sql)
                                db.commit()
                        except: 

                                return HttpResponse("Some Error Occured")    
                       
                        db.close()

                        return admin(request)
                else: return HttpResponse("Some Error Occured")
        else :
                form = HelpForm()
                context  = RequestContext(request,{'form':form , 'admin_id':request.session['admin'][0]})
                return render_to_response('tpo/adminhelp.html',context_instance=context)

def adminpost(request):
        #print admin_id
        if('admin' not in request.session): return HttpResponse("Some Error Occured")

        print request.session['admin']
        if(request.method == 'POST'):
                form = PostForm(request.POST)
                
                if(form.is_valid()):
                        #print form.cleaned_data
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()

                         #print form.cleaned_data['content']
                        #tmp = r'%s'%form.cleaned_data['content']
                        #print tmp
                        y,m,d = str(form.cleaned_data['date']).split('-')
                        y,m,d = int(y),int(m),int(d)
                        
                        try:
                                dt = datetime.date(y,m,d)
                                dd = datetime.date(2016,1,1)
                                dc = datetime.date(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))
                                if(dt>dc):
                                        return HttpResponse("Date is later than today's date")
                                if(dt<dd):
                                        return HttpResponse("Enter a more latest date")
                        except:
                                db.close()
                                return HttpResponse("Enter Valid Date")


                        sql = """ insert into post (admin_id ,Date, content ) values (%d, "%s" , "%s") ; """ % (request.session['admin'][0],str(form.cleaned_data['date']),form.cleaned_data['content'])     
                       
                        
                        try:
                                c.execute(sql)
                                db.commit()
                        except: 

                                return HttpResponse("Some Error Occured")
                        db.close()
                        return admin(request)
                else : return HttpResponse("Some Error Occured")

        else :
                form = PostForm()
                print form.fields
                context  = RequestContext(request,{'form':form , 'admin_id':request.session['admin'][0]})
                return  render_to_response('tpo/adminpost.html',context_instance=context)   

def admincompany(request):
        #print admin_id
        if('admin' not in request.session): return HttpResponse("Some Error Occured")
        if(request.method == 'POST'):
                form = CompanyForm(request.POST)
                if(form.is_valid()):
                        #print form
                        db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                        c=db.cursor()
                        sql = """ insert into company (admin_id ,name, type, description ) values (%d, "%s" , "%s" , "%s") ; """ % (
                                request.session['admin'][0],str(form.cleaned_data['name']),form.cleaned_data['type'],
                                form.cleaned_data['desc'])     
                        try:
                                c.execute(sql)
                                db.commit()
                        except: 

                                return HttpResponse("Some Error Occured")
                        db.close()
                       

                        return admin(request)
                else : return HttpResponse("Some Error Occured")

        else :
                form = CompanyForm()
                context  = RequestContext(request,{'form':form , 'admin_id':request.session['admin'][0]})
                return  render_to_response('tpo/admincompany.html',context_instance=context)                                     

def admincompwill(request):
        if('admin' not in request.session): return HttpResponse("Some Error Occured")
        if(request.method == 'POST'):
                #print "hell"
                #print request.POST.get("company")
                #print request.POST.get("department")
                #print request.POST.get("class")
                fcomp,fdept,fclass,fcg = int(request.POST.get("company")) ,int(request.POST.get("department")) , int(request.POST.get("class")), float(request.POST.get("cgpa")) 
                                      
                db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                c=db.cursor()
                sql = """ select * from dept_class where dept_id = %d and class_id = %d ;""" %(fdept,fclass)
                if(c.execute(sql)==0):
                        return HttpResponse("The following department does not have this class") 

                sql = """ select * from recruitment where comp_id = %d and dept_id = %d and 
                                class_id = %d and CGPA = %.2f ; """ %(fcomp,fdept,fclass,fcg)
                try:
                        if ( c.execute(sql) != 0 ) : return HttpResponse("Already Open")
                except: 
                        db.close()
                        return HttpResponse("Some Error Occured")
                sql = """ select * from recruitment where comp_id = %d and dept_id = %d and 
                                class_id = %d  ; """ %(fcomp,fdept,fclass)
                try:
                        if ( c.execute(sql) != 0 ) :
                                sql = """ update recruitment set CGPA = %.2f where comp_id = %d and dept_id = %d and 
                                class_id = %d  ; """ %(fcg,fcomp,fdept,fclass)
                                c.execute(sql)
                                db.commit()
                except : 
                        db.close()
                        return HttpResponse("Some Error Occured")
                else:


                        sql = """ insert into recruitment  values (%d, %d , %d , %.2f) ; """ % (
                                fcomp,fdept,fclass,fcg) 
                        #print sql 
                        try:
                                c.execute(sql)
                                db.commit()
                        except: 
                                return HttpResponse("Some Error Occured")
                db.close()
                
                return admin(request)
        else:
                db = MySQLdb.connect(host="localhost",user="root",passwd=passcode,db="TPO")
                c=db.cursor()
                try:
                        c.execute("select * from company ;")
                        companies = c.fetchall()
                        c.execute("select * from department ;")
                        departments = c.fetchall()
                        c.execute("select * from class ;")
                        classes = c.fetchall()
                        db.close()
                except:
                        db.close()
                        return HttpResponse("Some Error Occurred")
                context = RequestContext(request,{'companies':companies, 'departments':departments, 'classes':classes})
                return render_to_response('tpo/companywilling.html',context_instance=context)



from tkinter import *
import joblib
import warnings
warnings.filterwarnings('ignore')
top = Tk()
#top.attributes('-fullscreen', True)
#top.geometry("200x100")
top.geometry("1300x1200")
font = ('times', 16, 'bold')
font2 = ('times', 12,)
title = Label(top, text='Performance Analyzer for Employees')
title.config(bg='brown', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)
global p,a
p=Button()
a=Button()



def attr_cal():
        model_attr=joblib.load('INX_Future_Inc_Attrition.ml')
        global p,a, empenvsatis_field, empwrkbl_field, empjbsatis_field, yrssincelstprom_field, empovrtm_field, emphrrate_field

        
        prd_list=[empenvsatis_field.get(), emphrrate_field.get(), empjbsatis_field.get(), empovrtm_field.get(), empwrkbl_field.get(), yrssincelstprom_field.get()]
        
        prds = model_attr.predict([prd_list])

        attrition = Label(top, text="Your Attrition Chance is : "+str(prds[0]),font=font2)
        attrition.place(x=400,y=600)

    


def attr():
    global p,a, empenvsatis_field, empwrkbl_field, empjbsatis_field, yrssincelstprom_field, emphrrate_field, empovrtm_field
    p.destroy()
    a.destroy()
    
    heading = Label(top, text="Fill the below Particulars",font=font2)
    heading.place(x=500,y=140)
    

    
    empenvsatis = Label(top, text="Emp Environment Satisfaction")
    empenvsatis.place(x=420,y=200)
    empenvsatis_range = Label(top, text="Range: 1-4")
    empenvsatis_range.place(x=800,y=200)
    empenvsatis_field = Entry(top)
    empenvsatis_field.place(x=650,y=200)

    emphrrate=Label(top, text="Emp Hourly Rate")
    emphrrate.place(x=420, y=240)
    emphrrate_range = Label(top, text="Range: 1-4")
    emphrrate_range.place(x=800,y=240)
    emphrrate_field = Entry(top)
    emphrrate_field.place(x=650, y= 240)

    empjbsatis = Label(top, text="Emp Job Satisfaction")
    empjbsatis.place(x=420, y=280)
    empjbsatis_range = Label(top, text="Range: 1-4")
    empjbsatis_range.place(x=800,y=280)
    empjbsatis_field = Entry(top)
    empjbsatis_field.place(x=650, y=280)


    empovrtm= Label(top, text = "Over Time")
    empovrtm.place(x=420, y = 320)
    empovrtm_range = Label(top, text="Range: 0-1")
    empovrtm_range.place(x=800,y=320)
    empovrtm_field = Entry(top)
    empovrtm_field.place(x=650, y= 320)
    
    
    empwrkbl=Label(top, text='Emp Work Life Balance')
    empwrkbl.place(x=420,y=360)
    empwrkbl_range = Label(top, text="Range: 1-4")
    empwrkbl_range.place(x=800,y=360)
    empwrkbl_field = Entry(top)
    empwrkbl_field.place(x=650,y=360)


    
    
    yrssincelstprom = Label(top, text="Years Since Last Promotion")
    yrssincelstprom.place(x=420,y=400)
    yrssincelstprom_range = Label(top, text="Range: 1-15")
    yrssincelstprom_range.place(x=800,y=400)
    yrssincelstprom_field = Entry(top)
    yrssincelstprom_field.place(x=650,y=400)
    


    submit = Button(top, text="Submit",width=20, command=attr_cal)
    submit.place(x=550, y= 450)




def pr_hk():
    if (clicked.get() == "" and clicked2.get() == "" and empenvsatis_field.get() == "" and empwrkbl_field.get() == "" and expyrs_field.get() == "" and expyrscrrole_field.get() == "" and yrssincelstprom_field.get() == "" and yrswtcrmng_field.get() == ""):
        print("empty input")
    else:
        

        model_pr=joblib.load('INX_Future_Inc.ml')

        model_hike=joblib.load('INX_Future_Inc_Hike.ml')

        dpt={'Finance': 0, 'Human Resource': 1, 'Research & Development': 2, 'Sales': 3}
        jbrl={'Business Analyst': 0, 'Data Scientist': 1, 'Delivery Manager': 2, 'Developer': 3, 'Finance Manager': 4, 'Healthcare Representative': 5, 'Human Resources': 6, 'Laboratory Technician': 7, 'Manager': 8, 'Manager R&D': 9, 'Manufacturing Director': 10, 'Research Director': 11, 'Research Scientist': 12, 'Sales Executive': 13, 'Sales Representative': 14, 'Senior Developer': 15, 'Senior Manager R&D': 16, 'Technical Architect': 17, 'Technical Lead': 18} 

        prd_list=[dpt[clicked.get()], jbrl[clicked2.get()], empenvsatis_field.get(), empwrkbl_field.get(), expyrs_field.get(), expyrscrrole_field.get(), yrssincelstprom_field.get(), yrswtcrmng_field.get()]
        print(prd_list)
        prds = model_pr.predict([prd_list])
        print(prds)
        prd_list.append(prds[0])
        prds2=model_hike.predict([prd_list])
        print(prds2)

        performance = Label(top, text="Your Predicted performance is : "+str(prds[0]),font=font2)
        performance.place(x=400,y=600)

        hike= Label(top, text="Your Predicted Hike percentage is : "+str(prds2[0]), font=font2)
        hike.place(x=400, y=620)


def p_cal():
    global p,a, empdpt_field, empjbrl_field, empenvsatis_field, empwrkbl_field, expyrs_field, expyrscrrole_field, yrssincelstprom_field, yrswtcrmng_field, clicked, clicked2
    p.destroy()
    a.destroy()
    
    heading = Label(top, text="Fill the below Particulars",font=font2)
    heading.place(x=500,y=140)
    
    empdpt = Label(top, text="Emp Department")
    empdpt.place(x=420,y=200)
    options = ["Sales", "Research & Development", "Finance", "Human Resources"]
    clicked = StringVar()
    clicked.set( "Select the Department")
    empdpt_field = OptionMenu( top , clicked , *options )
    empdpt_field.place(x=650,y=200)

    empjbrl = Label(top, text="Emp Job Role")
    empjbrl.place(x=420,y=240)
    options2 = ["Sales Executive", "Developer", "Manager R&D", "Research Scientist", "Sales Representative", "Laboratory Technician", "Senior Developer", "Manager", "Finance Manager",  "Human Resources", "Technical Lead", "Manufacturing Director", "Healthcare Representative", "Data Scientist", "Research Director", "Business Analyst", "Senior Manager R&D", "Delivery Manager", "Technical Architect"]
    clicked2 = StringVar()
    clicked2.set( "Select the Job Role")
    empjbrl_field = OptionMenu( top , clicked2 , *options2 )
    empjbrl_field.place(x=650,y=240)
    
    empenvsatis = Label(top, text="Emp Environment Satisfaction")
    empenvsatis.place(x=420,y=280)
    empenvsatis_range = Label(top, text="Range: 1-4")
    empenvsatis_range.place(x=800, y=280)
    empenvsatis_field = Entry(top)
    empenvsatis_field.place(x=650,y=280)
    
    empwrkbl=Label(top, text='Emp Work Life Balance')
    empwrkbl.place(x=420,y=320)
    empwrkbl_range = Label(top, text="Range: 1-4")
    empwrkbl_range.place(x=800, y=320)
    empwrkbl_field = Entry(top)
    empwrkbl_field.place(x=650,y=320)
    
    expyrs = Label(top, text="Experience Years At This Company")
    expyrs.place(x=420,y=360)
    expyrs_range = Label(top, text="Range: 1-40")
    expyrs_range.place(x=800, y=360)
    expyrs_field = Entry(top)
    expyrs_field.place(x=650,y=360)
    
    expyrscrrole = Label(top, text="Experience Years In Current Role")
    expyrscrrole.place(x=420, y=400)
    expyrscrrole_range = Label(top, text="Range: 0-18")
    expyrscrrole_range.place(x=800, y=400)
    expyrscrrole_field = Entry(top)
    expyrscrrole_field.place(x=650,y=400)
    
    yrssincelstprom = Label(top, text="Years Since Last Promotion")
    yrssincelstprom.place(x=420,y=440)
    yrssincelstprom_range = Label(top, text="Range: 0-15")
    yrssincelstprom_range.place(x=800, y=440)
    yrssincelstprom_field = Entry(top)
    yrssincelstprom_field.place(x=650,y=440)
    
    
    yrswtcrmng = Label(top, text="Years With Current Manager")
    yrswtcrmng.place(x=420,y=480)
    yrswtcrmng_range = Label(top, text="Range: 0-16")
    yrswtcrmng_range.place(x=800, y=480)
    yrswtcrmng_field = Entry(top)
    yrswtcrmng_field.place(x=650,y=480)

    submit = Button(top, text="Submit",width=20, command=pr_hk)
    submit.place(x=550, y= 550)





p = Button(top, text = "Calculate performance/ Hike",height=2,width=25,font=font2,command=p_cal)
p.place(x=300,y=200)
a = Button(top,text = "Calculate Attrition Rate",height=2,width=25,font=font2, command=attr)
a.place(x=700,y=200)




top.mainloop()

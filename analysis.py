import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\Dharma Narisetty\Desktop')

result = open("matplot.txt",'w')
g = {'A+':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0,'W':0}
def file(file_name):
    f = open(file_name,'r')
    return f
#A function that converts the file content to a pandas dataframe
def data_frame(file):
    df = pd.read_csv(file)
    df = df[::2]
    return df
#A function that calculates the cgpa
def cgpa(grades,branch):
    #To compare which section did the best  'F' garde was given a -ve point
    grades = [g[x] for x in grades]
    b = ['CSD','CSO','CSM','CSE','IT','CSBS']
    if branch == 'CSBS':
        theory = [3,3,3,3,3]
        labs = [1,1,1,1.5]
    elif branch not in b:
        print('Branch not found please enter a branch from : ')
        print(*b)
        return 
    else:
        theory = [3,3,3,3]
        labs = [1.5,1.5,3,1.5]
    sgpa = 0
    t = 0
    for i in range(0,len(theory)):
        sgpa+=grades[i]*theory[i]
        t=i
    t+=1
    for j in range(0,len(labs)):
        sgpa+=grades[t]*labs[j]
        t+=1
    sgpa = sgpa/19.5
    return sgpa
#function that gives mean and standadrd deviation of the grades
def mean_sd(arr):
    sum = 0
    var = 0
    for i in arr:
        sum+=i
    mean = sum/len(arr)
    for i in arr:
        var = var+(i-mean)**2
    var = var/(len(arr))
    sd = (var)**0.5
    return mean,sd
#this function caalculates class average gpa
def class_gpa(df,branch):
    mat = df.values
    gpa = 0
    stu_gpa = []
    for i in range(0,len(mat)):
        t = cgpa(mat[i],branch)
        gpa+=t
        stu_gpa.append(t)
    gpa = gpa/len(mat)
    sd = 0
    for i in stu_gpa:
        sd = sd + (i-gpa)**2
    sd = (sd/len(mat))**0.5
    result.write(branch)
    gpa = round(gpa,3)
    sd = round(sd,3)
    result.write(f"\nclass average gpa = {gpa}\n")   
    result.write(f"THe class standard deviation = {sd}\n")
#this function calculates each subject mean and sd gpa
def sub_gpa(df,branch):
    branches = {
        'CSD':['CD111','CD112','CD113','CD114','CD151','CD152','CD153','CD154'],
        'CSBS':['CB111','CB112','CB113','CB114','CB115','CB151','CB152','CB153','CB154'],
        'CSM':['CM111','CM112','CM113','CM114','CM151','CM152','CM153','CM154'],
        'CSO':['CO111','CO112','CO113','CO114','CO151','CO152','CO153','CO154'],
        'CSE':['CS111','CS112','CS113','CS114','CS151','CS152','CS153','CS154'],
        'IT':['IT111','IT112','IT113','IT114','IT151','IT152','IT153','IT154']
               }
    branch_subs = branches[branch]
    for i in branch_subs:
        subject_grade = df[i]
        subject_grade = [g[x] for x in subject_grade]
        m,sd = mean_sd(subject_grade)
        m = round(m,4)
        sd = round(sd,3)
        op = f"SUB = {i}  MEAN = {m} STANDARD DEVIATION = {sd}"
        result.write(op)
        result.write("\n")

def section(df,branch):
    result.write(f"{branch} : \n")
    print(type(df))
    if branch=='CSD':
        A = df[:63]
        B = df[63:126]
        C = df[126:]
        class_gpa(A,'CSD')
        class_gpa(B,'CSD')
        class_gpa(C,'CSD')
        sub_gpa(A,'CSD')
        sub_gpa(B,'CSD')
        sub_gpa(C,'CSD')

    elif branch =='CSE':
        A = df[:66]
        B = df[66:128]
        C = df[128:]
        class_gpa(A,'CSE')
        class_gpa(B,'CSE')
        class_gpa(C,'CSE')
        sub_gpa(A,'CSE')
        sub_gpa(B,'CSE')
        sub_gpa(C,'CSE')
        
    elif branch == 'IT':
        A  = df[:63]
        B  = df[63:]
        class_gpa(A,'IT')
        class_gpa(B,'IT')
        sub_gpa(A,'IT')
        sub_gpa(B,'IT')
       
    elif branch == 'CSM':
        A = df[:65]
        B = df[65:129]
        C = df[129:]
        class_gpa(A,'CSM')
        class_gpa(B,'CSM')
        class_gpa(C,'CSM')
        sub_gpa(A,'CSM')
        sub_gpa(B,'CSM')
        sub_gpa(C,'CSM')
    else:
        print("This branch does not contain any sections")
 
csd = file("ds.csv")
it = file("it.csv")
cse = file("cse.csv")
CSO = file("CSO.csv")
csm = file("csm.csv")
csbs = file("csbs.csv")

csd_df = data_frame(csd)
it_df = data_frame(it)
cse_df = data_frame(cse)
csm_df = data_frame(csm)
CSO_df = data_frame(CSO)
csbs_df = data_frame(csbs)

class_gpa(csd_df,'CSD')
class_gpa(it_df,'IT')
class_gpa(cse_df,'CSE')
class_gpa(csm_df,'CSM')
class_gpa(CSO_df,'CSO')
class_gpa(csbs_df,'CSBS')

sub_gpa(csd_df,'CSD')
sub_gpa(it_df,'IT')
sub_gpa(cse_df,'CSE')
sub_gpa(csm_df,'CSM')
sub_gpa(CSO_df,'CSO')
sub_gpa(csbs_df,'CSBS')

section(csd_df,'CSD')
section(csm_df,'CSM')
section(cse_df,'CSE')
section(it_df,'IT')

it.close()
cse.close()
CSO.close()
csm.close()
csbs.close()
result.close()

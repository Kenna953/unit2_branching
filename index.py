''' 
course ID: CPRG-216-A Object Orriented Programming

Description:  
Retirement eligibility checker (Graded question 
Manna Corp. provides pension and other benefits to eligible retiring employees. The 
minimum age for retirement is 50 years. If a retiring employee’s age is at least 65 or their 
age plus years of service is at least 80 then that employee is eligible for a full pension. 
Otherwise, the retiring employee is eligible for a discounted (reduced) pension. Write a 
program that prompts the user for age and years of service, determines their eligibility, and 
prints the appropriate message as shown below. 

Author: McKenna Morrison-Ripley

Date: 2/5/2026
'''
retirement_age = 65
min_retirement_age = 50

print("Manna Corp. Retirement Eligibility Checker ")

age=input("Age: ")
years_of_service=input("Years of service: ")

if int(age) >= min_retirement_age:

        if  int(age) >= retirement_age or int(age) + int(years_of_service) == 80:
        ##s_of_service >= retirement_age or age + years_of_service == 80:## 
            print("You are eligible for retirement with full pension benefits")
        else:
            print("You are eligible for  retirement with discounted pension benefits")
else:
    print("You are not eligible for retirement")
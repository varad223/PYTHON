marks=[]
flag=1
for i in range (5):
	m=int(input("enter marks: "))
	if m>40:
	   marks.append(m)
	else:
	   flag=0
	   break
if flag==1:
	print("5 subject marks: ",marks)
	print("Total Marks: ",sum(marks))
	print("percentage: ",sum(marks)/5)
	percentage=sum(marks)/5
	if percentage>=75:
		print("Grade is Distinction")
	elif percentage>=60 and percentage<75:
		print("Grade is 1st Division")
	elif percentage>=50 and percentage<60:
		print("Grade is 2nd Division")
	elif percentage>=40 and percentage<50:
		print("Grade is 3rd Division")
else:
	print("Result is Fail")

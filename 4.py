year=int(input("year:\n"))  #輸入年月日
month=int(input("month:\n"))
day=int(input("day:\n"))
a=[31,28,31,30,31,30,31,31,30,31,30,31] #自訂列表為每月的天數
total=0
add=0
if (year%4==0 and year%100!=0) or year%400==0:
    add=1 #判斷是否為潤年
for i in range(0,month-1):
    total+=a[i] #加到那個月之前就停下來
total+=day+add
print("it is the %dth day."%total)
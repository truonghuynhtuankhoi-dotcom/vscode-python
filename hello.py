'''
a=int(input("please input a number:"))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")

'''
'''
age=int(input("Please input your age:"))
if age>=18:
    print("you are available to drive car")
else: 
    print("you are not")
'''
'''
a,b,c=map(int,input("please input three number and spacing it:").split())
max=a
if a>b and a>c:
    print(max)
elif b>a and b>c:
    max=b
    print(max)
else:
    max=c
    print(max)
'''
'''
year=int(input("please input year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("this is leap year")
else:
    print("this is not a leap year")
'''
'''
a=int(input("please input a number:"))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
else:
    print("the number is 0")
'''
"""
a=int(input("please input a number:"))
if a<=1:
    print("This is not a prime number")
elif a==2 or a==3:
    print("This is a prime number")
else:
    prime_number=True
    for n in range (1,int(a**0.5) +1):
        if 6*n+1==a or 6*n-1==a:
            prime_number=False
            print("this is a prime number")
            break
    if prime_number:
        print("this is not a prime number")

"""
''''
a,b,c= map(int,input("Please input the three side of triangle:").split())
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("This is a equilateral triangle")
    elif a==b or a==c or c==b:
        print("This is a isoclent triangle")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("this is square triangle")
    else:
        print("this is a normal triangle")
else:
    print("this is not a triangle")
'''
'''
rows=int(input("How many row:"))
col=int(input("How many colomns:"))

for r in range (rows):
    for c in range (col):
        print("*", end=" ")
    print()
'''

"""
for n in range (10):
    if n==5:
        print("break")
        break
    print(n)
if n>0:
    print(f"cycle:{n}")
"""
"""
a=int(input("Give the number:"))
b=1
c=1
sum=0

if a==1:
    print("0")
elif a>=2:
    for n in range(a-1):
        b=c
        c=sum
        sum=b+c
    print(sum)

"""

'''
product=0
while product<100: 
    num=int(input("Please enter a number:")) 
    product=num*10
    print(f"The product is {product}")
'''
'''
repeat="y"
while repeat=="y" or repeat=="Y":
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(f"the sum is {a+b}")
    repeat=input("Do you want to perform the operation again(press y/Y to repeat):")
if repeat != "y" or repeat!="Y":
    print("The program ends here")
'''
"""
for n in range (0,1001,10):
    if n!=1000:
        print(f"{n},",end=" ")
    else:
        print(n)
"""
'''
sum=0
for n in range (10):
    num=int(input("Please enter a number:"))
    sum+=num
print(f"The total is {sum}")
'''
'''
sum=0
for n in range(5):
    bug=int(input("Enter the number of bugs collected today:"))
    sum+=bug
print(f"The total number of bugs collected is {sum}")
'''

"""
for n in range (10,31,5):
    print(f"your calories after {n} minutes is: {n*4.2} ")
"""
"""
v=int(input("Enter the number of miles driven:"))
t=int(input("How many hours has it traveled:"))
print("Hour\tDistance Traveled")
for n in range (t):
    print(n+1,"\t\t", v*(n+1))
"""
"""
sum=0
year=int(input("Enter the year:"))
for n in range (year):
    for i in range(12):
        rainfall=float(input(f"Enter the rainfall for each month {i+1} in year {n+1}:"))
        sum+=rainfall
print(f"The total rainfall for {year} years is {sum} inches")
print(f"The average monthly rainfall is {sum/(year*12):.2f} inches")
"""
"""
print("Celsius\t\tFahrenheit")
for c in range (0,21):
    f=(c*9/5)+32
    print(f"{c}\t\t{f}")

"""
'''
speed=int(input("What is the speed of the vehicle in mph?"))

time=int(input("How many hours has it traveled?"))

print("Hour\t Distance Traveled")
for n in range (time):

     print(f"{n+1} \t\t {speed*(n+1)}")
'''
#chap 5

#1
"""
def main():
    distance=input("Enter the distance in killometers:")
    convert(distance)
def convert(km):
    miles=float(km)*0.6214
    print(f"The distance in miles is {miles:.2f}")

main()
"""
#3
"""
def main():
    cost=float(input("Enter the replacement cost of a building: "))
    insure(cost)
def insure(cost):
    price=cost*0.8
    print(f"The minimun amount of insurance should buy for property is: {price:,.2f}")

main()
"""
#4
"""
def main():
    monthly_total=monthly_cost()
    display_cost(monthly_total)


def display_cost(monthly_total):

    annual_cost=monthly_total*12
    print(f"your monthly cost is {monthly_total:.2f}")
    print(f"your annual cost is {annual_cost:.2f}")


def monthly_cost():
    loan=float(input("how much is your loan payment: "))
    insurance=float(input("How much is your insurance: "))
    gas=float(input("How much is your gas: "))
    tires=float(input("How much is your tires costs: "))
    maintenance=float(input("How much is your maintenance cost: "))
    cost=loan+insurance+gas+tires+maintenance
    return cost

main()    
"""
#5
"""
def cost(actual_cost):
    assessment_value=actual_cost*0.6
    tax_cost=(assessment_value/100)*0.72
    print(f"The assessment value is {assessment_value:.2f}")
    print(f"The tax cost is {tax_cost:.2f}")


def main():
    actual_cost=float(input("Enter the actual value of a piece of property: "))
    cost(actual_cost)
    
main()    
"""

#6
'''
def get_ticktet():
    ticketa=int(input("how many ticket for the class A: "))
    ticketb=int(input("how many ticket for the class B: "))
    ticketc=int(input("how many ticket for the class C: "))
    return ticketa, ticketb, ticketc

def income(a,b,c):
    total=a*20+b*15+c*10
    return total

def main():
    a,b,c=get_ticktet()
    total=income(a,b,c)
    print(f"The amount of income: {total}")

if __name__=='__main__':
    main()       
'''
#7
"""
def labor_time(space):
    time=(space/112)*8
    return time

def paint_price(space,cost):
    price=(space/112)*cost
    return price
def main():
    space=float(input("Enter the square feet of wall space to be painted: "))
    gallon_price=float(input("Enter the price of paint per gallon: "))
    time_labor=labor_time(space)
    price=paint_price(space,gallon_price)
    print(f"The number of gallon require: {(space/112)}")
    print(f"The hours of labor required: {time_labor}")
    print(f"The cost of the paint: {price}")
    print(f"The labor charges: {time_labor*35.00}")
    print(f"The total cost of paint job {time_labor*35.00+price}")

if __name__=="__main__":
    main()    
"""

#8
"""
def state_tax(revenue):
    tax=revenue*0.05
    return tax

def country_tax(revenue):
    tax=revenue*0.025
    return tax

def main():
    total_sales=float(input("Enter your total sales: "))
    state=state_tax(total_sales)
    country=country_tax(total_sales)
    print(f"The amount of country sales tax: {country}")
    print(f"The amount of state sales tax: {state}")
    print(f"The total sales tax: {country+state}")

if __name__=='__main__':
    main()
"""
#9
"""
def feet_into_inches(feet):
    inches=feet*12
    return inches

def main():
    feet=float(input("Enter distance in feet: "))
    print(f"The distance in inches is {feet_into_inches(feet)}")
main()
"""

#10
"""
import random
import operator
ops={
    "+": operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv,

}

def question():
    op=random.choice(["+","-","*","/"])
    if  op=="/":
        b=random.randint(1,10)
        a=random.randint(0,10)
    else:
        a=random.randint(0,10)
        b=random.randint(0,10)
    func=ops[op]
    result=round(func(a,b),2)
    return a,b,op,result

def cheking(c,d):
    if c==d:
        print("You're correct")
        return False
    else:
        print(f"You're wrong, please enter again!")
        return True

def main():
    a,b,op,right_answer=question()
    flag=True
    n=0
    while flag==True:
        print(f"  {a}", end=" ")
        if op != "*":
            print(f"{op} {b} =",end="")
        else:
            print(f"x {b} =",end="")
        d=float(input("  "))
        flag=cheking(right_answer,d)
        if flag==False:
            break
        n+=1
        if flag==True:
            print(f"You have {3-n} attempt remaining")
        if n==3:
            print(f"The right answer is {right_answer}")
            break

if __name__=="__main__":
    main()
"""
#11
"""
def max(a,b):
    max=a
    if a<b:
        max=b
    elif a==b:
        max=None
    return max

def main():
    a=float(input("Type a: "))
    b=float(input("Type b: "))
    result=max(a,b)
    if result==None:
        print("They are equal")
    else:
        print(f"The larger number is: {result}")
main()
"""
#12
"""
def falling_distance(t):
    d=1/2*9.8*(t**2)
    return d

def main():
    for i in range (1,11):
        print(round(falling_distance(i),2))

main()
"""
#13
"""
def kinetic_energy(m,v):
    KE=1/2*m*v**2
    return KE

def main():
    m,v=map(float,input("Enter the mass and velocity: ").split())
    result=kinetic_energy(m,v)
    print("KE=",round(result,2))

main()

"""

#14
"""
def calc_average(a,b,c,d,e):
    avg=sum([a,b,c,d,e])/5
    return avg

def determine_grade(avg):
    if 90<=avg and avg<100:
        print("Grade A")
    elif 80<=avg and avg<89:
        print("Grade B")
    elif 70<=avg and avg<79:
        print("Grade C ")
    elif 60<=avg and avg<69:
        print("Grade D")
    elif  avg<59:
        print("Grade F")

def main():
    a,b,c,d,e=map(float,input("Enter your score: ").split())
    determine_grade(calc_average(a,b,c,d,e))

main()   
"""

#15
"""
import random

def random_num():
    nums=[random.randint(1,10) for _ in range (100)]
    return nums

def main():
    n=0
    nums=random_num()
    print(nums)
    for i in range (100):
        a=nums[i]
        if a%2==0:
            n+=1
    print(f"The numbers of even number is {n}")

main()        
"""

#16
"""
import math
def is_prime(num):
    if num<1:
        return False
    elif num==2 or num==3:
        return True
    elif num %2==0 or num%3==0:
        return False
    for i in range (5,int(math.sqrt(num))+1,6):
        if num % i==0 or num % (i+2)==0:
            return False
    return True
        
def main():
    num=int(input("Enter the number: "))
    if is_prime(num)
        print("The number is a prime number")
    else:
        print("The number is not a prime number")            
main()
"""
# 17
"""
import math
def is_prime(num):
    if num<=1:
        return False
    elif num==2 or num==3:
        return True
    elif num %2==0 or num%3==0:
        return False
    for i in range (5,int(math.sqrt(num))+1,6):
        if num % i==0 or num % (i+2)==0:
            return False
    return True

def main():
   
    print(", ".join(map(str,sorted(i for i in range (1,101) if is_prime(i)))))



main()
"""

#18
"""
def fomular(P,i,t):
    F=P*(1+i)**t
    return F

def main():
    a,b,c=map(float,input("Enter the account's present value, monthly interest rate, and the number of months: ").split())
    print(f"The future value of account is {round(fomular(a,b,c),2)}")

main()    
"""

#19
"""
import random

def ramdom_num():
    a=random.randint(1,100)
    return a
def checking(num,user_input):
    if user_input<num:
        print("Too low, try again")
        return True
    elif user_input>num:
        print("Too high, try again")
        return True
    else:
        print("Congratulation")
        return False
def main():
    flag_1="y"
    while flag_1=="y" or flag_1=="Y":
        num=ramdom_num()
        count=0
        flag=True
        while flag:
            user_input=int(input("Enter a number: "))
            flag=checking(num,user_input)
            count+=1
        print(f"The number of guesses is {count}")
        flag_1=input("Do you to play again. Enter y/Y to play again: ")

if __name__=="__main__":
    main()     
"""
#20
'''
import random
def bot():
    move=random.choice(["rock","paper","scissors"])
    print(f"Bot moves is {move}")
    return move

def game_rule(move,player_move):
    if move==player_move:
        return 1
    elif (player_move=="rock" and move=="scissors") or (player_move=="paper" and move=="rock") or (player_move=="scissors" and move=="paper"):
        return 2
    else:
        return 3

def main():
    bot_win=0
    player_win=0
    while bot_win!=2 and player_win!=2:
        player_move=input("Enter your move: ")
        bot_move=bot()
        situation=game_rule(bot_move,player_move)
        if situation==1:
            print("The game is tie")
        elif situation==2:
            print("You win this round")
            player_win+=1
        else:
            print("You lose this round")
            bot_win+=1
    if bot_win==2:
        print("You lose")
    else:
        print("You win")
        
if __name__=="__main__":
    main()
'''

#chap 6
#1
"""
count=int(input("How many numbers do you want to enter: "))
def main():
    with open('numbers.txt',"w") as f:
        for i in range (1,count+1):
            num=int(input(f"Number {i}: "))
            f.write(f"{num}\n")

if __name__=="__main__":
    main()
"""


"""
def main():
    sum=0
    count=0
    try:
        with open("numbers.txt", "r") as f:
            line=f.readline()
            while line!='':
                line=line.rstrip()
                sum+=int(line)
                count+=1
                line=f.readline()
            if count>0:
                avg=sum/count
                print(f"{avg:.2f}")
            else:
                print("Invalid")
    except IOError:
        print("Error when opening file!")
    except ValueError:
        print("Please convert to a number")     

if __name__=="__main__":
    main()            
"""

#2
"""
def main():
    file_input=input("Enter the name of file: ")
    try:
        with open(file_input, "r") as f:
            line=f.readline()
            count=0
            while line!="" and count<5:
                line=line.rstrip()
                print(f"Line {count+1}:", line)
                line=f.readline()
                count+=1
    except FileNotFoundError:
        print("File is not found!")
if __name__=="__main__":
    main()    
"""

#3
"""
def main():
    file_input=input("Enter the name of file: ")
    try:
        with open(file_input,"r") as f:
            count=0
            line=f.readline()
            while line!="":
                line=line.rstrip()
                print(f"line {count+1}:", line)
                line=f.readline()
                count+=1
    except FileNotFoundError:
        print("File is not found")

if __name__=="__main__":
    main()        
"""
# 4
"""
def main():
    with open("names.txt", "r") as f:
        count=0
        line=f.readline()
        while line!="":
            if line.strip():
                count+=1
            line=f.readline()
    print(f"The total of names is {count}")

if __name__=="__main__":
    main()
"""

#7
"""
import random
def main():
    with open("numbers.txt", "w") as f:
        amount=int(input("How many random numbers do you want: "))
        for i in range (1, amount +1):
            nums=random.randint(1,500)
            f.write(f"{nums}\n")
    print(f"{i} number(s) has been copied to numbers.txt")
if __name__=="__main__":
    main()
"""
#8
"""
def main():
    with open("numbers.txt", "r") as f:
        count=0
        sum=0
        line=f.readline()
        while line!= "":
            if line.strip():
                line=int(line)
                count+=1
                print(f"Number {count}: {line}")
                sum+=line
            line=f.readline()
        print("The total:",sum)
        print("The number of random numbers:",count)
if __name__=="__main__":
    main()
"""
#10
"""
def main():
    amount=int(input("How many people do you want to enter: "))
    with open("golf.txt", "w") as f:
        for i in range(1,amount+1):
            print(f"The player number {i}")
            name=input("Enter player's name: ")
            score=input("Enter player's score: ")
            f.write(f"{name}\n")
            f.write(f"{score}\n")
            f.write("\n")
            print()
    print("All player's information have been copied to golf.txt")
if __name__=="__main__":
    main()
"""
"""
def main():
    count=0
    with open("golf.txt", "r") as f:
        name=f.readline()
        while name!="":
            if name.strip():
                count+=1
                score=f.readline()
                name=name.rstrip()
                score=score.rstrip()
                print(f"Player {count}:")
                print(f'Name: {name}')
                print(f"Player's score: {score}")
                print()
            name=f.readline()
if __name__=="__main__":
    main()
"""
"""
def main():
    NUM_DAYS=5
    sales=[0]*NUM_DAYS
    for index in range(len(sales)):
        sales[index]=float(input("F:"))
    print("your value:")
    for value in sales:
        print(value)

if __name__=="__main__":
    main()
"""

#chap 7 
#1
"""
def main():
    alist=[]
    total=0
    count=int(input("How many days you want to enter: "))
    for i in range (1,count+1):
        product=float(input(f"Enter a store's sales of day {i}: "))
        alist.append(product)
    for value in alist:
        total+=value
    print(f"The total of store's sales is {total}")

if __name__=="__main__":
    main()
"""
#2
"""
import random

def main():
    alist=[]
    for i in range(7):
        num=random.randint(0,9)
        alist.append(num)
    for value in alist:
        print(value,end="")

if __name__=="__main__":
    main()
"""

#3
"""
def main():
    list1=["January","February","March","April","May","June","July","August","September","October","November","December"]
    list2=[]
    for i in range(0,12):
        rainfall=float(input(f"Enter the total rainfall of {list1[i]}: "))
        list2.append(rainfall)
    print(f'The total rainfall for the year is {sum(list2)}')
    print(f'The average monthly rainfall is {sum(list2)/12}')
    print(f'The hightest month is {list1[list2.index(max(list2))]}')
    print(f'The lowest month is {list1[list2.index(min(list2))]}')

if __name__=="__main__":
    main()
"""
#4
"""
def main():
    list1=[]
    for i in range(20):
        num=int(input(f"Enter numbers {i+1}: "))
        list1.append(num)
    print(f"The lowest number in the list is {min(list1)}")
    print(f"The highest number in the list is {max(list1)}")
    print(f'The total of the list is {sum(list1)}')
    print(f"The average of the list is {sum(list1)/20}")

if __name__=="__main__":
    main()
"""
#5 
'''
import random
def intrandom():
    with open ("charge_accounts.txt", "w") as f:
        for i in range(0,100):
            num=random.randint(1000000,9999999)
            f.write(f"{num}\n")

if __name__=="__main__":
    intrandom()

def main():
    list1=[]
    with open ("charge_accounts.txt", "r") as f:
        numbers=f.readline()
        while numbers!="":
            if numbers.strip():
                numbers=numbers.rstrip()
                list1.append(numbers)
                numbers=f.readline()
    acount_number=input("Enter your charge acount number: ")
    if acount_number in list1:
        print("Valid!")
    else:
        print("The number is invalid")

if __name__=="__main__":
    main()
'''
#6
"""
def dontknow(list1,n):
    list2=[value for value in list1 if value>n]
    unique_list=list(set(list2))
    if len(list2)==0:
        print("There is no numbers in the list that greater than number n!")
    else:
        print("These numbers below are greater than number n")
        for item in unique_list:
            print(item)

def main():
    list1=[]
    count=int(input("How many numbers do you want to insert:"))
    for i in range(count):
        num=int(input("Enter the number for creating the list: "))
        list1.append(num)
    n=int(input("Enter the number n: "))

    dontknow(list1,n)

if __name__=="__main__":
    main()          
"""
#7
'''
def student_answer():
    list1=[]
    with open ("student_answer.txt", "w") as f:
        for i in range(20):
            answer=input(f"Enter your answer for question number {i+1}: ")
            f.write(f'{answer}\n')
            list1.append(answer)
    return list1
def right_answer():
    list2=[]
    with open ("right_answer.txt", "r") as f:
        answer=f.readline()
        while answer!="":
            if answer.strip():
                answer=answer.rstrip()
                list2.append(answer)
            answer=f.readline()
    return list2

        

def main():
    right_count=0
    wrong_count=0
    list2=right_answer()
    list1=student_answer()
    for i in range(20):
        if (list1[i].lower())==list2[i]:
            right_count+=1
        elif (list1[i].lower())!=list2[i]:
            wrong_count+=1
    if right_count>=15:
        print("You passed")
    else:
        print("You failed the exam.")
    print(f'The total of right answer is {right_count}')
    print(f'The wrong answer is {wrong_count}')

if __name__=="__main__":
    main()


'''

#8
"""
def main():
    list1=[]
    with open ("first-names.txt", "r") as f:
        name=f.readline()
        while name!="":
            if name.strip():
                name=name.rstrip()
                list1.append(name)
                name=f.readline()
    your_name=input("Enter your name: ")
    your_name=your_name.capitalize()
    if your_name in list1:
        print("Your name is among the popular name.")
    else:
        print("Your name is unique")

if __name__=="__main__":
    main()
"""

#9
"""
def main():
    annual_change=0
    total=0
    max=0
    year_max=0
    year_min=0
    list1=[]
    with open ("names.txt","r") as f:
        population=f.readline()
        while population!="":
            if population.strip():
                population=population.rstrip()
                list1.append(population)
                population=f.readline()
    list1=list(map(int,list1))

    min=list1[1]-  list1[0]
    for i in range(1,41):
            annual_change=list1[i]-  list1[i-1]
            total+=annual_change
            if annual_change>max:
                max=annual_change
                year_max=i+1950
            elif annual_change<min:
                min=annual_change
                year_min=i+1950
    print(f'The average annual change in population during the time is {total/40}')
    print(f'The year with the greatest increase in population is {year_max-1}-{year_max} with {max}')
    print(f'The year with the smallest increase in population is {year_min-1}-{year_min} with {min}')

if __name__=="__main__":
    main()
"""
#10
"""
def main():
    list1=[]
    with open ("names.txt",'r') as f:
        champion=f.readline()
        while champion!="":
            if champion.strip():
                champion=champion.rstrip()
                list1.append(champion)
                champion=f.readline()
    names=input("Enter your favorite team: ")
    count=list1.count(names)
    print(f'The numbers of win of your favorite team: {count}')

if __name__=="__main__":
    main()
"""

#chap 8
#1
'''
def initials():
    full_name = input("Enter your full name: ")

    # Tách chuỗi bằng khoảng trắng
    parts = full_name.split()

    # Lấy chữ cái đầu mỗi phần, đổi thành uppercase
    result = ""
    for word in parts:
        result += word[0].upper() + ". "

    print(result.strip())

initials()
'''
#2
"""
def sum_digits():
    s = input("Enter a series of digits: ")

    total = 0
    for ch in s:
        total += int(ch)   # mỗi ký tự là 1 số

    print("The sum is:", total)

sum_digits()
"""

#3
"""
def date_printer():
    date = input("Enter a date (mm/dd/yyyy): ")

    # Tách chuỗi bằng dấu '/'
    month, day, year = date.split("/")

    # Tên tháng
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Chuyển tháng dạng string "03" → thành int 3 → chọn "March"
    month_name = months[int(month) - 1]

    print(f"{month_name} {int(day)}, {year}")

date_printer()
"""
#4
"""
def morse_converter():

    # List các ký tự (chữ + số + dấu)
    letters = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9',
        ',', '.', '?', ' '
    ]

    # List Morse cùng index
    morse = [
        '.-','-...','-.-.','-..','.', '..-.','--.','....','..',
        '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
        '...','-','..-','...-','.--','-..-','-.--','--..',
        '-----','.----','..---','...--','....-','.....','-....',
        '--...','---..','----.',
        '--..--','.-.-.-','..--..',' '  # comma, period, question mark, space
    ]

    text = input("Enter a string: ")
    text = text.upper()

    output = ""

    for ch in text:
        # tìm index của ký tự ch
        if ch in letters:
            idx = letters.index(ch)     # tìm vị trí trong list
            output += morse[idx] + " "  # lấy Morse tương ứng
        else:
            output += "? "              # ký tự không hỗ trợ

    print("\nMorse code:")
    print(output)


morse_converter()
"""

#5

"""

def phone_translator():

    # List các nhóm chữ
    letters = [
        "ABC",
        "DEF",
        "GHI",
        "JKL",
        "MNO",
        "PQRS",
        "TUV",
        "WXYZ"
    ]

    # List số tương ứng
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]

    phone = input("Enter a phone number (XXX-XXX-XXXX): ")
    phone = phone.upper()

    result = ""

    for ch in phone:
        if ch.isalpha():  # nếu là chữ
            for i in range(len(letters)):
                if ch in letters[i]:   # tìm nhóm chữ chứa ký tự đó
                    result += numbers[i]
                    break
        else:
            result += ch  # giữ nguyên dấu '-' hoặc số

    print("Translated number:", result)


phone_translator()
"""
#chap 9
#1
"""
def main():

    # Dictionary: Course → Room
    rooms = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }

    # Dictionary: Course → Instructor
    instructors = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    course = input("Enter a course number: ").upper()

    if course in rooms:
        print(f"\nCourse: {course}")
        print(f"Room: {rooms[course]}")
        print(f"Instructor: {instructors[course]}")
    else:
        print("Course not found.")


main()
"""

#2
"""

import random

def capital_quiz():

    # Dictionary: state → capital
    states = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "New York": "Albany",
        "Texas": "Austin"
    }

    correct = 0
    incorrect = 0

    # Convert keys to list so we can pick random states
    state_list = list(states.keys())

    # Quiz user for all states (10 questions)
    for i in range(len(state_list)):
        state = random.choice(state_list)       # pick a random state
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == states[state].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The capital is {states[state]}.\n")
            incorrect += 1

        state_list.remove(state)  # remove so it doesn't repeat the question

    print("===== Results =====")
    print(f"Correct answers:   {correct}")
    print(f"Incorrect answers: {incorrect}")


capital_quiz()
"""

#10

#1
"""
class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # ----- SETTERS -----
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # ----- GETTERS -----
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = input("Enter your pet's age: ")

    # tạo object Pet
    pet1 = Pet(name, animal_type, age)

    # in ra dữ liệu dùng getters
    print("\nPet Information:")
    print("Name:", pet1.get_name())
    print("Animal Type:", pet1.get_animal_type())
    print("Age:", pet1.get_age())


main()
"""
#2
"""

class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0     # theo đề bài

    # tăng speed thêm 5
    def accelerate(self):
        self.__speed += 5

    # giảm speed 5
    def brake(self):
        self.__speed -= 5

    # lấy speed hiện tại
    def get_speed(self):
        return self.__speed

def main():
    year = input("Enter the car's year model: ")
    make = input("Enter the make of the car: ")

    car = Car(year, make)

    print("\nAccelerating...")
    for i in range(5):
        car.accelerate()
        print("Speed after accelerating:", car.get_speed())

    print("\nBraking...")
    for i in range(5):
        car.brake()
        print("Speed after braking:", car.get_speed())


main()
"""
#3

"""
class PersonalInformation:

    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # ----- MUTATORS (setters) -----
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    # ----- ACCESSORS (getters) -----
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

def main():

    # 3 fictional persons
    p1 = PersonalInformation("Alice Sparks", "123 Rainbow St", 22, "555-1111")
    p2 = PersonalInformation("Brian Knox", "77 Sunset Blvd", 35, "555-2222")
    p3 = PersonalInformation("Chloe Rivera", "890 Maple Ave", 28, "555-3333")

    # Display information
    print("Person 1:")
    print("Name:", p1.get_name())
    print("Address:", p1.get_address())
    print("Age:", p1.get_age())
    print("Phone:", p1.get_phone())
    print()

    print("Person 2:")
    print("Name:", p2.get_name())
    print("Address:", p2.get_address())
    print("Age:", p2.get_age())
    print("Phone:", p2.get_phone())
    print()

    print("Person 3:")
    print("Name:", p3.get_name())
    print("Address:", p3.get_address())
    print("Age:", p3.get_age())
    print("Phone:", p3.get_phone())
    print()


main()
"""
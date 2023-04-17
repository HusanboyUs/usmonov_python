
# задача 1

'''Составить алгоритм: если введенное число больше 7, то вывести 'Привет' '''

try:
    user_num=int(input("Hello, please enter your lucky number: "))
    num_checker = lambda number: "Привет" if number > 7 else 'Your number is less than 7'
    result = num_checker(user_num)
    print(result)
    
except ValueError:
    print('Please check your input!')    
 

# задача 2

'''
Составить алгоритм: если введенное имя совпадает
с Вячеслав, то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"
'''
username=input('Hello, what is your name? ')
def checkName(name):
    if name in ['Вячеслав','вячеслав']:
        print('Привет, {}'.format(name))
    else:
        print('Нет такого имени')
        #input is wrong
myfunction=checkName(username)        



# задача 3
'''
Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
'''

user_numbers=list(input('Please enter your sequential numbers: '))
result=[]

def num_multiples(numbers):
    for nums in numbers:
        if int(nums) % 3==0:
            result.append(nums)
        else:
            print(f'{nums}- canot not multiple evenly to 3')    
       
        
myfunction=num_multiples(user_numbers)
print(f'Dividable numbers are : {result}')
        

n = int(input('Enter The Number : '))
sum = 0
order = len(str(n))
copy_n = n
while(n>0):
    digit = n%10
    sum += digit **order
    n = n//10
if(sum == copy_n):
    print(f"{copy_n} is an Amstrong Number")
else:
    print(f"{copy_n} is not an Amstong Number")

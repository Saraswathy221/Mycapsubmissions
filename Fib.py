Fn = int(input("No.of terms :"))

n1, n2 = 0, 1
count = 0

if Fn <= 0:
   print("Enter a positive integer")
elif Fn == 1:
   print("Fibonacci sequence upto",Fn,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < Fn:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1

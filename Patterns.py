"""
Pattern 1

*****
*****
*****
*****
*****

"""

# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

"""
Pattern 2

*
**
***
****
*****

"""
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()

"""
Pattern 3

1
12
123
1234
12345

"""
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     print()

"""
Pattern 4

1
22
333
4444
55555

"""
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1, end='')
#     print()

"""
Pattern 5

*****
****
***
**
*

"""
# n=5
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()


"""
Pattern 6

54321
4321
321
21
1

"""
# n=5
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()


"""
Pattern 7

    *    
   ***   
  *****  
 ******* 
*********

"""
# n=5
# for i in range(0,n):
#     for j in range(n-i-1, 0, -1):
#         print(' ', end='')
#     for k in range(i*2+1):
#         print('*', end='')
#     for l in range(n-i-1, 0, -1):
#         print(' ', end='')
#     print()

"""
Pattern 8

*********
 ******* 
  *****  
   ***   
    * 
    
"""
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i, 0, -1):
#         print(' ', end='')
#     for k in range(i*2-1):
#         print('*', end='')
#     for l in range(n-i, 0, -1):
#         print(' ', end='')
#     print()


""" 
Pattern 9

    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    * 

"""
# n=5
# for i in range(0,n):
#     for j in range(n-i-1, 0, -1):
#         print(' ', end='')
#     for k in range(i*2+1):
#         print('*', end='')
#     for l in range(n-i-1, 0, -1):
#         print(' ', end='')
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i, 0, -1):
#         print(' ', end='')
#     for k in range(i*2-1):
#         print('*', end='')
#     for l in range(n-i, 0, -1):
#         print(' ', end='')
#     print()


"""
Pattern 10

*
**
***
****
*****
****
***
**
*

"""
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print('*', end='')
#     print()
# for i in range(n-1, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()

"""
Pattern 11 

1
10
101
1010
10101

"""
# n=5
# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(p, end='')
#         p = 1-p
#     print()

"""
Pattern 12 

1      1
12    21
123  321
12344321

"""
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     for k in range((n-i-1)*2,0,-1):
#         print(' ',end='')
#     for j in range(i+1,0,-1):
#         print(j, end='')
#     print()


"""
Pattern 14

A 
A B 
A B C 
A B C D 
A B C D E 

"""
# n=5
# for i in range(1,n+1):
#     num=65
#     for j in range(i):
#         print(chr(num), end=' ')
#         num+=1
#     print()

"""
Pattern 15

A B C D E 
A B C D 
A B C 
A B 
A

"""
# n=5
# for i in range(n):
#     num=65
#     for j in range(n-i):
#         print(chr(num), end=' ')
#         num+=1
#     print()

"""
Pattern 16

A 
B B 
C C C 
D D D D 
E E E E E

"""
# n=5
# num=65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(num), end=' ')
#     num+=1
#     print()


"""
Pattern 17 

    A
   ABA
  ABCAB
 ABCDABC
ABCDEABCD

"""
# n=5
# for i in range(0,n):
#     num=65
#     for j in range(n-i-1, 0, -1):
#         print(' ', end='')
#     for k in range(i+1):
#         print(chr(num), end='')
#         num+=1
#     for l in range(i):
#         print(chr(65+l), end='')
#     print()


"""
Pattern 18 

E
DE
CDE
BCDE
ABCDE

"""
# n=5
# num = 65 + n -1
# for i in range(n):
#     for j in range(num-i, num+1):
#         print(chr(j), end='')
#     print()


"""
Pattern 19

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print('*', end='')
#     for k in range(i*2):
#         print(' ',end='')
#     for j in range(n-i,0,-1):
#         print('*', end='')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     for k in range((n-i-1)*2,0,-1):
#         print(' ',end='')
#     for j in range(i+1,0,-1):
#         print('*', end='')
#     print()


"""
Pattern 20

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     for k in range((n-i-1)*2,0,-1):
#         print(' ',end='')
#     for j in range(i+1,0,-1):
#         print('*', end='')
#     print()
# for i in range(1,n):
#     for j in range(n-i):
#         print('*', end='')
#     for k in range(i*2):
#         print(' ',end='')
#     for j in range(n-i,0,-1):
#         print('*', end='')
#     print()

"""
Pattern 21

****
*  *
*  *
****

"""
# n=4
# for i in range(n):
#     for j in range(n):
#         if i!=0 and i!=n-1 and j!=0 and j!=n-1 :
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

"""
Pattern 22

4444444
4333334
4322234
4321234
4322234
4333334
4444444

"""
# num=4
# n = num*2-1
# for i in range(n):
#     for j in range(n):
#         mindis = min(j-0, i-0, n-i-1, n-j-1)
#         print(num-mindis, end='')
#     print()

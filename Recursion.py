#task-1 #summer23
# def  sum(n):
#   if n<10:
#     return n
#   else:
#     return n%10 + sum(n/10)
# print(sum(126))


#task-2
# def bunny_ears(a):
#     if a==0:
#         return 0
#     else:
#         if a%2==1:
#             return 2 + bunny_ears(a-1)
#         if a%2==0:
#             return 3 + bunny_ears(a-1)
# print(bunny_ears(1))

#task-3
# def count(a):
#     if a<10:
#         if a==7:
#             return 1
#         else:
#             return 0
#     else:
#         if a%10==7:
#             return 1 + count(a//10)
#         else:
#             return count(a//10)
# print(count(71778787878))


#task-4
# def countX(a):
#     if a=='':
#         return 0
#     else:        
#         if a[0]=='x':
#             return 1 + countX(a[1::])
#         else:
#             return countX(a[1::])
# print(countX('hi'))

# #task-5
# def changePi(a):
#     if a=='':
#         return ''
#     if len(a)==1:
#         return a[:1:]
#     else:
#         if a[0]=='p' and a[1]=='i':
#             return'3.14' + changePi(a[2::])
#         else:
#             return a[:1:] + changePi(a[1::])
# print(changePi('xpi'))

#task-6
# def arr11(a,b):
#     if len(a)==0:
#         return b
#     else:
#         if a[0]==11:
#             return arr11(a[1::],b+1)
#         else:
#             return  arr11(a[1::],b)
    
    
# print(arr11([11,1],0))


#task-7
# def pairstar(a):
#     if len(a)==1:
#         return a[0]
#     else:
#         if a[0]==a[1]:
#             return a[0] + '*' + a[1] +pairstar(a[2::])
#         else:
            
#             return a[0] + pairstar(a[1::])


# print(pairstar('hello'))

#task-8
# def countAbc(a):
#     if len(a) <3:
#         return 0
#     else:
#         if a[0]=='a'and a[1]=='b' and a[2]=='c' or a[2]=='a':
#             return 1+ countAbc(a[3::])
#         else:
#             return countAbc(a[1::])
# print(countAbc("abcxxaba"))

#task-9
#same problem as the previous one


#task-10
#same problem as the previous one

#task-11
# def bunnyEars(bunnies):
#     if bunnies == 0:
#         return 0
#     else:
#         return 2 + bunnyEars(bunnies - 1)


# print(bunnyEars(2))  



#task-12

# def tri(a):
#     if a==0:
#         return 0
#     else:
#         return a + tri(a-1)
# print(tri(5))

# task-13
# def noX(a):
#     if a=='':
#         return ''
#     else:
#         if a[0]=='x':
#             return noX(a[1::])
#         else:
#             return a[0] + noX(a[1::])
# print(noX('xxxxa'))



#task-14
# def array220(nums, index):

#     if index >= len(nums) - 1:
#         return False
#     if nums[index] * 10 == nums[index + 1]:
#         return True
#     else:

#         return array220(nums, index + 1)

# print(array220([1, 2, 20], 0))  
# print(array220([3, 30], 0))     
# print(array220([3], 0))         


#task-15
def end(a):
    if a=='':
        return ''
    else:
        if a[0]=='x':
            return a[0]

print('hello test')


def changeme(su) :
    print('su =', su)
    su = su+100

num=5
changeme(num)
print ('num =%d' %num)


def changem(mylist):
    mylist[0]=100
    
origin_list =[1,2,3,4,5]
print( 'Before change list = ', origin_list)
changem(origin_list)
print(" After change list = ", origin_list)


### Dictionary
def changeme(student):
		student['age']=55
		


student = {
    'name': '한지민',
    'age'  : 25,
    'address' : '서울시 강남구 역삼동'
}

print( student)
student['age']=35
print (student)
changeme(student)
print(student)
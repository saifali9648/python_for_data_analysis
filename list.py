#what is list 
    #list is container that are used to store a list of values of any types
# -->list is a mutable type i.e  we can change the value in place without creating 
#fesh list

#list is a type of sequence like tuple and string but it differ them in the way that 
# list are mutable but string and tuple are not it means (immutable)


#list are creating using square bracket []
#   []        empty list
#   [1,2,3]   list of integer
#   [1,19, 13.3, 100.4]   list of interge and float
#   ["apple","banana","kela"]   list of string
#   ["A","B","C"]   LIST OF CHARACTERS

#TO CRATE A LIST THE FOLLOWING SYNTAX WE NEED TO FLLOW:
   # --->  ListName=[] or
    # --->  ListName=[value1, value2, value3, ......]

 # ---> for example

#   CREATE A LIST OF FAMILY

family=["father","mother","bro","sis"]
print(family)

#CREATE A LIST OF STUDENT THAT CONTAIN THE SI.NO, NAME, CLASS, ROLL

student=["si","student_name","class","roll"]
student2=[1,"saif","post_graduation",1322703]

# HOW TO CEATE NESTED LIST

#create a student list that contain a student multiple mobile no

studentwithmobile=["si","student_name",["mobile1,mobile2"],"class","roll"]

student2withmobile=[1,"saif",["620316838","7050805032"],"post_graduation",1322703]

#HOW TO ACCESS LIST

print(student[1])
print(student2withmobile[2][0])











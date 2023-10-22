# if you can write print(name) so must provide variable then they can provide error at a run time 
#without variable print name
print("name")
# with variable print name first we can 
name = "Muhammad Shafique" 
print(name)
# in which string boundaries we can use in python
# 'single quote',"Double quote"
# '''Triple Single quote''' , """Triple Double quote""".


#   'Single quote'
name1 : str = "Samina Shafique"
print(type(name1))
print(name1)


#   "Double quote"
name2 : str = "Ahba Shafique"
print(type(name2))
print(name2)


#   '''Triple Single quote'''
name3 : str = "Aliza Shafique"
print(type(name3))
print(name3)


#   """Triple Double quote"""
name4 : str = "Ahtasham Shafique"
print(type(name4))
print(name4)


# in which boundaries string not used in python used in python
# `Backtick quote`

#name5 : str = `Abtahi Anjum`
#print(type(name))
#print(name)

# if you can print a name such  as
# message : str = 'Student Card /n father\'s name'
# then print cannot be run because of the 'single quote' cannot be used in full line 
# because of this is the the single quote cannot be used in two or more times 
# but it can be used in one time only.

# true code 

message : str = " PIAIC Student Card \n father name's "

# Convert any Special character Symbol into  Simple character. so error resolve of line 44.

message : str = 'PIAIC Student Card \nFather\'s Name'
print(message)

# For Adding any two String or variable 

# addition of two string
#.e.g:
"a" + "b"

#addition of two variables
#.e.g:

# False Code
# in this program the error is we cannot use addition of two variable of 
#  "string" + 123
# because the type of both side must be same otherwise an error will occur.

# True Code 

# here we add  string and string 
n1 : str = "A"
n2 : str = "S"
n : str = n1 + n2
print(n)


# here we add integer and integer
n3 : int = 1
n4 : int = 2
n : int = n3 + n4
print(n)


# False Code

#name6 : str = "AHTASHAM SHAFIQUE"
#fname : str = "MUHAMMAD SAHAFIQUE"
#age : int = 15
#education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
#phone : int = +923289497755
#nationality : str = "Pakistan"
#address : str = "Lahore, Pakistan"
#quater : str = "Q2"
#card : str = "PIAIC Student Card \nStudent Name: "+ name6 + "/nFather Name: "+ fname + "/nAge: " + age + "\nEducation: " + education + "/n Nationality:" + nationality + "/nPhone: " + phone + "\n Address: " + address + "\nQuater: " + quater
#print(card)


# true code 


name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str = "15"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str = "+923289497755"
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"
card : str = "PIAIC Student Card \nStudent Name: "+ name6 + "\nFather Name: "+ fname + "\nAge: " + age + "\nEducation: " + education + "\nNationality:" + nationality + "\nPhone: " + phone + "\nAddress: " + address + "\nQuater: " + quater
print(card)

#                          OR
print("OR")
# Same as a first code but differencr in line 3,5

ame6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str(15)
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str(+923289497755)
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"
card : str = "PIAIC Student Card \nStudent Name: "+ name6 + "\nFather Name: "+ fname + "\nAge: " + age + "\nEducation: " + education + "\nNationality:" + nationality + "\nPhone: " + phone + "\nAddress: " + address + "\nQuater: " + quater
print(card)

# For Continue line 
# .e.g:
print(8 +\
      2 + \
        4) 

# Second .e.g:

name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str = "15"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str = "+923289497755"
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"
card : str = "PIAIC Student Card \nStudent Name: "+ name6 +\
      "\nFather Name: "+ fname + "\nAge: " + age + "\nEducation: " + education +\
     "\nNationality:" + nationality + "\nPhone: " + phone +\
     "\nAddress: " + address + "\nQuater: " + quater
print(card)


# For simple line
# .e.g:
print(8 + 2 + 4)

# Define Multiline String """ """,''' '''

name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str = "15"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str = "+923289497755"
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"
card : str = """
PIAIC Student Card 
Student Name:
Father Name:
Age:
Education:
Nationality:
Phone:
Address:
Quater:
"""
print(card)


# F-String Powerful Feauture of Python

# First Method 

name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str = "15"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str = "+923289497755"
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"
card : str = f"""
PIAIC Student Card 
Student Name: {name6}
Father's Name: {fname}
Age: {age}
Education: {education}
Nationality: {nationality}
Phone: {phone}
Address: {address}
Quater: {quater}
"""
print(card)

# Fstring & Jinja Style

#F-string
f'''
Student Name {name6}
'''

#Jinja Style
'''
Student Name {{name6}}
'''

# F-String Second Method

name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
age : int = 15


card : str = f"""
PIAIC Student Card
Student Name : %s
Father's Name: %s
Age: %d
Education : %s

""" % (name6, fname, age, education)

print(card)


#    METHOD OF STRING

dir(str)

#     METHOD OF STRING

[i for i in dir(str) if "__" not in i]


# use string method

# such method of string  are : capitalize, lower

name : str = "MuHaMMaD ShAfIqUe"
print(name.capitalize())
print(name.lower())
# and use  other method in  upper 

# such method of string  are : format 

a = 1
# {} Place Holder
# In Computer a value is 
#              0                                                                0
'Pakistan  is {} of the most famous and powerful country in the world. '.format(a)

# False Code
name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
age : int = 15

card : str = """
PIAIC Student Card
Student Name : {}
Father's Name: {}
Age: {}
Education : {}
""".format(age, name6, education, fname)
print(card)

# True Code
 
 # 1
name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
age : int = 15


card : str = """
PIAIC Student Card
Student Name : {0}
Father's Name: {1}
Age: {2}
Education : {3}

""".format(name6,fname, age, education)
#            0     1     2      3
print(card)

 #2
name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
age : int = 15


card : str = """
PIAIC Student Card
Student Name : {1}
Father's Name: {3}
Age: {0}
Education : {2}

""".format(age, name6, education, fname)
#           0     1       2         3
print(card)

 #3
name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
age : int = 15


card : str = """
PIAIC Student Card
Student Name : {a}
Father's Name: {b}
Age: {c}
Education : {d}

""".format(a=name6, b=fname, c=age, d=education)

print(card)



# Recommended below two f-string format

name6 : str = "AHTASHAM SHAFIQUE"
fname : str = "MUHAMMAD SAHAFIQUE"
age : str = "15"
education : str = "DAE(Diploma of Associate Engineering Auto & Diesel)"
phone : str = "+923289497755"
nationality : str = "Pakistan"
address : str = "Lahore, Pakistan"
quater : str = "Q2"

card : str = f"""
PIAIC Student Card 
Student Name: {name6}
Father's Name: {fname}
Age: {age}
Education: {education}
Nationality: {nationality}
Phone: {phone}
Address: {address}
Quater: {quater}
"""
print(card)
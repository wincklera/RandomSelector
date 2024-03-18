# this will be my first real project 
from random import choice 

#list of possible first projects 
projects = input('Enter all projects seperated by space ')
project_list = projects.split("/")

print('\n')

print(choice(project_list))
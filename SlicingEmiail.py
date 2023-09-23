# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:23:24 2023
@author: segal
"""
# email slicer address:
# get users email
email= input("What is ur email address?: ").strip()
# slice out user name
user= email[:email.index("@")]

# slice out the domain name:
domain = email[email.index("@")+1:]

# formate the message
output = "Your username is {} and your domainName is {}".format(user,domain)
# display th output message:
print(output)
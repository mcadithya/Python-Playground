import re

pf_number = input("enter your PF Number : ")

pattern  = "(UK|AP|NE|BR|CG|SR|D|LGA|GJ|HP|JH|KD|VD|BG|MH|MP|OR|PB|HO|RJ|TH|TN|UP|WB|KR|DS|GN|LD|MR|GR|NZ|KN|GB|PY|MD|CB|TB|JL|NG|PU|AN|AP|AR|AS|BH|CG|CH|DD|DN|GA|GJ|HP|HR|JK|JR|KL|KN|LD|MG|MH|MP|MZ|N|LOR|PB|PN|RJ|SK|TN|TR|UC|UP|WB)/[A-Z]{3}/[0-9]{7}/(000)/[0-9]{7}"

matches  =  re.fullmatch(pattern,pf_number)

if matches:

    print("valid PF number")

else:

    print("not valid")

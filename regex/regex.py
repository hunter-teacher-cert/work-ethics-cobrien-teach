import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)
def find_name(line):
    pattern = r"(?:Dr\.|Mr\.|Mrs\.|Ms\.|Prof\.|Sr\.|[A-Z][a-z]+)\s(?!(?:Care|Doctor|History|Psych|Electric|Behavior|Power|Use|Hospital|Diagnosis))[A-Z][a-z]+"
    result = re.findall(pattern,line)
    return result
f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

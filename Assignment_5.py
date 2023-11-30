'''
Name:Chandre Dipali Ravindra
RollNo:13 
Batch: B1 
Program: Regular Expression in Python
''' 
import re
regex = (r"[A-Z]{5}[0-9]{4}[A-Z]{1}\n"
r"\b\d{1,3}\.\d{1,3}\.\d{1,2}\.\d{1,1}\n"
r"\d{1,2}\/\d{1,2}\/\d{2,4}\n"
r"[A-z]{6}[A-z]{8}[A-z]{3}")
test_str = ("BCBPH8858M\n"
"192.168.52.1\n"
"22/11/2023\n"
"DipaliRavindreChandre")
matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
  print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum =matchNum, start = match.start(), end = match.end(), match = match.group()))
for groupNum in range(0, len(match.groups())):
  groupNum = groupNum + 1
  print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum =groupNum, start = match.start(groupNum), end = match.end(groupNum), group =match.group(groupNum)))

#OUTPUT:
'''
Match 1 was found at 0-52: BCBPH8858M
192.168.52.1
22/11/2023
DipaliRavindreCha
'''

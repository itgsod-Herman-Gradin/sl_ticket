def fares(age,child=False, student=False, senior=False):
   if child or student or senior:
       return 'Halv'
   else:
       if age < 18 or age > 65:
           return 'Halv'
       else:
           return 'Hel'









print 'barn 10' ,fares(10)
print 'pensionar 65' ,fares(66)
print 'sjukpensionar' ,fares(47,senior=True)
print 'student 25' ,fares(25,student=True)
print 'vuxen 45' ,fares(45)

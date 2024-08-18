'''Clostridium pasteurianum DSM 525(type of bacteria) data taken from NCBI database.
why to analyze g-c content in a DNA sequencing also why dna sequencing?
Example1:In polymerase chain reaction (PCR) experiments( PCR is a method widely used to make millions to 
billions of copies of a specific DNA sample rapidly.This technique involves heating DNA at a specific temp.), the GC-content of short oligonucleotides known as primers is often used to 
predict their annealing temperature to the template DNA. A higher GC-content level indicates a relatively 
higher melting temperature.
Example2:To check the accuracy DNA between two people ,to check if they are related.
'''


file=open('NR1.txt',mode='r')

g=0
a=0
t=0
c=0

file.readline()

for line in file:
    line=line.lower()
    for char in line:
        if char=='g':
          g+=1
        elif char=='c':
           c+=1
        elif char=='t':
           t+=1
        elif char=='a':
           a+=1 

print(str(g)+" : Guanine")  
print(str(t)+" : Thymine")  
print(str(c)+" : Cytosine")  
print(str(a)+" : Adenine")        

gc_ratio=(g+c)/(g+c+a+t)

print(gc_ratio)

at_ratio=(a+t)/(g+c+a+t)

print(at_ratio)


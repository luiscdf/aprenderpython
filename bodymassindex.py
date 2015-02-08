#simple Body mass index calculator

name = raw_input("What is your name?")
#gostava de por aqui o nome!!
height = raw_input("Your Height (in Metric) is?")
weight = raw_input("Your weight (in Kg) is?")
bmi = (float(weight) / (float(height)**2))
print name + "your body mass index is: " + str(bmi)

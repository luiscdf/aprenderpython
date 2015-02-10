print "Hello there! I am a Simple Python program that will help you to calculate your Body mass index. in order to do that i need to ask you some questions..."
print " "

#data colect
name = raw_input("What is your name? ")
height = raw_input("Your Height (in Metric) is? ")
weight = raw_input("Your weight (in Kg) is? ")

#math bmi
bmi = (float(weight) / (float(height)**2))

# BMI table 
if bmi < 15.0:
    diag = "Very severely underweight"
elif bmi >= 15.0 and bmi < 16.0:
    diag = "Severely underweight"
elif bmi >= 16.0 and bmi < 18.5:
    diag = "Underweight"
elif bmi >= 18.5 and bmi < 25.0:
    diag = "Normal (healthy weight)"
elif bmi >= 25.0 and bmi < 30.0:
    diag = "Overweight"
elif bmi >= 30.0 and bmi < 35.0:
    diag = "Obese Class I (Moderately obese)"
elif bmi >= 35.0 and bmi < 40.0:
    diag = "Obese Class II (Severely obese)"
elif bmi >= 40.0 and bmi < 100.0:
    diag = "Obese Class III (Very severely obese)"
    
#output
print " "
print name + ", your body mass index is:" , bmi
print " "
print "According to (http://en.wikipedia.org/wiki/Body_mass_index) Your are: " + diag
print " "
closeInput = raw_input("Press ENTER to exit")
print "Closing..."

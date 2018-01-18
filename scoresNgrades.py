from random import randint

# random_num=random.random()
# random_num=random.randint(60,100)
# the random function will return a floating point number, that is 0.0<=random_num<1.0 , or use:
# random_num=random.randint()

# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
def marks():
	print 'Scores and Grades'
	for i in range(0,10):
		x=randint(60,100)
		if x <= 69:
			print 'Score:',x,'; Your grade is','D'
		elif x <= 79:
			print 'Score:',x,'; Your grade is','C'
		elif x <= 89:
			print 'Score:',x,'; Your grade is','B'
		else:
			print 'Score:',x,'; Your grade is','A'
	print "End of the program. Byyyye!"

marks()

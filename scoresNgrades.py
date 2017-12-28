import random

random_num=random.random()
random_num=random.randint(60,100)

def marks(int):
	print 'Scores and Grades'
	print random.randint(60,100)
	for i in range(60,100):
		if i <= 69:
			print 'Score:',i,'Your grade is','D'
		elif i <= 79:
			print 'Score:',i,'Your grade is','C'
		elif i <= 89:
			print 'Score:',i,'Your grade is','B'
		else:
			print 'Score:',i,'Your grade is','A'

marks(int)

	# the random function will return a floating point number, that is 0.0<=random_num<1.0 , or use:
	# random_num=random.randint()

# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
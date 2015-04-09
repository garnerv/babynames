#  File: BabyNames.py 

#  Description: program that will allow user to query a dictionary of the most popular baby names over the past 11 decades

#  Student Name: Garner Vincent

#  Student UT EID: GV4353

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3-10-15

#  Date Last Modified: 3-12-15

#option 1
def nameSearch(babyNames, name):
	name = name.capitalize()

	if name in babyNames:
		#calculate decade
		highNum = 1001
		highDex = 0
		posCount = 0
		for val in babyNames[name]:
			if val < highNum:
				highNum = val
				highDex = posCount
			posCount += 1

		decade = highDex * 10 + 1900

		return '\nThe matches with their highest ranking decade are:\n' + name + ' ' + str(decade) + '\n'
	else:
		return name + ' does not appear in any decade.'

#part of option 2
def printYearVal(printLst):
	decade = 1900
	printLst = printLst.split()
	for item in printLst:
		print(str(decade) + ': ' + str(item))
		decade += 10

#option 2
def valPrint(babyNames, name):
	name = name.capitalize()

	if name in babyNames:
		#convert the values list of integers into a string for printing
		printLst = []
		for val in babyNames[name]:
			if val == 1001:
				printLst.append(0)
			else:
				printLst.append(val)

		printLst = ' '.join(str(e) for e in printLst)


		nameString = name + ': ' + printLst 
		print('\n' + nameString)
		yearString = printYearVal(printLst) 

		return ''
	else:
		return name + ' does not appear in any decade.'

#option 3
def particularDecade(babyNames, decade):
	names = []
	hits = 0
	idx = int(decade % 100 / 10)
	for key in babyNames:
		for val in babyNames[key]:
			if val < 1001:
				hits += 1
		if (babyNames[key][idx] < 1001) and hits == 1:
			names.append(key)
		hits = 0

	names = sorted(names)
	return names

#option 4
def allNames(babyNames):
	names = []
	for key in babyNames:
		rankInAll = 0
		for val in babyNames[key]:
			if val < 1001:
				rankInAll += 1
		if rankInAll == 11:
			names.append(key)
	names = sorted(names)
	return names

#option 5
def increasinglyPopular(babyNames):
	names = []
	idx = 0
	for key in babyNames:
		for i in range(len(babyNames[key]) - 1):
			if babyNames[key][i] <= babyNames[key][i + 1]:
				break
			#if loop makes it without breaking, add the name to the list
			if i == (len(babyNames[key]) - 2):
				names.append(key)

	names = sorted(names)
	return names

#option6
def decreasinglyPopular(babyNames):
	names = []
	idx = 0
	for key in babyNames:
		for i in range(len(babyNames[key]) - 1):
			if babyNames[key][i] >= babyNames[key][i + 1]:
				break
			#if loop makes it without breaking, add the name to the list
			if i == (len(babyNames[key]) - 2):
				names.append(key)

	names = sorted(names)
	return names

def main():
	#import database
	inFile = open('./names.txt')

	#create babyNames dictionary
	babyNames = {}

	#add keys and values to dictionary
	for line in inFile:
		lst = line.strip().split()
		for i in range(1, len(lst)):
			lst[i] = int(lst[i])
			#change zero to 1001 for mathematial operation reasons
			if lst[i] == 0:
				lst[i] = 1001
		#assign key to the baby name, rankings to value as a list
		for item in lst:
			babyNames[lst[0]] = lst[1:]

	inFile.close()

	#make menu
	menu = 'Options:\n' + 'Enter 1 to search for names.\n' + 'Enter 2 to display data for one name.\n' + 'Enter 3 to display all names that appear in only one decade\n' \
	+ 'Enter 4 to display all names that appear in all decades.\n' + 'Enter 5 to display all names that are more popular in every decade.\n' + 'Enter 6 to display all names that are less popular in every decade.\n' \
	+ 'Enter 7 to quit.\n'

	#menu for query
	while True:
		print(menu)
		choice = input('Enter choice: ')
		intChoice = False
		#try converting the choice into an integer if possible; then the choice is valid
		while not (intChoice):
			try:
				choice = int(choice)
				while not (1 <= choice <= 7):
					choice = input('Enter a valid choice: ')
				intChoice = True

			except:
				choice = input ('Enter a valid choice: ')

		#validate menu choices

		#determine if a name is in the dataset, return most popular decade if true
		if choice == 1:
			name = input('Enter a name: ')
			print(nameSearch(babyNames, name))

		#rankings for a given name
		elif choice == 2:
			name = input('Enter a name: ')
			print(valPrint(babyNames, name))
		
		#names that are popular in only one decade
		elif choice == 3:
			decade = input('Enter a decade: ')

			#validate the decade as being both an integer and a proper decade
			decadeValid = False
			while not decadeValid:
				try:
					decade = int(decade)
					while ((decade != 1900) and (decade != 1910) and (decade != 1920) and (decade != 1930) and (decade != 1940) and (decade != 1950) and (decade != 1960) and (decade != 1970) and (decade != 1980) and (decade != 1990) and (decade != 2000)):
						decade = input('Enter a valid decade: ')
					decadeValid = True
				except:
					decade = input('Enter a valid decade: ')
			#run decade to print baby names which solely appear in that decade
			oneDecadeNames = particularDecade(babyNames, decade)
			print('The names are in alphabetical:')
			for name in oneDecadeNames:
				print(name)
			print()

		#names that are popular in every decade
		elif choice == 4:
			popularAll = allNames(babyNames)
			print(str(len(popularAll)) + " names appear in every decade. The names are: ")
			for name in popularAll:
				print(name)
			print()

		#names that are more popular in every decade
		elif choice == 5:
			incPop = increasinglyPopular(babyNames)
			print(str(len(incPop)) + " names are more popular in every decade.")
			for name in incPop:
				print(name)
			print()
	
		#names that are less popular in every decade
		elif choice == 6:
			decPop = decreasinglyPopular(babyNames)
			print(str(len(decPop)) + " names are less popular in every decade." )
			for name in decPop:
				print(name)
			print()

		#terminate program option
		elif choice == 7:
			print('Goodbye.')
			break


main()

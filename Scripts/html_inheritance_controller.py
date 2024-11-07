"""""
import aspose.words as aw

doc = aw.Document("base.html")
builder = aw.DocumentBuilder(doc)

# Insert text at the beginning of the document.
builder.move_to_document_start()
builder.writeln("Morbi enim nunc faucibus a.")

doc.save("Output.html")
"""

"""""
File_object = open("../../base.html","r+")
print(File_object.readlines())
File_object.write("JOHN")
"""

"""""
# using with statement
with open('../../base.html','r+') as file:
    for line in file:
        line = 'hello world !'
"""


# THIS IS HOW WE READ AND WRITE TO FILES
"""""
with open('../../base.html', 'r', encoding='utf-8') as file: 
	data = file.readlines() 

print(data) 

for i in range(len(data)):
	if data[i] == 'Old text\n':
		data[i] = 'New text\n'
	print(data[i])
print(data)


with open('../../base.html', 'w', encoding='utf-8') as file: 
	file.writelines(data) 
    """



### TO DO:
# MAKE CODE GENERAL SOLUTION FOR ALL HTML FILES IN FOLDER



# CODE START ---------------------------------------------------------------------- CODE START
import os
# Open base file and save contents in list ---------------------------------------------------
with open('base.html', 'r', encoding='utf-8') as file: 
	data = file.readlines() 
	
sectionNames = []           # names of found sections
sectionStart = 0            # line the current section started at
currentSection = "-1"       # name of current section

sectionData = []            # the data (html lines) in current section
sectionsDict = {}           # dictionary connecting section names and section code

# Iterate list of content 
for i in range(len(data)):
	# Look for the end of started sections (after a section start has already been detected)
	if data[i].replace("<!--BASE_","").replace("-->\n","").strip() == currentSection:
		# iterate lines in section and add to sectionData
		for j in range(i-sectionStart-1):
			sectionData.append(data[sectionStart+j+1])
		# add entry to dictinary
		sectionsDict[currentSection] = sectionData
		# empty sectionData. So ready for reuse
		sectionData = []

	# Look for base sections
	if "<!--BASE" in data[i]:
		# get name of section (from within html comment line)
		sectionNames.append(data[i].replace("<!--BASE_","").replace("-->\n","").strip())
		sectionStart = i
		currentSection = sectionNames[len(sectionNames)-1]



# start writing to non-base files -----------------------------------------------------------------------
# iterate through all html files
for webpage in os.listdir():
	if('.html' in webpage and webpage != 'base.html'):
		with open(webpage, 'r', encoding='utf-8') as file: 
    		# Reuse data element
			data = file.readlines() 

			data.append('\n')

			outOfSpace = False          # Are we out of space in old code? Insert instead of replacing
			newCodeLenght = 0           # Length of newly added code (so we don't calculate the list length over and over)
			doneUpdating = False		# Signify we are done updating and need to just delete lines now

			for section in sectionsDict:
				for i in range(len(data)):
					if i != 0 and data[i-1].replace("<!--","").replace("-->\n","").strip() == section:
						# In valid section to be updated
						# Start replacing with new code line by line
						newCodeLenght = len(sectionsDict[section])
						for j in range(newCodeLenght):
							if(outOfSpace):
								# insert new line
								data.insert(i+j,sectionsDict[section][j])
							else:
								# replace old line with new line
								data[i+j] = sectionsDict[section][j]
								
								# found end of section, start replacing
								if(section in data[i+j+1] and '<!--' in data[i+j+1]):
									outOfSpace = True
								
						
						# Already out of space? Finish up
						if(outOfSpace):
							# go to next section
							outOfSpace = False
							break
						
						doneUpdating = True
						# Not out of space? Remove rest of lines
					
					if(doneUpdating):
						"""if(section in data[i+newCodeLenght+1] and '<!--' in data[i+newCodeLenght+1]):
							data.pop(i+newCodeLenght)
							break"""
						data.pop(i+newCodeLenght)
						if((section in data[i+newCodeLenght+1] and '<!--' in data[i+newCodeLenght+1]) or ((section in data[i+newCodeLenght] and '<!--' in data[i+newCodeLenght]))):
							break


			# Write the new data to the file
			with open(webpage, 'w', encoding='utf-8') as file: 
				file.writelines(data) 

		  



			

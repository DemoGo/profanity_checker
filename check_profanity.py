#!/usr/bin/python
import urllib
def read_text():

	file_object = open("PATH TO THE FILE")  # Give the file path on you want to apply profanity checker
	all_text = file_object.read()
	#print(all_text)
	file_object.close()
	check_profanity(all_text)


def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!")
	elif "false" in output:
			print("No curse word found...")
	else:
			print("Document not scanned properly...")

		

read_text()

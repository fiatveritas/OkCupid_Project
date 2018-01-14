#!/usr/bin/python3

def word_counter(data_source):
	"""This function is to be used to find the basic
	summary for the features of the dataset. This function
	print output."""
	dummy_list = []
	for i in data_source:
		if i not in dummy_list:
			dummy_list.append(i)

	word_count = {i : 0 for i in dummy_list}

	for i in data_source:
		word_count[i] += 1

	people = float(0)

	for i in word_count:
		people += word_count[i]

	for i in word_count:
		print('{} : {} is {:.2f}% of the dataset.'.format(i, word_count[i], 100 * word_count[i] / people))

def word_count(data_source):
	"""This function is similar to the one above
	with the difference that this one types casts
	float to str and passes entries with NaN."""
	dummy_list = []
	for i in data_source.split():
		if i not in dummy_list:
			dummy_list.append(i)

	word_count = {i : 0 for i in dummy_list}

	for i in data_source.split():
		word_count[i] += 1
	return word_count

def remove_tags(data_source):
	"""This function gets rid of most HTML tags. I did my best to come
	up with code that got rid of tags. I ran random samples from essays
	to make sure."""
	import re
	cleanr = re.compile(r'<.*/?>')
	cleanr2 = re.compile(r'<.*\s?.*>')
	cleanr3 = re.compile(r'&amp;')
	cleanr4 = re.compile(r'&lt;')
	cleanr5 = re.compile(r'&gt;')
	cleanr6 = re.compile(r'&nbsp;')
	cleanr7 = re.compile(r'\n')
	cleantext = re.sub(cleanr, ' ', data_source)
	cleantext = re.sub(cleanr2, ' ', cleantext)
	cleantext = re.sub(cleanr3, ' ', cleantext)
	cleantext = re.sub(cleanr4, ' ', cleantext)
	cleantext = re.sub(cleanr5, ' ', cleantext)
	cleantext = re.sub(cleanr6, ' ', cleantext)
	cleantext = re.sub(cleanr7, ' ', cleantext)
	return cleantext

if __name__ == '__main__':
	print('hello world!')

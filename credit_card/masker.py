import re

def mask_number(number):
	# Type cast number to a string since we'll use some string operations
	unmasked = str(number)

	# If number is empty or null or is shorter than 8 chars,
	# return the number itself
	if not unmasked or len(unmasked) < 8:
		return unmasked

	# Extract the section that needs to be masked i.e. middle segment
	unmasked_sensitive_info = unmasked[4:-4]

	# Use regular expressions to find only digits
	# and substitute each match with #
	masked_sensitive_info = re.sub(
		r'[0-9]',
		'#',
		unmasked_sensitive_info)

	# Combine the segments i.e. first four, middle segment and last_four
	first_four = unmasked[:4]
	last_four = unmasked[-4:]

	return first_four + masked_sensitive_info + last_four

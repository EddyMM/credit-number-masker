import re

def mask_number(number):
	# Type cast number to a string since we'll use some string operations
	unmasked = str(number)

	# If number is empty or null or is shorter than 8 chars,
	# return the number itself
	if not unmasked or len(unmasked) < 8:
		return unmasked

	# Use regular expressions to find only digits
	# and substitute each match with # only on the section 
	# that needs to be masked i.e. middle segment
	masked_sensitive_info = re.sub(
		r'[0-9]',
		'#',
		unmasked[4:-4])

	# Combine the segments i.e. first four, middle segment and last_four

	return unmasked[:4] + masked_sensitive_info + unmasked[-4:]

import re

def mask_number(number):
	unmasked = str(number)

	if not unmasked or len(unmasked) < 8:
		return unmasked

	unmasked_sensitive_info = unmasked[4:len(unmasked)-4]

	masked_sensitive_info = re.sub(
		r'[0-9]',
		'#',
		unmasked_sensitive_info)

	return unmasked[:4] + masked_sensitive_info + unmasked[len(unmasked)-4:]

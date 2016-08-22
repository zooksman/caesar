def alphabet_position(letter):
	letter = str(letter)
	uniletter = letter.lower()
	return int(ord(uniletter) - 97)

def rotate_character(char, rot):
	ordi = (alphabet_position(char) + int(rot)) % 26
	char = chr(ordi + 97)
	return char

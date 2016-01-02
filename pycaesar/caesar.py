# create a searchable array of a common 26-letter alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define our encryption function with two arguements: the plain text and number of letters to shift by
def encrypt(plaText, shift):
	# an empty variable to hold our encrypted text until completion
	encryptedText = ""
	# an empty variable to hold our encrypted characters which will be appended to our result
	appendLetter = ""
	# cycles through every character in our provided plain text
	for character in plaText:
		# checks if said character is a letter in the alphabet
		if character in alphabet:
			# makes the letter lowercase to ensure it stays within the alphabet array
			character = character.lower()
			# takes the current letter position and transforms it to the new encrpyted position
			currentPosition = alphabet.index(character)
			newPosition = (currentPosition + shift) % len(alphabet)
			# holds the encrpyted letter that is going into our 'encryptedText' variable
			appendLetter = alphabet[newPosition]
		# if character is NOT a letter, don't encrpyt it (e.g !@#$%^&*())
		else:
			appendLetter = character

		# appends the character to our result
		encryptedText += appendLetter
	# returns our encrypted text
	return encryptedText

# the exact same as our above function except that we negatively transform
# our encrypted text along the alphabet array instead of positively, therefore
# decrypting the text. Essentially we're encrypting our text in the the reverse order.
def decrypt(encText, shift):

	decryptedText = ""
	appendLetter = ""

	for character in encText:

		character = character.lower()

		if character in alphabet:
			currentPosition = alphabet.index(character)
			newPosition = (currentPosition - shift) % len(alphabet)
			appendLetter = alphabet[newPosition]
		else:
			appendLetter = character

		decryptedText += appendLetter

	return decryptedText

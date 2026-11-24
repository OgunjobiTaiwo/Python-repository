letter = input("Enter any word of choice: ")

vowel = 0;
consonant = 0;

for count in range(len(letter)):

	if letter[count] == 'a' or letter[count] == 'e' or letter[count] == 'i' or letter[count] == 'o' or letter[count] == 'u' :
		vowel+=1
	else:
		consonant+=1
print("Number of vowels:" , counter)
print("Number of consonants:" , consonant)
		
		








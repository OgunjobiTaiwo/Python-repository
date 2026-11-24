let letter = prompt("Enter any word of choice: ");

let vowel = 0;
let consonant = 0;

for (let count = 0 ; count < letter.length ; count++){
	if (letter.charAt(count) == 'a' || letter.charAt(count) == 'e' || letter.charAt(count) == 'i'|| letter.charAt(count) == 'o'|| letter.charAt(count) == 'u' ){
		vowel++;
	}
	else
		consonant++;
	}



}
console.log(vowel + "Vowel");
console.log(consonant + "consonants");








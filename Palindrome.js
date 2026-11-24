let letter = prompt("Enter any number: ");
let reversed = ""

for(let count = 0 ; count < letter.length ; count++){
reversed = letter[count] + reversed ;
}

if (reversed == letter){
	console.log("Palindrome");
}
else{
	console.long("Not a palindrome");
}





















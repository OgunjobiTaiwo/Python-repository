let letter = prompt("Enter a word: ");

for (let count = 0; count < letter.length; count++) {

if (count % 2 === 0) {
    console.log(letter.charAt(count));
}


}

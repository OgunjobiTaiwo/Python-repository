let targetValue = parseInt(prompt("Enter your target value:"));

let number1 = parseInt(prompt("Enter any number from 1 to 9:")); let number2 = parseInt(prompt("Enter any number from 1 to 9:")); let number3 = parseInt(prompt("Enter any number from 1 to 9:"));

let sum = 0;

for (let count = 1; count <= 3; count++) {

sum = number1 + number2 + number3;

if (sum === targetValue) {
    console.log(number1, number2, number3);
}


}

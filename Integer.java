import java.util.Scanner;
public class Integer{
	public static void main (String[] args){
	Scanner input = new Scanner(System.in);
System.out.print("Enter your target value ");
int targetValue = input.nextInt();

System.out.print("Enter any  number from 1 to 9: ");
int number1 = input.nextInt();

System.out.print("Enter any number from 1 to 9: ");
int number2 = input.nextInt();

System.out.print("Enter any number from 1 to 9: ");
int number3 = input.nextInt();

int sum = 0;
for (int count = 1 ; count <=3 ; count++){

	sum = number1 + number2 + number3;

	if (sum == targetValue){
		System.out.print(number1 + number2 + number3);
	}




}

	}
}

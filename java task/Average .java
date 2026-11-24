import java.util.Scanner;
public class Average{
	public static void main (String[] args){
	Scanner input = new Scanner(System.in);
System.out.print("Enter a number (press -1 to stop): ");
int number = input.nextInt();
int count = 0;
int total = 0;
while(number != -1){

count++;
total = total + number;

double average = total /count
System.out.print(average);
int number = input.nextInt();

import java.util.Scanner;
public class VowelConsonant{
public static void main(String[] args){
Scanner input = new Scanner(System.in);

System.out.print("Enter any word of choice: ");
String letter = input.nextLine();


int counter = 0;
int consonant = 0;
for(int count = 0 ; count < letter.length() ; count++){
	if (letter.charAt(count) == 'a' || letter.charAt(count) == 'e' || letter.charAt(count) == 'i'|| letter.charAt(count) == 'o'|| letter.charAt(count) == 'u' ){
		counter++;
		}
	else{
		consonant++;
	}
  }
	System.out.println( counter + "vowel");
	System.out.println( consonant + " Consosnant");
	}
	
}

import java.util.Scanner;
public class EvenIndex{
public static void main(String[] args){
Scanner input = new Scanner(System.in);

System.out.print("Enter a word : ");
String letter = input.nextLine();
for(int count = 0 ; count < letter.length(); count++){

	if (count % 2 == 0){
	  System.out.print(letter.charAt(count));
	}


}






























	}
}

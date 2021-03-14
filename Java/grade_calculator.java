package grade_calculator;
import java.util.Scanner; //Scanner to get user input
/**
 * Program grade_calculator.java - Calculate QQI Grade
 * Date 09/01/2019
 * @author EyeCode4You
 */
public class grade_calculator{
    public static void main(String[] args) {     
        try (Scanner in = new Scanner(System.in)) {
			String Desc = "This program will convert given QQI results into Fail,\n"
			        + "Pass, Merit, and Distinction Status based on score achieved in \n"
			        + "Skill Demonstrations (60%) and the Theory Test (40%)\n"
			        + "________________________________________________________________";
			
			String grade = null; //Used for displaying result status.
			
			//Variables for getting results and computing the result.
			double skillDemo = 0, theoryTest = 0, result = 0;
			
			System.out.print("\n"+Desc);
			
			do{
				//Prompt for Skills demo results while input<0 or >60.
				System.out.print("\n\nEnter Total Marks For SKILLS DEMONSTRATIONS : ");
				skillDemo = in.nextDouble();
			}while(skillDemo < 0 || skillDemo > 60);
			
			do{
				//Prompt for theory test results while input<0 or >40.
				System.out.print("Enter Total Marks For THEORY TEST : ");
				theoryTest = in.nextDouble();
			}while(theoryTest < 0 || theoryTest > 40);
			
			result = skillDemo + theoryTest;

			if(result < 50){grade = "Unsuccessful";
			}else if(result < 65){grade = "Pass";
			}else if(result < 80){grade = "Merit";
			}else {grade = "Distinction";}
			
			System.out.print("\nThe total result for the grade is : "+
			result+"%" + "\nThe Grade Of The Result Is : "+grade+"\n\n");
		}catch(Exception e) {
			System.out.println("\n****Error in Input! Program Will Now Exit!****");
			System.out.println("________________________________________________");
		}
    } 
}

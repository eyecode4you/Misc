package twitter;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class twitterFuncs {
	private String tName;
	char [] validChar = {'`', '¬', '"', '£', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '\\', 
			 '|', '{', '[', '}', ']', ';', ':', '\'', '@', '#', '~', ',', '<', '.', '>', 
			 '/', '?', '€'}; //Array of valid user name chars
	private ArrayList<String> valid = new ArrayList<String>(); //Dynamic String arrays for valid and invalid names
	private ArrayList<String> invalid = new ArrayList<String>();
	String error = "";
	
	public twitterFuncs() { //Constructor
		tName = ""; //Init tName
	}
	
	public boolean check(String twitterName) {
		for(int i = 1; i < twitterName.length(); i++) { //Loop through items in twitterName
			char ch = twitterName.charAt(i);
			for(int j = 0; j < validChar.length; j++) { //Loop through items in validChar[]
				if(validChar[j] == ch) {
					return true; //Invalid character found
				}
			}
		}
		return false; //No invalid characters
	}
	//twitterFuncs METHODS
	public void addValid(String tName) { //Add valid name to addValid[]
		valid.add(tName);
	}
	public void addInvalid(String tName) { //Add invalid name to addInvalid[]
		invalid.add(tName);
		JOptionPane.showMessageDialog(null,"Invalid Twitter Username!");
	}
	public void outputInfo() { //Output valid and invalid arrays
		System.out.println("-----Valid Names-----");
		System.out.println(getValid());
		System.out.println("\n-----Invalid Names-----");
		System.out.println(getInvalid());
	}
	
	// GETTER & SETTERS
	public void setName(String tName) { //Set object tName var
		this.tName = tName;
	}
	public String getName() { //Get object tName var
		return this.tName;
	}
	public ArrayList<String> getValid() { //Return array of valid twitter names
		return this.valid;
	}
	public ArrayList<String> getInvalid() { //Return array of invalid twitter names
		return this.invalid;
	}
}

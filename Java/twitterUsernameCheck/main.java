package twitter;
import javax.swing.JOptionPane;
public class main {
	public static void main(String[] args) {
		String twitterName = " ";
		boolean flg = true; //bool for main prog execution
		String ynPrompt = ""; //Prompt for user to enter user name
		
		twitterFuncs mytFuncs = new twitterFuncs(); //Create object from class
		while(flg) {
			ynPrompt = JOptionPane.showInputDialog(null,"Input name? (y/n)");
			if(ynPrompt.equals("y")) {
					twitterName = JOptionPane.showInputDialog(null,"Enter Twitter Username (Must start with '@' and be between 5 & 16 chars)");
					mytFuncs.setName(twitterName);
					//Check validity
					if(twitterName.charAt(0) != '@' || twitterName.length() < 5 || twitterName.length() > 16) {
						mytFuncs.addInvalid(twitterName);
					}else if(mytFuncs.check(twitterName)){ //returns true if invalid char found in name
						mytFuncs.addInvalid(twitterName);
					}else {
						mytFuncs.addValid(twitterName);
					}
			}else {mytFuncs.outputInfo(); flg = false;}	//Output results and end loop
		}//End flg while
	}//End of main
}//End Class

import java.util.Scanner;
public class BankAccount
{
    String acc_holder_name;
    int acc_number;
    double acc_balance;
    
    
    public BankAccount(String acc_holder_name, int acc_number, double acc_balance) {
        this.acc_holder_name = acc_holder_name;
        this.acc_number = acc_number;
        this.acc_balance = acc_balance;
    }
     void deposit(double amount)
    {
        if(amount>0)
        {
            acc_balance+=amount;
            System.out.println("Deposit of Rs." + amount + " successful. Current balance: Rs." + this.acc_balance);

        }
        else
        {
            System.out.println("Please enter a valid denomination");
        }
    }
    
   void withdraw(double amount)
    {
        if(this.acc_balance>amount)
        {
            this.acc_balance-=amount;
            System.out.println("Withdrawal of Rs." + amount + " is successful. and Current balance left is: Rs" + this.acc_balance);

        }
        else{
            System.out.println("Insufficient Funds in your account");
        }
    }
    
     void display()
    {
        System.out.println("Account Holder name is : " + acc_holder_name);
        System.out.println("Account Number is: " + acc_number);
        System.out.println("Current Balance: Rs." + acc_balance);
    }
    
    
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	   String x =sc.next();
	    int y =sc.nextInt();
	    int z = sc.nextInt();
	    int amt= sc.nextInt();
		BankAccount ac = new BankAccount(x, y,z);
		
		//Display the account details
		ac.display();

        // Making a deposit amount
        ac.deposit(amt);
        
        //Withdrawl
        ac.withdraw(amt);
	}
}


//import java.util.Scanner;
//Scanner sc = new Scanner(System.in);

public class TestAccount {
    public static void main(String[] args){
        Account ac = new Account(1122,20000);
        System.out.println(ac.getdate());
        //ac.getMonthlyInterestRate(4.5);
        //ac.getMonthlyInterest(20000, ac.MonthlyInterestRate(4.5));
        ac.setR(4.5);
        ac.withdraw(2500);
        ac.deposity(3000);
        System.out.println(ac.getBalance());
        System.out.println(ac.getMonthlyInterest());
        //System.out.println(ac.date());
         Account ac2 = new Account();
        System.out.println(ac2.getMonthlyInterest());
        System.out.println(ac2.getdate());
     }
}

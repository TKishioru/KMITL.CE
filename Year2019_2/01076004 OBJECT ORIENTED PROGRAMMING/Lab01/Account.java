import java.util.Date;

public class Account {
    private int id;
    private double balance;
    private double annualInterestRate;
    private Date dateCreated;
    double MonthlyInterestRate;
    double MonthlyInterest;
    
    Account(){
           dateCreated = new Date();
    }
    Account(int newID,double newbalance){
        id = newID;
        balance = newbalance;
        dateCreated = new Date();

    }
    public void setR(double annualInterestRate){
        this.annualInterestRate = annualInterestRate;
    }
    /*double getMonthlyInterestRate(double annualInterestRate){
    annualInterestRate/=100;
    MonthlyInterestRate = annualInterestRate/12;
        return  MonthlyInterestRate;
    }
    double getMonthlyInterest(double balance,double MonthlyInterestRate){
    MonthlyInterest = balance * MonthlyInterestRate;
         return MonthlyInterest;
    }*/
    double getMonthlyInterest(){
        return MonthlyInterest = balance * (annualInterestRate/12/100);
    }
    double withdraw(double withd){
        balance -= withd;
         return balance;
    }
    double deposity(double depos){
        balance += depos;
         return balance;
    }
/*
    Date date(){
       dateCreated = new Date();
       return dateCreated;
    }*/

    public double getBalance() {
        return balance;
    }
    public Date getdate() {
        return dateCreated;
    }
}


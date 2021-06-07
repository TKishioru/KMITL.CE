
import java.util.ArrayList;
import java.util.Date;

public class Transactions extends NewAccount {

    private Date dateCreated;
    private char type;
    private double amount;
    private double balance;
    private double annualInterestRate;
    //private String description;

    public Transactions() {
    }

    public Transactions(char type, double amount, double balance) {
        this.type = type;
        this.amount = amount;
        this.balance = balance;

    }

    public Transactions(char type, double amount, String Name, int id, double balance, double interestRate) {
        super(Name, id, balance, interestRate);
        this.type = type;
        this.amount = amount;

    }

//    private double withdraw() {
//        if (type == 'W') {
//            balance = balance - (amount + 20);
//        }
//        return balance;
//    }
//
//    private double deposit() {
//        if (type == 'D') {
//            balance += amount;
//        }
//        return balance;
//    }

    public void setAnnualInterestRate(double annualInterestRate) {
        this.annualInterestRate = annualInterestRate;
    }

    public double getAnnualInterestRate() {
        return (annualInterestRate / 12 / 100) * balance;
    }

    public char getType() {
        return type;
    }

    public double getAmount() {
        return amount;
    }

    public double getBalance() {
        return balance;
    }

    public ArrayList<Transactions> getTs() {
        return transactions;
    }

    public void setType(char type) {
        this.type = type;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setTs(ArrayList<Transactions> transactions) {
        this.transactions = transactions;
    }

    @Override
    public String toString() {
        return "Transactions{" + "dateCreated=" + dateCreated + ", type=" + type + ", amount=" + amount + ", balance=" + balance + ", annualInterestRate=" + annualInterestRate + '}';
    }

}

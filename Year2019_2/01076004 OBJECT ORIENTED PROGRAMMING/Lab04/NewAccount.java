
import java.util.ArrayList;
import java.util.Date;

public class NewAccount {

    private String Name;
//private String specifiedName;
    private int id;
    private double balance = 0;
    private double interestRate;
    private Date dateCreated;
    ArrayList<Transactions> transactions = new ArrayList<>();

    public NewAccount() {
        dateCreated = new Date();
    }

    public NewAccount(String Name, int id, double balance, double interestRate) {
        this.Name = Name;
        this.id = id;
        this.balance = balance;
        this.interestRate = interestRate;
        dateCreated = new Date();
    }

    public void withdraw(double w) {
        transactions.add(new Transactions('W', w, balance - w));
        balance = balance - w;
    }

    public void deposit(double d) {
        transactions.add(new Transactions('D', d, balance + d));
        balance = balance + d;
    }

    public String getName() {
        return Name;
    }

    public int getId() {
        return id;
    }

    public double getBalance() {
        return balance;
    }

    public Date getDateCreated() {
        return dateCreated;
    }

    public ArrayList<Transactions> getTransactions() {
        return transactions;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setDateCreated(Date dateCreated) {
        this.dateCreated = dateCreated;
    }

    public void setTransactions(ArrayList<Transactions> transactions) {
        this.transactions = transactions;
    }

    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate;
    }

    @Override
    public String toString() {
        return "NewAccount{" + "Name=" + Name + ", id=" + id + ", balance=" + balance + ", interestRate=" + interestRate + ", dateCreated=" + dateCreated + ", transactions=" + transactions + '}';
    }

}

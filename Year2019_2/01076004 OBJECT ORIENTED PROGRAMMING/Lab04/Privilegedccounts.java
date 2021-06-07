
public class Privilegedccounts extends NewAccount {

    private double limit = 20000;

    public Privilegedccounts() {
    }

    public Privilegedccounts(String Name, int id, double balance, double interestRate) {
        super(Name, id, balance, interestRate);
    }

    public void deposit(double d) {
        super.deposit(d); //To change body of generated methods, choose Tools | Templates.
    }

    public void withdraw(double w) {
        if (super.getBalance() - w >= -limit) {
            System.out.println("Over Money" + limit);
        } else {
            super.withdraw(w); //To change body of generated methods, choose Tools | Templates.
        }
    }

    public String toString() {
        return "Privileged{" + "id=" + super.getId() + ", balance=" + super.getBalance() + ", annaulInterestRate=" + super.getInterestRate() + "%" + ", dateCreated=" + super.getDateCreated() + ", name=" + super.getName() + "}";
    }

}

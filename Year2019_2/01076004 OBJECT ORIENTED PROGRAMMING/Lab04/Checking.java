
public class Checking extends NewAccount {
    
    public Checking() {
    }

    public Checking(String Name, int id, double balance, double interestRate) {    
        super(Name, id, balance, interestRate);
    }

    public void deposit(double d) {
        super.deposit(d); //To change body of generated methods, choose Tools | Templates.
    }


    public void withdraw(double w) {
        if (super.getBalance() - w - 20 >= 0) {

            super.getTransactions().add(new Transactions('W', w, super.getBalance() - w - 20));
            super.setBalance(super.getBalance() - w - 20);
        } else {
            System.out.println("You don't have enough money for withdraw " + w);

        }
    }

    public String toString() {
        return "Checking{" + "id=" + super.getId() + ", balance=" + super.getBalance() + ", dateCreated=" + super.getDateCreated() + ", name=" + super.getName() + "}";
    }

}


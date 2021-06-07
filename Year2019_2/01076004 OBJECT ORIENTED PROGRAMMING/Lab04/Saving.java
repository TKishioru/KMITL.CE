
public class Saving extends NewAccount{
    
    public Saving() {
    }

    public Saving(String Name, int id, double balance, double interestRate) {
        super(Name, id, balance, interestRate);
    }


    public void deposit(double d) {
        super.deposit(d); //To change body of generated methods, choose Tools | Templates.
    }

    public void withdraw(double w) {
        if(super.getBalance()-w>=0){
        super.withdraw(w); //To change body of generated methods, choose Tools | Templates.
        }else{
            System.out.println("You don't have enough money for withdraw "+w);
         
        }
    }
        public String toString() {
        return "Savings{" + "id=" + super.getId() + ", balance=" + super.getBalance() + ", annaulInterestRate=" + super.getInterestRate() +"%"+ ", dateCreated=" + super.getDateCreated() + ", name=" + super.getName()+"}";
    }
}

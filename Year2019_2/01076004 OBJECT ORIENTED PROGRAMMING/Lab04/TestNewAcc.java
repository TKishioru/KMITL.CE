
public class TestNewAcc {

    public static void main(String[] args) {
        NewAccount a = new NewAccount("George", 1122, 1000, 1.5);
        //(String Name, int id, double balance, double interestRate)
        a.deposit(30.00);
        a.deposit(40.00);
        a.deposit(50.00);
        a.withdraw(5.00);
        a.withdraw(4.00);
        a.withdraw(2.00);
        for (int i = 0; i < a.getTransactions().size(); i++) {

            System.out.println(a.getTransactions().get(i).toString());

        }
        System.out.println(a.toString() + "\n");

        Checking c = new Checking("George", 1122, 1000, 0);

        Privilegedccounts p = new Privilegedccounts("George", 2048, 2500, 2.5);

        Saving s = new Saving("George", 5789, 1500, 0.75);

        c.deposit(50);
        c.withdraw(1030);
        for (int i = 0; i < c.getTransactions().size(); i++) {
            System.out.println(c.getTransactions().get(i).toString());
        }

        System.out.println(c.toString() + "\n");

        p.deposit(50);
        p.withdraw(6000);
        for (int i = 0; i < p.getTransactions().size(); i++) {
            System.out.println(p.getTransactions().get(i).toString());
        }

        System.out.println(p.toString() + "\n");

        s.deposit(50);
        s.withdraw(6000);
        for (int i = 0; i < s.getTransactions().size(); i++) {
            System.out.println(s.getTransactions().get(i).toString());
        }
        System.out.println(s.toString() + "\n");

    }
}

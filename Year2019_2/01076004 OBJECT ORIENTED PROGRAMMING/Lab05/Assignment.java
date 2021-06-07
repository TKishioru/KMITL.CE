
public class Assignment extends AssignmentList {

    private String name;
    private int month;
    private int day;
    private int hour;
    private int minute;
    private double score;
    private double totalPoints;
    private double totalWeight;

    public Assignment(String name, int month, int day, int hour, int minute) {
        this.name = name;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
    }

    public String getName() {
        return name;
    }

    public int getMonth() {
        return month;
    }

    public int getDay() {
        return day;
    }

    public int getHour() {
        return hour;
    }

    public int getMinute() {
        return minute;
    }

    public double getScore() {
        return score;
    }

    public double getTotalPoints() {
        return totalPoints;
    }

    public double getTotalWeight() {

        return totalWeight;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public void setTotalPoints(double Points) {
        this.totalPoints = Points;
    }

    public void setTotalWeight(double Weight) {
        this.totalWeight = Weight;
    }

    @Override
    public String toString() {
        return "(  date : " + month + "-" + day + "at " + hour + ":" + minute + ") : score = " + score + "; totalPoints = " + totalPoints + "; totalWeight = " + totalWeight;
        //Unit Testing ( date : 12−01 at 23:00) : score = 0.78; totalPoints = 0.99; totalWeight = 0.30
    }
}

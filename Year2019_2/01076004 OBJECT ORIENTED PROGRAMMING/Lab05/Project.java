
public class Project extends Assignment {

    private String specification;
    private String dataFile;

    public String getSpecification() {
        return specification;
    }

    public String getDataFile() {
        return dataFile;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public void setDataFile(String dataFile) {
        this.dataFile = dataFile;
    }

    public Project(String name, int month, int day, int hour, int minute) {
        super(name, month, day, hour, minute);
    }

    public Project(String specification, String dataFile, String name, int month, int day, int hour, int minute) {
        super(name, month, day, hour, minute);
        this.specification = specification;
        this.dataFile = dataFile;
    }

    @Override
    public String toString() {
        return "(  date : " + super.getMonth() + "-" + super.getDay() + "at " + super.getHour() + ":" + super.getMinute() + ") : score = " + super.getScore() + "; totalPoints = " + super.getTotalPoints() + "; totalWeight = ← " + super.getTotalWeight() + "; specification = " + specification + "; data file = " + dataFile;
        //Unit Testing ( date : 12−01 at 23:00) : score = 0.78; totalPoints = 0.99; totalWeight = ← 0.30; s p e c i f i c a t i o n = UnitTesting . pdf ; data file = Snacks . csv;    
    }
}


import java.util.ArrayList;

public class AssignmentList {

    private ArrayList<Assignment> itemList = new ArrayList<>();

    private int numberOfAssignment = 0;
    private double grade = 0, weightA = 0, sumG = 0;

    AssignmentList() {

    }

    public void additem(Assignment item) {
        numberOfAssignment++;
    }

    public double computeCourseGrade() {
        for (int i = 0; i <= numberOfAssignment; i++) {
            sumG += ((itemList.get(i).getScore()) * (itemList.get(i).getTotalWeight()));
            weightA += (itemList.get(i).getTotalWeight());
        }
        grade = sumG / weightA;
        return grade;

    }

    public ArrayList<Assignment> getItemList() {
        return itemList;
    }

    public void setItemList(ArrayList<Assignment> itemList) {
        this.itemList = itemList;
    }

    @Override
    public String toString() {
        return "AssignmentList{" + "itemList=" + itemList + '}';
    }

}

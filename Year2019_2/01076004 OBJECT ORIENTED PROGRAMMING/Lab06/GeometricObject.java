
import java.util.ArrayList;
import java.util.Date;

public abstract class GeometricObject implements Comparable<GeometricObject>,Colorable {

    String color;
    Date deateCreated;
    private static int numberOfGeo = 5;
    private ArrayList<GeometricObject> itemList = new ArrayList<>();

    public GeometricObject() {
    }

    public GeometricObject(String color, Date deateCreated) {
        this.color = color;
        this.deateCreated = deateCreated;
    }

    abstract double getArea();

    abstract double getPerimeter();

    public static GeometricObject max(GeometricObject o1, GeometricObject o2) {
        if(o1.compareTo(o2) == +1) return o1;
        else return o2;        
//return o1.compareTo(o2) == 1 ? o1 : o2;
    }

    public void ShowGeo() {
        for (int i = 0; i <= numberOfGeo; i++) {
            System.out.println(itemList.get(i).getArea() + itemList.get(i).color);
        }
    }

    public ArrayList<GeometricObject> getItemList() {
        return itemList;
    }

    public void setItemList(ArrayList<GeometricObject> itemList) {
        this.itemList = itemList;
    }

    @Override
    public String toString() {
        return "GeometricObject{" + "color=" + color + ", deateCreated=" + deateCreated + '}';
    }
}

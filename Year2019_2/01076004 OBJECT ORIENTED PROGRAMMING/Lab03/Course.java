
public class Course {

    private String courseName;
    private String[] students = new String[100];
    private int numberOfStudent;
    
    private Student[] classList;
    private Faculty faculty;

    public void setFaculty(Faculty faculty) {
        this.faculty = faculty;
    }
    public void addStudent(Student s){
        
    }
           
    public Course(String courseName) {
        this.courseName = courseName;
    }

    public String getCourseName() {
        return courseName;
    }

    public String[] getStudents() {
        return students;
    }

    public int getNumberOfStudent() {
        return numberOfStudent;
    }

    public void addStudent(String student) {
        students[numberOfStudent] = student;
        numberOfStudent++;
    }

    public void dropStudent(String student) {
        for (int i = 0; i < students.length; i++) {
            if (students[i] == student) {
                students[i] = null;
            }
        }
        numberOfStudent--;
    }

    @Override
    public String toString() {
        return "Course{" + "courseName=" + courseName + ", students=" + students + ", numberOfStudent=" + numberOfStudent + ", classList=" + classList + ", faculty=" + faculty + '}';
    }
    

}

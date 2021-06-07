/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class MaddAccN2Controller implements Initializable {

    private String user_sg, pass_sg, email_sg;
    private User currentUser;

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

    public void initUser(String user, String pass, String email) {
        this.user_sg = user;
        this.pass_sg = pass;
        this.email_sg = email;

    }

    @FXML
    private TextField name_sur;

    @FXML
    private TextField phone;

    @FXML
    private TextArea address;

    @FXML
    private Button create_ac;

    @FXML
    private Label back_p1;

    @FXML
    void back_page1(MouseEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("MaddAccN1.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();
    }

    @FXML
    void onCreate(ActionEvent event) throws IOException {
        User user = new User(user_sg, pass_sg, name_sur.getText(), address.getText(), phone.getText(), email_sg);
        ArrayList<User> user_read = new ArrayList<User>();

        //---------------Read
        try {
            FileInputStream readData = new FileInputStream("Users.txt");
            ObjectInputStream readStream = new ObjectInputStream(readData);

            user_read = (ArrayList<User>) readStream.readObject();
            readStream.close();

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("First time sign up!");
        }

        if (user_sg.length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Username must >= 6 letters!!");
            alert.showAndWait();
        } else if (pass_sg.length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Password must >= 6 letters!!");
            alert.showAndWait();
        } else if (verifyRegis(user_read, user_sg) == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Username is already exist!,Pls try agian");
            alert.showAndWait();
        } else if (user_sg.isEmpty() == true || pass_sg.isEmpty() == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Please Fill Username or Password");
            alert.showAndWait();
        } else {
            user_read.add(user);
            currentUser = user;
            Alert alert = new Alert(AlertType.INFORMATION);
            alert.setTitle("Information Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Sign Up Success!");
            alert.showAndWait();
            Parent root = FXMLLoader.load(getClass().getResource("Mlogin.fxml"));
            Scene site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(site);
            window.show();
        }

        //----------------Write
        try (ObjectOutputStream user_out = new ObjectOutputStream(new FileOutputStream("Users.txt"))) {
            user_out.writeObject(user_read);
            user_out.flush();
            user_out.close();
            System.out.println("Sign Up Success!");
        } catch (FileNotFoundException ex) {
            System.out.println("FileNotFound!");
        } catch (IOException ex) {
            System.out.println("Fail create!");
        }

    }

    public boolean verifyRegis(ArrayList<User> user_read, String user) {
        boolean found = false;

        for (User user1 : user_read) {
            if (user1.getUser().compareTo(user) == 0) {
                found = true;
                break;
            } else {
                found = false;
            }
        }

        return found;
    }

}

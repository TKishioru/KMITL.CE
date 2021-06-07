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
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class HeditController implements Initializable {

    private User currentuser;

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

    public void initUser(User user) {
        currentuser = user;
        name_sur.setText(currentuser.getName_sur());
        phone.setText(currentuser.getPhone());
        email.setText(currentuser.getEmail());
        pass.setText(currentuser.getPass());
        address.setText(currentuser.getAddress());

    }

    @FXML
    private Button Back;

    @FXML
    private Button edit_btt;

    @FXML
    private TextArea address;

    @FXML
    private TextField name_sur;

    @FXML
    private TextField phone;

    @FXML
    private TextField email;

    @FXML
    private PasswordField pass;

    @FXML
    void back_page(ActionEvent event) throws IOException {
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("HHome.fxml"));
            Parent root = loader.load();
            HHomeController home_control = loader.getController();
            home_control.initUser(currentuser);
            
            Scene home_site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(home_site);
            window.show();
    }

    @FXML
    void onedit(ActionEvent event) {
        
        currentuser.setName_sur(name_sur.getText());
        currentuser.setEmail(email.getText());
        currentuser.setAddress(address.getText());
        currentuser.setPass(pass.getText());
        currentuser.setPhone(phone.getText());
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

        for (User user : user_read) {
            if (user.getUser().compareTo(currentuser.getUser()) == 0) {
                //user.setAddress(currentUser.getAddress());
                user.setName_sur(name_sur.getText());
                user.setEmail(email.getText());
                user.setAddress(address.getText());
                user.setPass(pass.getText());
                user.setPhone(phone.getText());
                System.out.println("EDIT!");
                
            }
        }

        try (ObjectOutputStream user_out = new ObjectOutputStream(new FileOutputStream("Users.txt"))) {
            user_out.writeObject(user_read);
            user_out.flush();
            user_out.close();
            System.out.println("Save Success!");
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Information Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Change Complete!");
            alert.showAndWait();
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("HHome.fxml"));
            Parent root = loader.load();
            HHomeController home_control = loader.getController();
            home_control.initUser(currentuser);
            
            Scene home_site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(home_site);
            window.show();
            
        } catch (FileNotFoundException ex) {
            System.out.println("FileNotFound!");
        } catch (IOException ex) {
            System.out.println("File Can't Write");
        }
    }
}

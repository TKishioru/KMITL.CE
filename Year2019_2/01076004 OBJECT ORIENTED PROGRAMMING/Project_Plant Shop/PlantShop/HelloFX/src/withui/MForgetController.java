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
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class MForgetController implements Initializable {
    
    private String pass = "";

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

    @FXML
    private TextField user_fg;

    @FXML
    private TextField email_fg;

    @FXML
    private Button checkbtt;

    @FXML
    private Button backbtt;

    @FXML
    void onBack(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("MLogin.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();
    }

    public boolean verifyForget(ArrayList<User> user_read, String user, String email) {
        boolean found = false;
        //for(user xi :  userAttayList X)
        for (User user1 : user_read) {
            if (user1.getUser().compareTo(user) == 0 && user1.getEmail().compareTo(email) == 0) {
                pass = user1.getPass();
                found = true;
                break;
            } else {
                found = false;
            }
        }

        return found;
    }
    
    @FXML
    void onCheck(ActionEvent event) {
        
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

        if (user_fg.getText().isEmpty() == true || email_fg.getText().isEmpty() == true) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Please Fill Username or Email");
            alert.showAndWait();
        } else {
            if(verifyForget(user_read, user_fg.getText(), email_fg.getText()) == true){
                Alert alert = new Alert(Alert.AlertType.INFORMATION);
                alert.setTitle("Information Dialog");
                alert.setHeaderText(null);
                alert.setContentText("Your Password : " + pass);
                alert.showAndWait();
            }else{
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setTitle("Warning Dialog");
                alert.setHeaderText(null);
                alert.setContentText("Not Found!");
                alert.showAndWait();
                
                
            }
                
            
            
        }

        
    }
}

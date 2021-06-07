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
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author Nitipat
 */
public class MainMLController implements Initializable {

    

    /**
     * Initializes the controller class.
     */
    

    
    
    private User currentUser = new User();

    
    
    //---------Login---------//
    @FXML
    private TextField tf;

    @FXML
    private PasswordField pf;
    @FXML
    private Button lBtt;

    @FXML
    private Button regisbtt;

    @FXML
    private Button bttforgot;

    //--------Regis P1----------//
    @FXML
    private PasswordField pass_sign;

    @FXML
    private TextField email_sign;

    @FXML
    private TextField user_sign;

    @FXML
    private Button next_regis;

    @FXML
    private Label already_s;

    
    

    public boolean verifyLogin(ArrayList<User> user_read, String user, String pass) {
        boolean found = false;
        //for(user xi :  userAttayList X)
        for (User user1 : user_read) {
            if (user1.getUser().compareTo(user) == 0 && user1.getPass().compareTo(pass) == 0) {
                currentUser = user1;
                found = true;
                break;
            } else {
                found = false;
            }
        }

        return found;
    }

    @FXML
    void onClick(ActionEvent event) throws IOException {
        //Product Read----------------------------------------------------//
        ArrayList<Products> products_read = new ArrayList<Products>();
        ArrayList<Products> cart_read = new ArrayList<Products>();
        /*try {
            FileInputStream readData = new FileInputStream("Products.txt");
            ObjectInputStream readStream = new ObjectInputStream(readData);

            products_read = (ArrayList<Products>) readStream.readObject();
            readStream.close();

        } catch (Exception e) {
            System.out.println("Error");
        }*/

        //User Read-------------------------------------------------------//
        ArrayList<User> user_read = new ArrayList<User>();
        try {
            FileInputStream readData = new FileInputStream("Users.txt");
            ObjectInputStream readStream = new ObjectInputStream(readData);

            user_read = (ArrayList<User>) readStream.readObject();
            readStream.close();

        } catch (Exception e) {
            System.out.println("Error");
        }

        if (verifyLogin(user_read, tf.getText(), pf.getText()) == true) {
            Alert alert = new Alert(AlertType.INFORMATION);
            alert.setTitle("Information Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Welcome " + tf.getText() + "!");
            alert.showAndWait();
            System.out.println(currentUser.toString());
            //-------------------Change to Home-------------------------///
            /*Parent root = FXMLLoader.load(getClass().getResource("HHome.fxml"));
            Scene site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(site);
            window.show();*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("HHome.fxml"));
            Parent root = loader.load();
            HHomeController home_control = loader.getController();
            home_control.initUser(currentUser);
            
            Scene home_site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(home_site);
            window.show();
            
            

        } else if (tf.getText().isEmpty() == true || pf.getText().isEmpty() == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Please Fill Username or Password");
            alert.showAndWait();
        } else {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Sorry Try Again!");
            alert.showAndWait();
            //System.out.println("Incorrect");
        }

    }

    @FXML
    void onFor(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("MForget.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();
    }
    
    @FXML
    void onRegis(ActionEvent event) throws IOException {

        Parent root = FXMLLoader.load(getClass().getResource("MaddAccN1.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();

    }

    @FXML
    void next_page(ActionEvent event) throws IOException {

        
        
        


        if (user_sign.getText().length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Username must >= 6 letters!!");
            alert.showAndWait();
        } else if (pass_sign.getText().length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Password must >= 6 letters!!");
            alert.showAndWait();
        } else if (user_sign.getText().isEmpty() == true || pass_sign.getText().isEmpty() == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Please Fill Username or Password");
            alert.showAndWait();
        } else {
            /*
            Alert alert = new Alert(AlertType.INFORMATION);
            alert.setTitle("Information Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Sign Up Success!");
            alert.showAndWait();*/
            
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("MaddAccN2.fxml"));
            Parent root = loader.load();
            MaddAccN2Controller home_control = loader.getController();
            home_control.initUser(user_sign.getText(),pass_sign.getText(),email_sign.getText());
            
            Scene home_site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(home_site);
            window.show();
            
            
        }

        //----------------Write
        
        
        
        /*Parent root = FXMLLoader.load(getClass().getResource("MaddAccN2.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();*/
        
       

    }

    @FXML
    void previous_login(MouseEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("Mlogin.fxml"));
        Scene site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(site);
        window.show();
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

    
    
    

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }

}

/*
User user = new User();
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

        if (user_sign.getText().length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Username must >= 6 letters!!");
            alert.showAndWait();
        } else if (pass_sign.getText().length() < 5) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Password must >= 6 letters!!");
            alert.showAndWait();
        } else if (verifyRegis(user_read, user_sign.getText()) == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Username is already exist!,Pls try agian");
            alert.showAndWait();
        } else if (user_sign.getText().isEmpty() == true || pass_sign.getText().isEmpty() == true) {
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Warning Dialog");
            alert.setHeaderText(null);
            alert.setContentText("Please Fill Username or Password");
            alert.showAndWait();
        } else {
            user.setUser(user_sign.getText());
            user.setUser(pass_sign.getText());
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
*/

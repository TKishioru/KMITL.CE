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
import javafx.scene.control.Label;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class HHomeController implements Initializable {

    private User currentuser;

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

    public void initUser(User user) {
        currentuser = user;
        username.setText(currentuser.getUser());
        System.out.println(currentuser.getOrder());

    }

    @FXML
    private Button Home_btt;

    @FXML
    private Button healbtt;

    @FXML
    private Button secbtt;

    @FXML
    private Button ornbtt;

    @FXML
    private Button allbtt;

    @FXML
    private Button probtt;

    @FXML
    private Button purbtt;

    @FXML
    private Label username;

    @FXML
    private Button editbtt;

    @FXML
    private Button logoutbtt;

    @FXML
    private Button shownow;

    @FXML
    void onAll(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop1.fxml"));
        Parent root = loader.load();
        Hshop1Controller hshop1_control = loader.getController();
        hshop1_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();

    }

    @FXML
    void onEdit(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hedit.fxml"));
        Parent root = loader.load();
        HeditController hedit_control = loader.getController();
        hedit_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onHeal(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop4.fxml"));
        Parent root = loader.load();
        Hshop4Controller hshop4_control = loader.getController();
        hshop4_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onHome(ActionEvent event) {

    }

    @FXML
    void onLogout(ActionEvent event) throws IOException {

       ArrayList<User> user_read = new ArrayList<User>();

        //---------------Read
        try {
            FileInputStream readData = new FileInputStream("Users.txt");
            ObjectInputStream readStream = new ObjectInputStream(readData);

            user_read = (ArrayList<User>) readStream.readObject();
            readStream.close();

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Read!");
        }

        for (User user : user_read) {
            if (user.getUser().compareTo(currentuser.getUser()) == 0) {
                //user.setAddress(currentUser.getAddress());
                user.setId(currentuser.getId());
                user.setAddress(currentuser.getAddress());
                user.setNumberOfOrder(currentuser.getNumberOfOrder());
                //user.currentcart = currentUser.currentcart;
                System.out.println(currentuser.getCurrentcart().getProductList());
                user.getCurrentcart().setProductList(currentuser.getCurrentcart().getProductList());
                System.out.println(user.getCurrentcart().getProductList());
                user.setOrderList(currentuser.getOrderList());
                user.setPoint(currentuser.getPoint());

            }
        }

        try (ObjectOutputStream user_out = new ObjectOutputStream(new FileOutputStream("Users.txt"))) {
            user_out.writeObject(user_read);
            user_out.flush();
            user_out.close();
            System.out.println("Save Success!");

            Parent root = FXMLLoader.load(getClass().getResource("Mlogin.fxml"));
            Scene site = new Scene(root);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(site);
            window.show();

        } catch (FileNotFoundException ex) {
            System.out.println("FileNotFound!");
        } catch (IOException ex) {
            System.out.println("File Can't Write");
        }
    }

    @FXML
    void onOrn(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop2.fxml"));
        Parent root = loader.load();
        Hshop2Controller hshop2_control = loader.getController();
        hshop2_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onPro(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("HPromo.fxml"));
        Parent root = loader.load();
        HPromoController hedit_control = loader.getController();
        hedit_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onPur(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hpuch.fxml"));
        Parent root = loader.load();
        HpunchController hedit_control = loader.getController();
        hedit_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onSec(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop3.fxml"));
        Parent root = loader.load();
        Hshop3Controller hshop3_control = loader.getController();
        hshop3_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

}

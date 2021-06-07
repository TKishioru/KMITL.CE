/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class HplantController_3 implements Initializable {

    private User currentuser = new User();
    private Products pro;
    private int count = 0;
    public void initUser(User user) {
        currentuser = user;

    }
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
    }
    @FXML
    private ImageView product_img;

    @FXML
    private Label name_plant;

    @FXML
    private Label type;

    @FXML
    private Label amount;

    @FXML
    private Label price;

    @FXML
    private Label information;

    @FXML
    private Button Back;

    @FXML
    private Button addcart;

    @FXML
    private Button reducebtt;

    @FXML
    private Button incress;

    @FXML
    void onAdd(ActionEvent event) throws IOException {

        currentuser.currentcart.addProducts(pro, count);
        System.out.println(currentuser.currentcart);
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop1.fxml"));
        Parent root = loader.load();
        Hshop1Controller home_control = loader.getController();
        home_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onBack(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hshop1.fxml"));
        Parent root = loader.load();
        Hshop1Controller home_control = loader.getController();
        home_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onDecress(ActionEvent event) {
        if(count >0)
            amount.setText(--count +"");
        
    }

    @FXML
    void onIncress(ActionEvent event) {
        amount.setText(++count +"");
        
    }

    void initProduct(Products product) {
       pro = product;
       name_plant.setText(pro.getName());
       information.setText(pro.getInfo());
       price.setText(pro.getPrice()+".00");
       type.setText(pro.getCategoryName());
    }
}

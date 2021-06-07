/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.Toggle;
import javafx.scene.control.ToggleGroup;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class HsendController implements Initializable {

    private String[] Payment = {"Visa", "MasterCard", "Debit Card"};
    private ObservableList<String> data = FXCollections.observableArrayList(Payment);
    private User currentuser;
    private ToggleGroup shipmentGroup = new ToggleGroup();

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        comboBox.setItems(data);
        comboBox.setValue("Visa");
        std_.setSelected(true);
        this.std_.setToggleGroup(shipmentGroup);
        this.ems_.setToggleGroup(shipmentGroup);
        this.kerry_.setToggleGroup(shipmentGroup);
        
    }

    public void initUser(User user) {
        currentuser = user;
        name_sur.setText(currentuser.getName_sur());
        phone.setText(currentuser.getPhone());
        address.setText(currentuser.getAddress());
        currentuser.currentcart.setFee(20);
        if (currentuser.code.getCode().isEmpty() == false) {
                    totalprice.setText(currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100))+"");
        } else {
                    totalprice.setText(currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() + "");
        }
        
        
    }

    @FXML
    private Button backbtt;

    @FXML
    private Button orderbtt;

    @FXML
    private TextField name_sur;

    @FXML
    private TextArea address;
    
    @FXML
    private TextField phone;

    @FXML
    private ComboBox<String> comboBox;

    @FXML
    private Label totalprice;

    @FXML
    void onBack(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("HNbuy.fxml"));
        Parent root = loader.load();
        HNbuyController home_control = loader.getController();
        home_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onCalculate(ActionEvent event) {
        /*shipmentGroup.selectedToggleProperty().addListener((ObservableValue<? extends Toggle> ob, Toggle o, Toggle n) -> {
            RadioButton rb = (RadioButton) shipmentGroup.getSelectedToggle();

            
            
            
            
            if (rb.getText().equals("Kerry 100 THB (1-4 days)")) {
                System.out.println("Change Fee1");
                currentuser.currentcart.setFee(100);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + " THB");

            } else if (rb.getText().equals("EMS 80 THB (2-5 days)")) {
                System.out.println("Change Fee2");
                currentuser.currentcart.setFee(80);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + " THB");
            } else {
                currentuser.currentcart.setFee(55);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + " THB");
            }
        });*/
    }

    @FXML
    void onOrder(ActionEvent event) throws IOException {
        
        currentuser.addOrder(new Order(currentuser.code.getPer() * ((currentuser.getCurrentcart().getTotalPrice() + currentuser.currentcart.getFee()) / 100), currentuser.getCurrentcart().getTotalPrice(), currentuser.currentcart.getFee(), currentuser.getCurrentcart().getTotalPrice() + currentuser.currentcart.getFee(), currentuser.getName_sur(), currentuser.getAddress(),comboBox.getSelectionModel().getSelectedItem()));
        System.out.println("" + currentuser.code.getPer() * ((currentuser.getCurrentcart().getTotalPrice() + currentuser.currentcart.getFee()) / 100));
        System.out.println("Per : " + currentuser.code.getPer() + "TotalPrice : "  );
        System.out.println(currentuser.getOrder());
        //currentUser.setPoint(currentUser.getPoint()+(currentUser.getCurrentcart().getTotalPrice() + currentUser.currentcart.getFee())/100);
        System.out.println("" + currentuser.getPoint());
        currentuser.getCurrentcart().getProductList().clear();
        currentuser.currentcart.setProductList(currentuser.getCurrentcart().getProductList());
        currentuser.useCode();

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
    private RadioButton std_ ;

    @FXML
    private RadioButton ems_ ;

    @FXML
    private RadioButton kerry_ ;
    
    @FXML
    void onSelected(ActionEvent event) {
        if(shipmentGroup.getSelectedToggle().equals(this.std_)){
            currentuser.currentcart.setFee(20);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + "");
        }
        
        if(shipmentGroup.getSelectedToggle().equals(this.kerry_)){
            currentuser.currentcart.setFee(30);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + "");
        }
        if(shipmentGroup.getSelectedToggle().equals(this.ems_)){
            currentuser.currentcart.setFee(45);
                int sum = 0;
                if (currentuser.code.getCode().isEmpty() == false) {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee() - (currentuser.code.getPer() * ((currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee()) / 100));
                } else {
                    sum = currentuser.currentcart.getTotalPrice() + currentuser.currentcart.getFee();
                }
                totalprice.setText(sum + "");
        }
        
        
        
    }
    
   
}

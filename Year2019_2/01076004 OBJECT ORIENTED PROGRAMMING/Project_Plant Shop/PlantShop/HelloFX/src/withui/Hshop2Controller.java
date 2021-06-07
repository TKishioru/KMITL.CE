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
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class Hshop2Controller implements Initializable {

    private User currentuser;
    private ArrayList<Products> product_list = new ArrayList<>();

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

    public void initUser(User user) {
        currentuser = user;
        username.setText(currentuser.getUser());
        amountcart.setText(String.valueOf(currentuser.currentcart.getTotalAmount()));
        product_list.add(new Products(name_p3.getText(), Integer.parseInt(price_p3.getText()), "ornamental", "ราชินีแห่งไม้ประดับ”\n"
                + "สำหรับในด้านความเป็นมงคล มีความเชื่อกันว่าหากบ้านใดปลูกต้นเฟื่องฟ้าไว้เป็นไม้ประจำบ้าน จะสามารถช่วยสร้างคุณค่าของชีวิตให้สูงขึ้น"));
        product_list.add(new Products(name_p4.getText(), Integer.parseInt(price_p4.getText()), "ornamental", "ต้นพรมออสเตรเลียแดง"));
        product_list.add(new Products(name_p6.getText(), Integer.parseInt(price_p6.getText()), "ornamental", "การดูดสารพิษของลิ้นมังกรจะไม่มากนัก แต่คุณสมบัติเด่นของลิ้นมังกรอยู่ที่เป็นพืชที่คายออกซิเจนออกมาตอนกลางคืนและดูดคาร์บอนไดออกไซด์เข้าไป จึงเหมาะที่จะปลูกไว้ในห้องนอน\n"
                + "\n"
                + "การดูแลรักษา\n"
                + "ลิ้นมังกร เป็นไม้ประดับที่มีความเขียวสดใสตลอดทั้งปี ลิ้นมังกรแคระปลูกเลี้ยงง่าย ทนต่อสภาพแวดล้อมที่แห้งแล้ง จึงไม่ต้องดูแลรักษามาก แต่ต้องได้รับแสงเพียงพอ สามารถปลูกได้ทั้งภายในอาคารบ้านเรือนและกลางแจ้ง"));

    }
@FXML
    private Button homebtt;

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
    private Label amountcart;
    
    @FXML
    private Button purbtt;
    @FXML
    private Label username;

    @FXML
    private Label name_p3;

    @FXML
    private Label price_p3;

    @FXML
    private Button Info_p3;

    @FXML
    private Label name_p4;

    @FXML
    private Label price_p4;

    @FXML
    private Button Info_p4;

    @FXML
    private Label name_p6;

    @FXML
    private Label price_p6;

    @FXML
    private Button Info_p6;

    @FXML
    void onInfo_p3(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hplant_2.fxml"));
        Parent root = loader.load();
        HplantController_2 hplant_control = loader.getController();
        hplant_control.initUser(currentuser);
        hplant_control.initProduct(product_list.get(0));

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onInfo_p4(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hplant_3.fxml"));
        Parent root = loader.load();
        HplantController_3 hplant_control = loader.getController();
        hplant_control.initUser(currentuser);
        hplant_control.initProduct(product_list.get(1));

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }

    @FXML
    void onInfo_p6(ActionEvent event) throws IOException {

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hplant_5.fxml"));
        Parent root = loader.load();
        HplantController_5 hplant_control = loader.getController();
        hplant_control.initUser(currentuser);
        hplant_control.initProduct(product_list.get(2));

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
    private Button cartbtt;
    @FXML
    void onCart(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("HNbuy.fxml"));
        Parent root = loader.load();
        HNbuyController hedit_control = loader.getController();
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
    void onAll(ActionEvent event) throws IOException {
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
    void onHome(ActionEvent event) throws IOException {
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
    void onLogout(ActionEvent event) {
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
    void onOrn(ActionEvent event) {
        
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
    void onSearch(ActionEvent event) {

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

package withui;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.Initializable;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.InputMethodEvent;
import javafx.stage.Stage;

/**
 *
 * @author Nitipat
 */
public class HNbuyController implements Initializable {

    private User currentuser;

    public void initUser(User user) {
        currentuser = user;
        assumePane1.setText(currentuser.getCurrentcart().nameList());
        assumePane11.setText(currentuser.getCurrentcart().numberList());
        assumePane3.setText(currentuser.getCurrentcart().totalList());
        //amountText.setText("    |           " + currentuser.getCurrentcart().getTotalAmount() + "          |");
        last_price.setText(currentuser.getCurrentcart().getTotalPrice()+"");
        System.out.println(last_price);

    }

    @FXML
    private Label last_price;

    @FXML
    private Label assumePane1;

    @FXML
    private Label assumePane11;

    @FXML
    private Label assumePane3;

    @FXML
    private TextField code_box;

    @FXML
    void check_code(InputMethodEvent event) {
        if(code_box.getText().compareTo(currentuser.code.getCode()) == 1){
            
        }
    }

    @FXML
    void onCheckout(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("Hsend.fxml"));
        Parent root = loader.load();
        HsendController home_control = loader.getController();
        home_control.initUser(currentuser);

        Scene home_site = new Scene(root);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(home_site);
        window.show();
    }
    
    @FXML
    void onBack(ActionEvent event) throws IOException {
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
    void onOK(ActionEvent event) {
        
        
    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {

    }

}

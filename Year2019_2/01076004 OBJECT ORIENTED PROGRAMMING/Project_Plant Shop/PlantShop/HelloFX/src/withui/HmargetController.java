/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.Initializable;

/**
 *
 * @author Nitipat
 */
public class HmargetController implements Initializable {

    private User currentuser;
    
    public void initUser(User user) {
        currentuser = user;
        

    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
       
    }
    
    
    
}
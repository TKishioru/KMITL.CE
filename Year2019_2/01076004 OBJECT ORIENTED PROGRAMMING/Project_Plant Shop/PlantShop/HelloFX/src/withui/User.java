package withui;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
/**
 *
 * @author Nitipat
 */
public class User implements Serializable{
    private int id;
    private int status; // 0-member 1-admin
    private String user;
    private String pass;
    private String name_sur;
    private String address;
    private String phone;
    private String email;
    private int numberOfOrder;
    public ArrayList<Order> orderList = new ArrayList<Order>();
    public Cart currentcart = new Cart();
    public Code code = new Code();
    public int point;
    public User() {
    }

    public User(String user, String pass , String email) {
        this.user = user;
        this.pass = pass;
        this.email = email;
        
    }

    public User(String user, String pass, String name_sur, String address, String phone, String email) {
        this.user = user;
        this.pass = pass;
        this.name_sur = name_sur;
        this.address = address;
        this.phone = phone;
        this.email = email;
    }

    public void addOrder(Order order){
        orderList.add(order);
        addPoint(order.getTotalOrderPrice()/50);
        System.out.println("Point :" +this.point);
        numberOfOrder++;
    }

    public String getOrder(){
        String s = "";
        for (int i = 0; i < numberOfOrder; i++) {
            s+= "Order No "+ i + " : " + orderList.get(i).toString();
            s+="\n------------------------\n";
        }
//            s+=orderList.get(orderList.size()-1).toString();
//            s+="\n------------------------\n";
        
        return s;
    }
    
    public String checkOrder(Date now){
        String s = "";
        for (int i = 0; i < numberOfOrder; i++) {
            s+= "Order No "+ (i+1) + " : " + orderList.get(i).purchaselist(now);
            s+="\n----------------------------------------------------------------------------------------------------------------------------------\n";
        }
//            s+=orderList.get(orderList.size()-1).toString();
//            s+="\n------------------------\n";
        
        return s;
        
    }

    public ArrayList<Order> getOrderList() {
        return orderList;
    }

    public int getPoint(){
        return this.point;
    }
    
    public void setPoint(int i){
        this.point=i;
    }
    public void addPoint(int i){
        this.point=this.point+i;
    }
    public void setOrderList(ArrayList<Order> orderList) {
        this.orderList = orderList;
    }
    
    public int getNumberOfOrder() {
        return numberOfOrder;
    }

    public void setNumberOfOrder(int numberOfOrder) {
        this.numberOfOrder = numberOfOrder;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }

    public String getName_sur() {
        return name_sur;
    }

    public void setName_sur(String name_sur) {
        this.name_sur = name_sur;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "User{" + "id=" + id + ", status=" + status + ", user=" + user + ", pass=" + pass + ", name_sur=" + name_sur + ", address=" + address + ", phone=" + phone + ", email=" + email + ", Cart = " + currentcart + ", Point =" + point ;
    }

    public Cart getCurrentcart() {
        return currentcart;
    }
    
     // function to generate a random string of length n 
    public String genCode(int per) 
    { 
  
        // chose a Character random from this String 
        String AlphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                    + "0123456789"
                                    + "abcdefghijklmnopqrstuvxyz"; 
  
        // create StringBuffer size of AlphaNumericString 
        StringBuilder sb = new StringBuilder(4); 
  
        for (int i = 0; i < 4; i++) { 
  
            // generate a random number between 
            // 0 to AlphaNumericString variable length 
            int index 
                = (int)(AlphaNumericString.length() 
                        * Math.random()); 
  
            // add Character one by one in end of sb 
            sb.append(AlphaNumericString 
                          .charAt(index)); 
        } 
        if(per == 5) this.point=this.point-100;
        else if(per == 10) this.point=this.point-250;
        else this.point=this.point-500;
        
        String s = sb.toString();
        this.code.setCode(s);
        this.code.setPer(per);
        return sb.toString(); 
    } 
    
    
    public String showCode(){
        String s = "";
        s+="Code : "+code.getCode()+" for discount "+code.getPer()+"%";
        return s;
    }
    
    
     public void useCode(){
        
       this.code.setCode("0000");
       this.code.setPer(0);
    }
    
    
}

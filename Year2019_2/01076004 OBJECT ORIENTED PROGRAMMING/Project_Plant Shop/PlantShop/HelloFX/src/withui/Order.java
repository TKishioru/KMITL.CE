/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;


import java.io.Serializable;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 *
 * @author MrZOMBIT
 */
public class Order implements Serializable {

    private int productPrice, fee, order, totalOrderPrice, discount;
    private String name, address, types;
    private Date dateCreate = new Date();
    private static final DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");

    public Order() {
    }

    public Order(int discount, int productPrice, int fee, int order, String name, String address) {
        this.discount = discount;
        this.productPrice = productPrice;
        this.fee = fee;
        this.order = order;
        this.name = name;
        this.address = address;
        this.totalOrderPrice = productPrice + fee - discount;
        
    }

    public Order(int discount, int productPrice, int fee, int order, String name, String address, String type) {
        this.discount = discount;
        this.productPrice = productPrice;
        this.fee = fee;
        this.order = order;
        this.name = name;
        this.address = address;
        this.totalOrderPrice = productPrice + fee - discount;
        this.types = type;
    }

    public int getProductPrice() {
        return productPrice;
    }

    public int getTotalOrderPrice() {
        return totalOrderPrice;
    }

    public void setTotalOrderPrice(int totalOrderPrice) {
        this.totalOrderPrice = totalOrderPrice;
    }

    public void setDiscount(int totalOrderPrice) {
        this.discount = totalOrderPrice;
    }

    public int getDiscount() {
        return this.discount;
    }

    public void setProductPrice(int productPrice) {
        this.productPrice = productPrice;
    }

    public int getFee() {
        return fee;
    }

    public void setFee(int fee) {
        this.fee = fee;
    }

    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Date getDateCreate() {
        return dateCreate;
    }

    public String checkStatus(Date now, int fee) {
        String s = "";
        Date ordered = dateCreate;
        Calendar c = Calendar.getInstance();

        if (fee == 20) {
            c.setTime(ordered);
            c.add(Calendar.DATE, 5);

        } else if (fee == 30) {
            c.setTime(ordered);
            c.add(Calendar.DATE, 1);
        } else {
            c.setTime(ordered);
            c.add(Calendar.DATE, 2);
        }

        if (ordered.compareTo(now) == 0) {
            s = "The product has been delivered!";

        } else {
            s = "The product has delivering!";
        }

        return s;
    }

    public String purchaselist(Date now) {
        /*return "Date : " + dateCreate
                + "\n Products Price\t\t= " + productPrice
                + "\n Shipment Fee\t\t= " + fee
                + "\n Discount\t\t\t= " + discount
                + "\n Name\t\t\t= " + name
                + "\n Address\t\t\t= " + address
                + "\n Total Price\t\t= " + totalOrderPrice
                + "\n Type\t\t\t= " + types
                + "\n Status\t\t\t= " + checkStatus(now, fee);
         */

        return dateCreate
                + "\nName \t\t\t=  " + name
                + "\nAddress \t\t\t=  " + address
                + "\nProducts Price\t\t=  " + productPrice+" ฿" + "\t\tShipment Fee\t\t=  " + fee+" ฿" + "\t\tDiscount\t\t\t=  " + discount+" ฿"
                + "\nTotal Pricet\t\t=  " + totalOrderPrice+" ฿" + "\t\tPayment\t\t\t=  " + types + "\t\tStatus\t\t\t = " + checkStatus(now, fee);
    }

    @Override
    public String toString() {
        return "Date : " + dateCreate
                + "\n Products Price = " + productPrice
                + "\n Shipment Fee   = " + fee
                + "\n Discount       = " + discount
                + "\n Name           = " + name
                + "\n Address        = " + address
                + "\n Total Price    = " + totalOrderPrice
                + "\n Type           = " + types;

    }

}

/*

return "Date : " + dateCreate
                + "\n Products Price = " + productPrice
                + "\n Shipment Fee   = " + fee
                + "\n Discount       = " + discount
                + "\n Name           = " + name
                + "\n Address        = " + address
                + "\n Total Price    = " + totalOrderPrice
                + "\n Type           = " + types
                + "\n Status         = " + checkStatus(dateCreate, fee);
*/

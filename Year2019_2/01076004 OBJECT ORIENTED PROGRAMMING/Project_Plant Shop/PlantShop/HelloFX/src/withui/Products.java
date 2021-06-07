/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;

import java.io.Serializable;

/**
 *
 * @author MrZOMBIT
 */
public class Products  implements Serializable {
    
    
    private String name;
    private int price;
    private int numberOfProduct,totalPrice;
    private int category;
    private String info;
    private String categoryName;
    private String img;
    

    public Products(String name, int price, String categoryName,String info) {
        this.name = name;
        this.price = price;
        this.totalPrice = price;
        this.info = info;
        this.categoryName = categoryName;
        
        
        numberOfProduct++;
    }

    public Products(){}
    
    
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getNumberOfProduct() {
        return numberOfProduct;
    }

    public void setNumberOfProduct(int numberOfProduct) {
        this.numberOfProduct = numberOfProduct;
        this.totalPrice = numberOfProduct*price;
    }

    public int getCategory() {
        return category;
    }

    public void setCategory(int category) {
        this.category = category;
    }

    public int getTotalPrice() {
        this.totalPrice = numberOfProduct*price;
        return totalPrice;
    }

    public void setTotalPrice(int totalPrice) {
        this.totalPrice = totalPrice;
    }

    
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public String getCategoryName() {
        return categoryName;
    }

    public void setCategoryName(String categoryName) {
        this.categoryName = categoryName;
    }

    public String getImg() {
        return img;
    }
    
    
    
    
    
   
    

}

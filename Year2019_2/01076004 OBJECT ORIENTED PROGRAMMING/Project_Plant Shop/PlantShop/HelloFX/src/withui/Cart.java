/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package withui;


import java.io.Serializable;
import java.util.ArrayList;

/**
 *
 * @author Nitipat
 */
public class Cart implements Serializable{
    public ArrayList<Products> productList = new ArrayList<>();
    private int totalAmount;
    private int totalPrice;
    private int fee=100;

    public Cart(ArrayList<Products> productList) {
        this.productList = productList;
    }

    public Cart() {
    }

    public ArrayList<Products> getProductList() {
        return productList;
    }

    public void addProducts(Products product,int amount){
        int size = productList.size();;
        if(productList.size()!=0){
        for (int i = 0; i < size; i++) {
            System.out.println(productList.get(i).getName() +" "+product.getName());
            if((productList.get(i).getName().compareTo(product.getName()) == 0) ){
                if(productList.get(i).getNumberOfProduct()!=0){
                    productList.get(i).setNumberOfProduct(productList.get(i).getNumberOfProduct()+amount);
                    System.out.println("Old item num :"+productList.get(i).getNumberOfProduct());
                    
                }
                else {productList.add(product);
                productList.get(i).setNumberOfProduct(productList.get(i).getNumberOfProduct()+amount-1);
                System.out.println("New1 item num :"+productList.get(i).getNumberOfProduct()); }
            }
            else if(i==size-1){productList.add(product);
            productList.get(i+1).setNumberOfProduct(productList.get(i+1).getNumberOfProduct()+amount-1);
            System.out.println("New2 item num :"+productList.get(i).getNumberOfProduct());}
        }} else {productList.add(product); productList.get(0).setNumberOfProduct(productList.get(0).getNumberOfProduct()+amount-1);}      
        System.out.println(productList.size());
    }
    
    public void deleteProducts(Products product){
        int size = productList.size();
        for (int i = 0; i < size; i++) {
            System.out.println(productList.get(i).getName() +" "+product.getName());
            if((productList.get(i).getName().compareTo(product.getName()) == 0) ){
                    productList.remove(i);
            }
        }
    }
    
    public void deleteAllProducts(){
        productList.clear();
    }
    
    public void addAmountProducts(Products product,int amount){
        int size = productList.size();;
        for (int i = 0; i < size; i++) {
            System.out.println(productList.get(i).getName() +" "+product.getName());
            if((productList.get(i).getName().compareTo(product.getName()) == 0) ){
                if(productList.get(i).getNumberOfProduct()!=0){
                    productList.get(i).setNumberOfProduct(productList.get(i).getNumberOfProduct()+amount);
                    System.out.println("Old item num :"+productList.get(i).getNumberOfProduct());
                }
            }
        }
        System.out.println(productList.size());
    }
    
    public int verifyAddProducts(Products product){
        int s=0;
        int size = productList.size();;
        if(productList.size()!=0){
        for (int i = 0; i < size; i++) {
            System.out.println(productList.get(i).getName() +" "+product.getName());
            if((productList.get(i).getName().compareTo(product.getName()) == 0) ){ s=1; System.out.println("Old item!");}
            }
        }   
        if(s==0) System.out.println("New item!");
        return s;
    }
    
    public void setProductList(ArrayList<Products> productList) {
        this.productList = productList;
    }

    public int getFee() {
        return fee;
    }

    public void setFee(int fee) {
        this.fee = fee;
    }

    
    
    public int getTotalAmount() {
        int sum = 0;
        for (Products products : productList) {
            sum += products.getNumberOfProduct();
        }
        totalAmount = sum;
        return totalAmount;
    }

    public void setTotalAmount(int totalAmount) {
        this.totalAmount = totalAmount;
    }

    public int getTotalPrice() {
        int sum = 0;
        for (Products products : productList) {
            sum += products.getTotalPrice();
        }
        totalPrice = sum;
        return totalPrice;
    }

    @Override
    public String toString() {
        String s = "";
        for (Products products : productList) {
            s += products.getName() + "           |           " + products.getNumberOfProduct() + "           |           " + products.getTotalPrice() + "\n";
        }
        return s;
    }

    public void setTotalPrice(int totalPrice) {
        this.totalPrice = totalPrice;
    }
    public void reduceProduct(Products product){
        for (Products products : productList) {
            if(products == product){
                products = productList.get(productList.size()-1);//productList.size()-1;
                productList.remove(productList.size()-1);
            }
        }
    }

    void setProductList(Cart currentcart) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    public String nameList(){
        String s = "";
        int i = 1;
       
        for (Products products : productList) {
            s += i + "." + products.getName()+"\n";
            i++;
        }
        return s;
    }

    public String numberList(){
        String s = "";
        for (Products products : productList) {
            s += products.getNumberOfProduct()+"\n";
        }
        return s;
    }

    public String totalList(){
        String s = "";
        for (Products products : productList) {
            s += products.getTotalPrice()+"\n";
        }
        return s;
    }
}

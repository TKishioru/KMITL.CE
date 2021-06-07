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
public class Code implements Serializable{
    public String code = "0000";
    public int percent = 0;
    
    Code(){}
    Code(String code,int percent){
        this.code = code;
        this.percent = percent;
    }
    
    public int getPer(){
        return this.percent;
    }  
    
    public String getCode(){
        return this.code;
    }  
    
    public void setCode(String code){
        this.code = code;
    }  
    public void setPer(int per){
        this.percent = per;
    } 
}

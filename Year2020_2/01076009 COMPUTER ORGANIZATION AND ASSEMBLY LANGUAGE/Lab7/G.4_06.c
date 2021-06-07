/*
จงพัฒนาโปรแกรมด้วยภาษา C เพื่อรับตัวเลขจำนวน 2 ตัวจากผู้ใช้ผ่านทางคีย์บอร์ด เรียกว่า A และ B แล้วคำนวณหาค่า หารร่วมมาก (Greatest Common Divisor) หรือ หรม (GCD) และแสดงผลลัพธ์ตาม
ตัวอย่างในตารางต่อไปนี้
Input   Output
5 2     1
18 6    6
49 42   7
81 18   9
*/
#include <stdio.h>

int main(){
	int A,B,gcd = 0;
    printf("Enter Number(A): ");
    scanf("%d",&A);
    printf("Enter Number(B): ");
    scanf("%d",&B);
    for(int i = 1;i < A;i++){
        if ((A%i == 0) && (B%i == 0)){
            gcd = i;
        }
    }
    printf("GCD : %d",gcd);
	return 0;
}
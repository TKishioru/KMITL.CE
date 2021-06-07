/*
จงพัฒนาโปรแกรมด้วยภาษา C เพื่อรับตัวเลขจำนวน 2 ตัวจากผู้ใช้ผ่านทางคีย์บอร์ด เรียกว่า A และ B แล้วคำนวณและแสดงผลลัพธ์ ตามตารางต่อไปนี้ "A % B = <Result>"
Input   Output
5 2     5 % 2 = 1
18 6    18 % 6 = 0
5 10    5 % 10 = 5
10 5    10 % 5 = 0
*/
#include <stdio.h>

int main(){
	int A,B;
    printf("Enter Number(A): ");
    scanf("%d",&A);
    printf("Enter Number(B): ");
    scanf("%d",&B);
    printf("%d %% %d = %d",A,B,A%B);
	return 0;
}

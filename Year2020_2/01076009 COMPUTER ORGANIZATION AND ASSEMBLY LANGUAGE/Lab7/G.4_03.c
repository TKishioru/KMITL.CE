//จงยกตัวอย่างการเรียกใช้ฟังค์ชัน printf ด้วยการส่งค่าพารามิเตอร์แบบ Pass by Values
#include <stdio.h>
int func_byVal(int);
int main(){
	int data = 100;
    func_byVal(data);
    printf("data = %d",data);
    //Answer : 100
	return 0;
}
int func_byRef(int data){
    data = 900
}
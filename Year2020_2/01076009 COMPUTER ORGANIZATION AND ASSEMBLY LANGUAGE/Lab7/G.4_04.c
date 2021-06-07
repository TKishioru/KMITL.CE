//จงยกตัวอย่างการเรียกใช้ฟังค์ชัน scanf ด้วยการส่งค่าพารามิเตอร์แบบ Pass by Reference
#include <stdio.h>

int func_byRef(int*);
int main(){
	int data = 100;
    func_byRef(&data);
    printf("data = %d",data);
    //Answer : 900
	return 0;
}
int func_byRef(int *prt){
    *prt = 900;
}
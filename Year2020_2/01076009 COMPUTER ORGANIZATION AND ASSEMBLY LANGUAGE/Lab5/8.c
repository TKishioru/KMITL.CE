/*
จงพัฒนาโปรแกรมภาษา C เพื่อสั่งพิมพ์เลขอนุกรม Fibonacci โดยรับค่าเลขเป้าหมาย n ซึ่งเกิดจาก n = (n-1)+(n-2)
EX. input number 5 : 1 1 2 3 5
*/


//Code by Erika
#include <stdio.h>

int main() {
    int i, n, t1 = 0, t2 = 1, nextTerm;
    printf("Enter the number (n): ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");

    for (i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }

    return 0;
}

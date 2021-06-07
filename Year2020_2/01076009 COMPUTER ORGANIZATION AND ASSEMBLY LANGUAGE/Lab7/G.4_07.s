@ asl.s is an assembly program that stores 2 integers
@ (A and B) and return greater number

@ ============== Data ==============

.data
.balign 4
get_num_A:  .asciz "Number A : \n"
get_num_B:  .asciz "Number B : \n"
result: .asciz "Greater Number : %d"
pattern: .asciz "%d"
A: .word 0
B: .word 0
OUT: .word 0

@ ============== CODE ==============

.text
.global main
.global printf
.global scanf

@ —————— Compare Function ——————
main: @Get 2 ints R1 and R2, show greater R
@print "Number 1: "
ldr r0, get_num_A
bl printf

@get A form keyboard
ldr r0, addr_pattern
str r1, addr_A
bl scanf

ldr r0, get_num_B
bl printf

ldr r0, addr_pattern
ldr r1, addr_B
bl scanf

ldr r0, get_num_A
ldr r0, [R0]
ldr r1, get_num_B
ldr r1, [R1]
cmp r0, r1 gt
movgt r2, r0
movlt r2, r1

ldr r0, result
ldr r1, r2
bl printf

@ —————— ADDR ——————
addr_A: .word A
addr_B: .word B
addr_OUT: .word OUT
addr_pattern: .word pattern
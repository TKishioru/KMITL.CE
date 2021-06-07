var1		DCD		1
var1addr	DCD		var1
		
main		MOV		R1, #2
		LDR		R2, =var1addr
		STR		R1, [R2]
		LDR		R0, [R2]

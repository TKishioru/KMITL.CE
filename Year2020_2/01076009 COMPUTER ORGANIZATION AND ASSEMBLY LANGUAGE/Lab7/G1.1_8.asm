fifteen	DCD		15
thirty	DCD		30
		
		
main		LDR		R1,=fifteen
		MOV		R3,#15
		STR		R3,[R1]
		LDR		R2,=thirty
		MOV		R3,#30
		STR		R3,[R2]
		
		LDR		R1,=fifteen
		LDR		R1,[R1]
		LDR		R2,=thirty
		LDR		R2,[R2]
		ADD		R0,R1,R2
		

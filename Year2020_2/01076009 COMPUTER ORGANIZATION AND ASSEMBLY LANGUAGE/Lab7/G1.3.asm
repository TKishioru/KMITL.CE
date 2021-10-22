numbers	DCB		1,2,3,4,5

main		LDR		R3,=numbers
		LDRB		R0,[R3,#2]
		

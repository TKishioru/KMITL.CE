var1		DCD		1
var1addr	DCD		var1
		
main		MOV		R5, #1
loop		CMP		R4, #0
		BLE		lend
else		MOV		R5, #2
lend		MOV		R0, R5

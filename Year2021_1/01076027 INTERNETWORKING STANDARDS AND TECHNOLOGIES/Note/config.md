# Configure Router

```

```

ชื่ออุปกรณ์	: `hostname name`
ความปลอดภัยในการเข้าถึง : enable secret password
สร้างแบนเนอร์ : banner motd # text #
เชื่อมต่ออินเทอร์เฟส *loopback ก็เหมือนกัน*
	interface type slot/port
	
	ip address [ip] [subnet mask]
	
	no shut
	
	*สำหรับ DCE for PC : clock rate 56000*
	
## Static Routes
1. `ip route [ip remote] [subnet mask] [next hop]`
2. `ip route [ip remote] [subnet mask] [next hop]`
3. `ip route [ip remote] [subnet mask] [next hop]`

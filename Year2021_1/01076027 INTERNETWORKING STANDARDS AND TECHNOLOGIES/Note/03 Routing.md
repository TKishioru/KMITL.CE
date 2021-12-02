```
Static Routing & Dynamic Routing Protocol
```
**ลักษณะเฉพาะ**
1. Topology : โครงสร้างในการต่อเน็ตเวิร์ค
2. Reliability : ความน่าเชื่อถือ
3. Speed : ความเร็ว
4. Scalability : สามารถปรับขนาดได้
5. Cost : ต้นทุน
6. Availability : ความพร้อมในการใช้งาน
7. Security : ความปลอดภัย

**Why Routing**
เป็นการตอบโต้ระหว่าง network ทั้งสอง และเปรียบเสมือนเป็นคอมพิวเตอร์เครื่องนึงที่มี CPU, OS, หน่วยเก็บความจำ

| Memory |                | Stores                                                                               |
|--------|----------------|--------------------------------------------------------------------------------------|
| RAM    | Volatitile     | - Running IOS - Running configuration file - IP routing & ARP tables - Packet buffer |
| ROM    | Non-Volatitile | - Bootup instructions - Basic diagnostic software - Limited IOS                      |
| NVRAM  | Non-Volatitile | - Startup configuration file                                                         |
| Flash  | Non-Volatitile | - IOS - Other system files                                                           |

**Function of Router**
1. เชื่อมต่อได้หลาย network ซึ่งจะมีหลาย interface แต่ละอันก็มี IP network ต่างกัน
2. มีฟังก์ชัน Routing (ค้นหาเส้นทาง) : Router จะเลือกทางที่สุดอยู่ในส่วน Routing Table
3. มีฟังก์ชัน Forwarding (รับ - ส่งข้อมูลต่อ) : การรับข้อมูลหรือ Packet เข้ามาทาง Port ใดๆ แล้วทำการส่งต่อข้อมูลนั้นออกไปยังอีก Port หนึ่ง
4. remote network ด้วยการทำเป็น static/dynamic routes เพื่อเพิ่มเส้นทางโดยตรง

**Packet Forwarding Methods**
- Process switching : ให้ CPU Process เลือกว่าจะไปทางไหน
- Fast switching : ไม่ต้องผ่าน CPU เผื่อประมวลผล
- Cisco Express Forwarding (CEF) : ดู routing แล้วไปเลย

**Connect Devices**

มี Default Gateways ซึ่งจำเป็นต่อการติดต่อไป network อื่นๆ
` จำเป็น! ` คือ ชื่ออุปกรณ์, interface, IP address/subnet mask, Default Gateways

**แจก IP ให้เครื่อง**
- static : ตั้งให้เอง
- dynamic : แจก ip ให้อัตโนมัติ (DHCP) 
> static ที่ดีกว่าเพราะว่าใช้ทรัพยากรน้อย ปลอดภัยมากกว่า แต่ config ยาก, หา Path ยาก + ใช้ยาก, สเปคน้อยกว่า Dynamic

**Path Determination**
- Best Path : มีค่าเส้นทาง (cost) ที่ต่ำสุด
  - RIP >>> จำนวน Hop
  - OSPF >> cost ที่คำนวณ BW จากต้นทาง - ปลายทาง
  - EIGRP > cost ที่คำนวณ BW, delay, load, reliability
- Load Balancing ในกรณีที่ cost เท่ากัน
> แบ่งส่ง
- AD : ระยะห่าง ยิ่งน้อย ยิ่งดี

**Routing Table**
| D   | 10.1.1.0/24 | [90/2170112] | via | 209.168.200.226 | 00:00:05 | Serial0/0/0      |
|-----|-------------|--------------|-----|-----------------|----------|------------------|
| ชนิด | remote ที่รู้จัก | AD/Cost      |     | hop ต่อไป        | เวลา     | interface ทางออก |
> ver.15 ขึ้นไป มีชนิด Link Local(L) แสดงด้วย

**ชนิด Static Routic**
- Standard SR. : อยากรู้ network ---> route เลย
> Stub network คือ เครือข่ายทีมีการเชื่อมต่อเส้นทางเดียว
- Default SR. :
- Summary SR. : รวมใช้ IP เดียวกัน
- Floating SR. : ทำ Backup-link สำรอง เผื่อ WAN ไม่ได้ + Private WAN เพิ่มความปลอดภัย

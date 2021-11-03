PC X : 172.1.0.2 255.255.254.0 172.1.0.1
PC Y : 172.1.2.2 255.255.255.128 172.1.2.1
PC Z : 192.168.3.2 255.255.255.0 192.168.3.1

**เปิดเครื่อง -> no
---- Router X ----
en
conf t

hostname Udon
int Gi 0/0
ip add 172.1.0.1 255.255.254.0
no shut
exit

int Se 0/0/0
ip add 172.1.2.129 255.255.255.252
no shut
exit

router eigrp 123
eigrp router-id 1.1.1.1
no auto-summary
network 172.1.0.0 0.0.1.255
network 172.1.2.128 0.0.0.3

---- Router Y ----
en
conf t

hostname Bangkok
int Se 0/0/1
clock rate 56000
ip add 172.1.2.130 255.255.255.252
no shut
exit

int Gi 0/0
ip add 172.1.2.1 255.255.255.128
no shut
exit

int Se 0/0/0
clock rate 56000
ip add 192.168.2.5 255.255.255.252
no shut
exit

router eigrp 123
eigrp router-id 2.2.2.2
no auto-summary
network 172.1.2.128 0.0.0.3
network 172.1.2.0 0.0.0.127
redistribute static
exit
ip route 0.0.0.0 0.0.0.0 192.168.2.6

---- Router Z ----
en
conf t

int Se 0/0/1
ip add 192.168.2.6 255.255.255.252
Router(config-if)#no shut
exit

int Gi 0/0
ip add 192.168.3.1 255.255.255.0
no shut
exit

int lo 0
ip add 10.1.1.1 255.255.255.252
exit

ip route 0.0.0.0 0.0.0.0 10.1.1.0
ip route 172.1.0.0 255.255.252.0 192.168.2.5
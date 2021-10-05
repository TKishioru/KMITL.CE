# Lab 7.2

```
Switch>en
Switch#copy running-config startup-config
Switch#conf t
Switch(config)#host IST
IST(config)#enable password ccna
IST(config)#end
	
IST#conf t
IST(config)#enable secret class
IST(config)#end

IST#disable
IST>en
Password: 
IST#conf t
IST(config)#line console 0
IST(config-line)#password cisco
IST(config-line)#login
IST(config-line)#end

IST#conf t
IST(config)#inter vlan 99
IST(config-if)#ip add 172.17.1.11 255.255.255.0
IST(config-if)#no shut
IST(config-if)#exit
IST(config)#ip default-gateway 172.17.1.254
IST(config)#vlan 99
IST(config-vlan)#exit
IST(config)#inter fa 0/1
IST(config-if)#switchport mode access
IST(config-if)#switchport access vlan 99
IST(config-if)#exit
IST(config)#line vty 0
IST(config-line)#password istlab
IST(config-line)#login
IST(config-line)#exit
IST(config)#username ADMINist secret istlab
IST(config)#line vty 0
IST(config-line)#login local
IST(config-line)#exit
IST(config)#ip domain-name ce.kmitl.ac.th
IST(config)#line vty 0
IST(config-line)#transport input ssh
IST(config-line)#exit
IST(config)#crypto key generate rsa
1024
```

# Lab 7.4

```
Switch>en
Switch#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#inter fa 0/4
Switch(config-if)#switch mode access
Switch(config-if)#switchport port-security
Switch(config-if)#switchport port-security mac-add sticky
Switch(config-if)#switchport port-security violation protect
```

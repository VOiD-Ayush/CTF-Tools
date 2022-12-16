# Important links and stuff

## Web
For web there are services that provide dns like 10.0.0.2.something.io that resolves to 10.0.0.2 helps in bypassing many ssrf and other things.
Its also known as rebounded ssrf heres a site that helps https://lock.cmpxchg8b.com/rebinder.html

If we want a subdomain filter bypass like anything_we_want.but_this_must_be_present.com we can use beeceptor for that.

Dnszone transfer
`dnsenum --dnsserver 10.129.89.244 --enum -p 0 -s 0 -o subdomains.txt -f /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb`

## Trick
SSH not working on some box solution : `sudo ifconfig eth0 mtu 1200`


## Rev
jad (tool converts .class file to .jad file which are human readable)


## Crypto
- General math
If we have `c = g * y % p` we can find y by `y = (c * inverse(g,p)) %p`
Miller Rabin no. that passes 64+ bases `2887148238050771212671429597130393991977609459279722700926516024197432303799152733116328983144639225941977803110929349655578418949441740933805615113979999421542416933972905423711002751042080134966731755152859226962916775325475044445856101949404200039904432116776619949629539250452698719329070373564032273701278453899126120309244841494728976885406024976768122077071687938121709811322297802059565867`


## Trick
SSH not working on some box solution : `sudo ifconfig eth0 mtu 1200`

Instead of proxychains we can use 
```bash
proxytunnel -p 10.0.0.7:3128 -d 127.0.0.1:22 -a 2222
proxytunnel -p proxy:port -d wheretoconnect:port -a ourport
```

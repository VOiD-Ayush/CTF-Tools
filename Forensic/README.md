# For Forensic category


## Extracting dns exfiltration
```bash
tshark -r wireshark.pcapng -T fields -e ip.src -e dns.qry.name -Y "dns.flags.response eq 0"
```

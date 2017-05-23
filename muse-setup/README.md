# MuseInstaller
Need to install the program.
- [Muse Research Tools](http://developer.choosemuse.com/research-tools/getting-started)

## Dependicies:
- Pyliblo (might need liblo) - used for OSC communication
  - [Pyliblo Info](http://das.nasophon.de/pyliblo/API.html)

# MuseIO command-line prompt 
First make sure to pair with your muse device to access the MAC address
Connecting with UDP over local port 5000 (UDP doesn't care about dropped bits)
`muse-io --device 'MACaddress' --osc osc.udp://localhost:5000`

# More info
- [MuseIO](http://developer.choosemuse.com/research-tools/museio)
- [OSC Server](http://developer.choosemuse.com/research-tools-example/grabbing-data-from-museio-a-few-simple-examples-of-muse-osc-servers#python)

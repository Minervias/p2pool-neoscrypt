Requirements:
-------------------------
Generic:
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Notes for NeoScrypt:
=========================
Requirements:
-------------------------
In order to use P2Pool with any NeoScrypt powered coin, you need to build
and install the NeoScrypt Python module first.

Linux:

    cd neoscrypt
    sudo python setup.py install
	
Notes for Innovacoin Daemon:
=========================
Requirements:
-------------------------
The Innovacoin Daemon must be running on or accessible from the p2pool application. 
Port 14520 has been used for Innovad. 

To install the Innova Daemon:

**Download and extract**
https://github.com/innovacoin/innova

	cd innova
    ./autogen.sh
    ./configure
    make
	make install # optional
	sudo apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils

**To run the coin Daemon**
	
	cd innova/src
	./innovad -daemon

**To see sync status**
	
	cd innova/src
	./innova-cli getinfo


Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local coin daemon. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net innovacoin

Then run your miner program, connecting to 127.0.0.1 on the default worker
port with any username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

**To open the ports on your Linux machine use command:**

sudo ufw allow 9333 - p2pool
sudo ufw allow 14777 - Worker Port

**To check the status of the firewall:**

sudo ufw status

Run for additional options.

    python run_p2pool.py --help
	
	
**Running P2Pool for Innovacoin:**
-------------------------------
Run P2Pool with the "--net innovacoin" option.
Run your miner program, connecting to 127.0.0.1 on port 14520.
Forward port 14519 on your router to any PXC nodes running P2Pool.	
	
	
Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/justino/p2pool-ui-punchy
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](LICENCE)



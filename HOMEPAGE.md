# ATC P2pool

## Intro

This is the future homepage of ATC P2Pool. Information about it will be released more when it enters BETA.

## Status
Current state: Alpha Testing

## Connect 

Current Testing Nodes (Contact if you wish to run a testing Node)

| Node		| IP					| Sponsor								|
|:----------|:----------------------|:--------------------------------------|
| Name TBD  | 104.131.60.126:8559	| [Mircea Popescu](http://trilema.com/)|
| ATC P2Pool Dev Box | 72.135.98.192:8559 | [MWGUY](http://mwguy.us/) |

## Documentation

*Incoming*

### Runtime Options

### How to install:

1. Install [Altcoin](http://therealaltcoin.org/)
1. Go to Install Direcotry
2. Pull Version down. Depending on wether you want the latest and greatest or the last stable branch.
    1. ```<Latest Release URL>```
    2. ```git clone https://github.com/chalbersma/p2pool```

### Example Runtime:

```
 python ./run_p2pool.py --give-author 0 --fee 1 --net altcoin -a 12djAcViRDNpfzkBEpN2N1RXCDocNi41BV --bitcoind-config-path /Path/to/altcoin.conf
```

### Howto Connect

Use the following information to connect to the server.

Connection Info: ```<servername or IP>:8559```
Username: ```1mebitcoinadress023kdfa```
Password: ```x```

Optionally if your bringing a lot of TH/s to the Node you can manually set a higher difficulty by adding +<diff> at the end. Example: ```1mebitcoinadress023kdfa+1024```

### Full runtime Options:

```
usage: run_p2pool.py [-h] [--version]
                     [--net {altcoin,bitcoin,fastcoin,litecoin,terracoin}]
                     [--testnet] [--debug] [-a ADDRESS] [--datadir DATADIR]
                     [--logfile LOGFILE] [--merged MERGED_URLS]
                     [--give-author DONATION_PERCENTAGE] [--iocp]
                     [--irc-announce] [--no-bugreport] [--p2pool-port PORT]
                     [-n ADDR[:PORT]] [--disable-upnp] [--max-conns CONNS]
                     [--outgoing-conns CONNS] [--disable-advertise]
                     [-w PORT or ADDR:PORT] [-f FEE_PERCENTAGE]
                     [--bitcoind-config-path BITCOIND_CONFIG_PATH]
                     [--bitcoind-address BITCOIND_ADDRESS]
                     [--bitcoind-rpc-port BITCOIND_RPC_PORT]
                     [--bitcoind-rpc-ssl]
                     [--bitcoind-p2p-port BITCOIND_P2P_PORT]
                     [BITCOIND_RPCUSERPASS [BITCOIND_RPCUSERPASS ...]]

p2pool (version 13.4-73-gb49389b)

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --net {altcoin,bitcoin,fastcoin,litecoin,terracoin}
                        use specified network (default: bitcoin)
  --testnet             use the network's testnet
  --debug               enable debugging mode
  -a ADDRESS, --address ADDRESS
                        generate payouts to this address (default: <address
                        requested from bitcoind>)
  --datadir DATADIR     store data in this directory (default: <directory
                        run_p2pool.py is in>/data)
  --logfile LOGFILE     log to this file (default: data/<NET>/log)
  --merged MERGED_URLS  call getauxblock on this url to get work for merged
                        mining (example:
                        http://ncuser:ncpass@127.0.0.1:10332/)
  --give-author DONATION_PERCENTAGE
                        donate this percentage of work towards the development
                        of p2pool (default: 1.0)
  --iocp                use Windows IOCP API in order to avoid errors due to
                        large number of sockets being open
  --irc-announce        announce any blocks found on
                        irc://irc.freenode.net/#p2pool
  --no-bugreport        disable submitting caught exceptions to the author
  --disable-upnp        don't attempt to use UPnP to forward p2pool's P2P port
                        from the Internet to this computer
  --disable-advertise   don't advertise local IP address as being available
                        for incoming connections. useful for running a dark
                        node, along with multiple -n ADDR's and --outgoing-
                        conns 0

p2pool interface:
  --p2pool-port PORT    use port PORT to listen for connections (forward this
                        port from your router!) (default: altcoin:8558,
                        bitcoin:9333, fastcoin:23660, litecoin:9338,
                        terracoin:9323)
  -n ADDR[:PORT], --p2pool-node ADDR[:PORT]
                        connect to existing p2pool node at ADDR listening on
                        port PORT (defaults to default p2pool P2P port) in
                        addition to builtin addresses
  --max-conns CONNS     maximum incoming connections (default: 40)
  --outgoing-conns CONNS
                        outgoing connections (default: 6)

worker interface:
  -w PORT or ADDR:PORT, --worker-port PORT or ADDR:PORT
                        listen on PORT on interface with ADDR for RPC
                        connections from miners (default: all interfaces,
                        altcoin:8559, bitcoin:9332, fastcoin:5150,
                        litecoin:9327, terracoin:9322)
  -f FEE_PERCENTAGE, --fee FEE_PERCENTAGE
                        charge workers mining to their own bitcoin address (by
                        setting their miner's username to a bitcoin address)
                        this percentage fee to mine on your p2pool instance.
                        Amount displayed at http://127.0.0.1:WORKER_PORT/fee
                        (default: 0)

bitcoind interface:
  --bitcoind-config-path BITCOIND_CONFIG_PATH
                        custom configuration file path (when bitcoind -conf
                        option used)
  --bitcoind-address BITCOIND_ADDRESS
                        connect to this address (default: 127.0.0.1)
  --bitcoind-rpc-port BITCOIND_RPC_PORT
                        connect to JSON-RPC interface at this port (default:
                        altcoin:9335, bitcoin:8332, fastcoin:9527,
                        litecoin:9332, terracoin:13332 <read from bitcoin.conf
                        if password not provided>)
  --bitcoind-rpc-ssl    connect to JSON-RPC interface using SSL
  --bitcoind-p2p-port BITCOIND_P2P_PORT
                        connect to P2P interface at this port (default:
                        altcoin:9336, bitcoin:8333, fastcoin:9526,
                        litecoin:9333, terracoin:13333 <read from bitcoin.conf
                        if password not provided>)
  BITCOIND_RPCUSERPASS  bitcoind RPC interface username, then password, space-
                        separated (only one being provided will cause the
                        username to default to being empty, and none will
                        cause P2Pool to read them from bitcoin.conf)
```

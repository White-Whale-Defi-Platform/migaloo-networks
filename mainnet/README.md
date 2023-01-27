# Migaloo Mainnet

This mainnet will start with the node version `x.x.x`.

**Genesis File**

[Genesis File](/mainnet/genesis.json):

```bash
curl -s  https://raw.githubusercontent.com/White-Whale-Defi-Platform/migaloo-networks/mainnet/main/genesis.json > ~/.FOLDER/config/genesis.json
```

**Genesis sha256**

```bash
sha256sum ~/.FOLDER/config/genesis.json
# TBD
```

**BINARY version**

```bash
$ BINARY version --long
TBD
```

**Seed nodes**

```
TBD
```

**Persistent Peers**

```
TBD
```

## Setup

**Prerequisites:** Make sure to have [Golang >=1.19](https://golang.org/).

#### Go setup

You need to ensure your gopath configuration is correct. If the following **'make'** step does not work then you might have to add these lines to your .profile or .zshrc in the users home folder:

```sh
nano ~/.profile
```

```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export GO111MODULE=on
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
```

Source update .profile

```sh
source .profile
```

### Minimum hardware requirements

- 8-16GB RAM
- 100GB of disk space
- 2 cores

## Setup validator node

Below are the instructions to generate & submit your genesis transaction

### Generate genesis transaction (gentx)

1. Initialize the Juno directories and create the local genesis file with the correct chain-id:

```bash
BINARY init <moniker-name> --chain-id=CHAIN_ID
```

2. Create a local key pair (skip this step if you already have a key):

```sh
> BINARY keys add <key-name>
```

3. Add your account to your local genesis file with a given amount and the key you just created. Use only `AMOUNT`, other amounts will be ignored.

```bash
BINARY add-genesis-account $(BINARY keys show <key-name> -a) AMOUNT
```

4. Create the gentx, use only `AMOUNT`:

```bash
BINARY gentx <key-name> v --chain-id=CHAIN_ID
```

If all goes well, you will see a message similar to the following:

```bash
Genesis transaction written to "/home/user/FOLDER/config/gentx/gentx-******.json"
```

### Submit genesis transaction

- Fork [the this repo](https://github.com/White-Whale-Defi-Platform/migaloo-networks) into your Github account

- Clone your repo using

```bash
git clone https://github.com/<your-github-username>/migaloo-networks
```

- Copy the generated gentx json file to `<repo_path>/gentx/`

```sh
cd migaloo-networks
cp ~/FOLDER/config/gentx/gentx*.json ./mainnet/gentx/
```

- Commit and push to your repo
- Create a PR onto https://github.com/White-Whale-Defi-Platform/migaloo-networks
- Only PRs from individuals / groups with a history successfully running nodes will be accepted. This is to ensure the network successfully starts on time.

#### Running in production

If you have not installed cosmovisor, create a systemd file for your Juno service:

```sh
sudo nano /etc/systemd/system/BINARY.service
```

Copy and paste the following and update `<YOUR_USERNAME>` and `<CHAIN_ID>`:

```sh
Description=Juno daemon
After=network-online.target

[Service]
User=juno
ExecStart=/home/<YOUR_USERNAME>/go/bin/BINARY start
Restart=on-failure
RestartSec=3
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
```

Enable and start the new service:

```sh
sudo systemctl enable BINARY
sudo systemctl start BINARY
```

Check status:

```sh
BINARY status
```

Check logs:

```sh
journalctl -u BINARY -f
```

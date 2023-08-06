# Migaloo Testnet

This testnet will start with the node version `x.x.x`.

## Minimum hardware requirements

- 8-16GB RAM
- 100GB of disk space
- 2 cores

## Genesis Instruction

### Install node

```bash
git clone https://github.com/White-Whale-Defi-Platform/migaloo-chain
cd migaloo-chain
git checkout x.x.x
make install
```

### Check Node version

```bash
# Get node version (should be x.x.x)
migalood version

# Get node long version (should be 78953dff50cf2f292a0f00eb6d7629531d86716d)
migalood version --long | grep commit
```

### Initialize Chain

```bash
migalood init MONIKER --chain-id=narwhal-2
```

### Download pre-genesis

```bash
curl -s https://raw.githubusercontent.com/White-Whale-Defi-Platform/migaloo-networks/main/narwhal-2/pre-genesis.json > ~/.migalood/config/genesis.json
```

## Create gentx

Create wallet

```bash
migalood keys add KEY_NAME
```

Fund yourself `20000000uwhale`

```bash
migalood add-genesis-account $(migalood keys show KEY_NAME -a) 20000000uwhale
```

Use half (`10000000uwhale`) for self-delegation

```bash
migalood gentx KEY_NAME 10000000uwhale --chain-id=narwhal-2
```

If all goes well, you will see a message similar to the following:

```bash
Genesis transaction written to "/home/user/.migalood/config/gentx/gentx-******.json"
```

### Submit genesis transaction

- Fork this repo
- Copy the generated gentx json file to `migaloo-networks/narwhal-2`
- Commit and push to your repo
- Create a PR on this repo
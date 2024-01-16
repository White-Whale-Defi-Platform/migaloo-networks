# Migaloo Testnet

This testnet will start with the node version `3.0.4`.

## Minimum hardware requirements

- 8-16GB RAM
- 100GB of disk space
- 2 cores

## Genesis Instruction

### Install node

```bash
git clone https://github.com/White-Whale-Defi-Platform/migaloo-chain
cd migaloo-chain
git checkout v3.0.4
make install
```

### Check Node version

```bash
# Get node version (should be v3.0.4)
migalood version

# Get node long version (should be de98de2dd96917ae1ab79161d573fc0b4ee1facf)
migalood version --long | grep commit
```

### Initialize Chain

```bash
migalood init MONIKER --chain-id=narwhal-2
```

### Replace pre-genesis

```bash
curl -s https://raw.githubusercontent.com/notional-labs/migaloo-networks/add-testnet-genesis/narwhal-2/genesis.json > ~/.migalood/config/genesis.json
```

## Run node

### Setup seeds

```bash
export PERSISTENT_SEEDS="6e8a56df9b9c52a730dd780172fc135a96a9feda@65.109.26.223:26656"
```

### Run node with persistent peers

```bash
migalood start --p2p.persistent_peers=$PERSISTENT_SEEDS
```

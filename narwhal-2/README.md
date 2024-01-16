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

# Get node long version (should be 6e3cc31edaa790176fe94792880f2ec25350b8d0)
migalood version --long | grep commit
```

### Initialize Chain

```bash
rm -rf ~/.migalood
migalood init notional --chain-id=narwhal-2
```

### Replace pre-genesis

```bash
# Download the file
curl -s https://raw.githubusercontent.com/notional-labs/migaloo-networks/add-testnet-genesis/narwhal-2/genesis.json > ~/.migalood/config/genesis.json

# Calculate the SHA256 checksum
calculated_checksum=$(shasum -a 256 ~/.migalood/config/genesis.json | awk '{ print $1 }')

# Compare with the expected checksum
expected_checksum="272eec5c068aa25393273b707ce861f634a570f7a0ee63e904d3e8f5c6632fc9"
if [ "$calculated_checksum" = "$expected_checksum" ]; then
    echo "---> Checksum is CORRECT."
else
    echo "---> Checksum is INCORRECT."
fi
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

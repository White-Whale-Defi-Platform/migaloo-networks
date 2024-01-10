import json

# Set this to your home directory.
INPUT_GENESIS_PATH = "/???/.migalood/config/genesis.json"
OUTPUT_GENESIS_PATH = "/???/.migalood/config/pre-genesis.json"

# Convenience variables
DENOM = "uwhale"
DECIMALS = "000000"
MILLION = 1000000
SECONDS_PER_DAY = 24 * 60 * 60

NUM_GENESIS_VALIDATORS = 8
INITIAL_GENESIS_ALLOCATION = 10
INITIAL_AMOUNT = NUM_GENESIS_VALIDATORS * INITIAL_GENESIS_ALLOCATION

# Do not edit. Used to check the total balances in the genesis.
THREE_MONTH_AMOUNT = 0
TWELVE_MONTH_AMOUNT = 0
TWENTY_FOUR_MONTH_AMOUNT = 0
THIRTY_SIX_MONTH_AMOUNT = 0
COMMUNITY_POOL_AMOUNT = 25 * MILLION
MULTI_SIG_AMOUNT = 380.3848 * MILLION - INITIAL_AMOUNT


# see: https://www.epochconverter.com for more infos on the unix time stamp
GENESIS_TIME_UNIX = 1704897600
THREE_MONTH_UNIX = 1712756400
TWELVE_MONTH_UNIX = 1736520000
TWENTY_FOUR_MONTH_UNIX = 1768056000
THIRTY_SIX_MONTH_UNIX = 1799592000

# List of all accounts that get continously vested tokens.
# Address: Address of the account.
# Amount: Amount of vested tokens of the Address.
# Vesting Duration: Duration of the vesting period in unix format starting from genesis.
VESTING_ACCOUNTS = [
    # Team
    {
        "address": "migaloo1v8n2jpmq8a97xtv9j28c557q3ztqn7rkrxtykg",
        "amount": 24 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo16u8ljxqr2sjfpxur5nmkpdu0j86vxh2udhunsu",
        "amount": 15 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo13w00xz4t7gftnur9q6w8ychlpxc4pw02hzdx5z",
        "amount": 14 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo18a9m9stu3dyvewwcq9qmp85euxqcvln5mefync",
        "amount": 12.5 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1eenffmetkkyzf5rejtn0jq5l2p7nz35klxlgff",
        "amount": 8 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1jr6m4eu65kgf6flncd7nrhd4gcaexexr0swxm9",
        "amount": 8 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1typsgj0nvketwusvaakyerjp9exr2fuxtmda9v",
        "amount": 4.25 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1pen8w6rshxqrt9t5fsd8zhc0ux54mrlw4al4mw",
        "amount": 4 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo10layywwtg6kcjr0nunvnsr9g78n6veae85zx8j",
        "amount": 2 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo16k4493edgkpy4apthg6m3m5wp0s36fvmkkampn",
        "amount": 4 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1ug5h3wn9qlmn00h7dvws8h68vdeh8c0paazv8z",
        "amount": 4 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1938p0dxg9s2wdfcy8j747gfuyf40wqzkdcmuxt",
        "amount": 2 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    {
        "address": "migaloo1qp8flhtcev6ag8av3mwr3eessuq8sxjrukh7tw",
        "amount": 1 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    { #ww hot wallet
        "address": "migaloo1fpfg0max7kvpn40y3245qnpg7a5lefsd7ktemg",
        "amount": 20 * MILLION,
        "duration": TWENTY_FOUR_MONTH_UNIX,
    },
    { #dankuzone
        "address": "migaloo1h8pgcp78hf20qmrpkykns70j8s0pvty0ve25ls",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #polkachu
        "address": "migaloo1jt9w26mpxxjsk63mvd4m2ynj0af09cslw4huul",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #nftswitch
        "address": "migaloo18mf4c20fw6903k0uyt5q2gtxtxaces8wveupfy",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #PFC
        "address": "migaloo1wpayju4jcn2mhv6yewclf6rcq9fyqzvavppjal",
        "amount": 4 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #synergy
        "address": "migaloo1xzern65ppact6sgh4htllnr8pg9dpnc8wrsq7h",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #autostake
        "address": "migaloo13qf8zqs95rvn2aqrpct4zvr6rsjl3xqqwrs44q",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #Kalia network
        "address": "migaloo14as7p2qkccvgq3q3nntzsjkdnpq03kk0nz3lfd",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
    { #kjnodes
        "address": "migaloo167k6kvu7rfeju9amdg654uqekhcrxf4pnyaqva",
        "amount": 3 * MILLION,
        "duration": THIRTY_SIX_MONTH_UNIX,
    },
]


def create_vesting_genesis_entry(address, amount, end_time):
    return {
        "@type": "/cosmos.vesting.v1beta1.ContinuousVestingAccount",
        "base_vesting_account": {
            "base_account": {
                "address": address,
                "pub_key": None,
                "account_number": "0",
                "sequence": "0",
            },
            "original_vesting": [{"denom": DENOM, "amount": amount}],
            "delegated_free": [],
            "delegated_vesting": [],
            "end_time": end_time,
        },
        "start_time": "%d" % GENESIS_TIME_UNIX,
    }


def create_account_genesis_entry(address, amount):
    return {"address": address, "coins": [{"denom": DENOM, "amount": amount}]}


if __name__ == "__main__":
    # Load genesis
    with open(INPUT_GENESIS_PATH, "r") as FILE:
        genesis = json.load(FILE)

    # Modify genesis parameters
    genesis["genesis_time"] = "2024-01-10T14:40:00.000000Z"
    genesis["chain_id"] = "narwhal-2"
    genesis["app_state"]["auth"]["params"]["max_memo_characters"] = "512"
    genesis["app_state"]["crisis"]["constant_fee"]["denom"] = DENOM
    genesis["app_state"]["distribution"]["params"][
        "community_tax"
    ] = "0.100000000000000000"
    genesis["app_state"]["gov"]["deposit_params"]["min_deposit"] = [
        {"denom": DENOM, "amount": "25000" + DECIMALS}
    ]
    genesis["app_state"]["gov"]["deposit_params"]["max_deposit_period"] = "%ds" % (
        14 * SECONDS_PER_DAY
    )
    genesis["app_state"]["gov"]["voting_params"]["voting_period"] = "%ds" % (
        7 * SECONDS_PER_DAY
    )
    genesis["app_state"]["mint"]["minter"]["inflation"] = "0.040000000000000000"
    genesis["app_state"]["mint"]["params"]["mint_denom"] = DENOM
    genesis["app_state"]["mint"]["params"]["inflation_max"] = "0.040000000000000000"
    genesis["app_state"]["mint"]["params"]["inflation_min"] = "0.040000000000000000"
    genesis["app_state"]["mint"]["params"]["goal_bonded"] = "0.750000000000000000"
    genesis["app_state"]["slashing"]["params"]["signed_blocks_window"] = "10000"
    genesis["app_state"]["slashing"]["params"][
        "min_signed_per_window"
    ] = "0.100000000000000000"
    genesis["app_state"]["slashing"]["params"][
        "slash_fraction_downtime"
    ] = "0.001000000000000000"
    genesis["app_state"]["staking"]["params"]["max_validators"] = 50
    genesis["app_state"]["staking"]["params"]["bond_denom"] = DENOM
    genesis["app_state"]["staking"]["params"][
        "min_commission_rate"
    ] = "0.050000000000000000"

    # Add community pool
    genesis["app_state"]["distribution"]["fee_pool"]["community_pool"].append(
        {"denom": DENOM, "amount": "%d%s" % (COMMUNITY_POOL_AMOUNT, DECIMALS)}
    )
    genesis["app_state"]["bank"]["balances"].append(
        create_account_genesis_entry(
            address="migaloo1jv65s3grqf6v6jl3dp4t6c9t9rk99cd82tdxu3",
            amount="%d%s" % (COMMUNITY_POOL_AMOUNT, DECIMALS),
        )
    )

    # Add multi-sig
    genesis["app_state"]["bank"]["balances"].append(
        create_account_genesis_entry(
            address="migaloo1zfpqclh862kcdr8czul2k2lu2gvwk5gfg26fpx",
            amount="%d%s" % (MULTI_SIG_AMOUNT, DECIMALS),
        )
    )

    # Add vesting accounts
    for account in VESTING_ACCOUNTS:
        genesis["app_state"]["bank"]["balances"].append(
            create_account_genesis_entry(
                address=account["address"],
                amount="%d%s" % (account["amount"], DECIMALS),
            )
        )
        genesis["app_state"]["auth"]["accounts"].append(
            create_vesting_genesis_entry(
                address=account["address"],
                amount="%d%s" % (account["amount"], DECIMALS),
                end_time="%d" % account["duration"],
            )
        )

    # Check how many tokens are vested to each category of initial holders.
    for account in VESTING_ACCOUNTS:
        if account["duration"] == THREE_MONTH_UNIX:
            THREE_MONTH_AMOUNT += account["amount"]
        elif account["duration"] == TWELVE_MONTH_UNIX:
            TWELVE_MONTH_AMOUNT += account["amount"]
        elif account["duration"] == TWENTY_FOUR_MONTH_UNIX:
            TWENTY_FOUR_MONTH_AMOUNT += account["amount"]
        elif account["duration"] == THIRTY_SIX_MONTH_UNIX:
            THIRTY_SIX_MONTH_AMOUNT += account["amount"]
        else:
            ...

    # Print results with some minor adjustments
    # migaloo14kqr9fjjzl24gwfndf05wkelncm76ynkk04zjk: Substract 1M from 36 and add to 12
    # migaloo18a9m9stu3dyvewwcq9qmp85euxqcvln5mefync: Substract 0.5M from 24 and add to 12
    # migaloo1typsgj0nvketwusvaakyerjp9exr2fuxtmda9v: Substract 0.25M from 24 and add to 12
    print("Initial", INITIAL_AMOUNT / MILLION)
    print("Three Month", THREE_MONTH_AMOUNT / MILLION)
    print("Twelve Month", TWELVE_MONTH_AMOUNT / MILLION + 0.25 + 0.5)
    print("Twenty Four Month", TWENTY_FOUR_MONTH_AMOUNT / MILLION - 0.25 - 0.5)
    print("Thirty Six Month", (THIRTY_SIX_MONTH_AMOUNT) / MILLION - 1)
    print("Community Pool", COMMUNITY_POOL_AMOUNT / MILLION)
    print("Multi Sig", MULTI_SIG_AMOUNT / MILLION)
    TOTAL = (
        THREE_MONTH_AMOUNT
        + TWELVE_MONTH_AMOUNT
        + TWENTY_FOUR_MONTH_AMOUNT
        + THIRTY_SIX_MONTH_AMOUNT
        + COMMUNITY_POOL_AMOUNT
        + MULTI_SIG_AMOUNT
    )
    print("Total", (TOTAL + INITIAL_AMOUNT) / MILLION)

    # Update total supply
    genesis["app_state"]["bank"]["supply"].append(
        {
            "amount": "%d%s" % (TOTAL, DECIMALS),
            "denom": DENOM,
        }
    )
    # Store genesis
    with open(OUTPUT_GENESIS_PATH, "w") as FILE:
        json.dump(genesis, FILE, indent=2)
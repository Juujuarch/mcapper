# mcapper

Memecoin position calculator. Given buy amount, entry market cap, and target market cap, compute your supply share, position value, and multiple.

```
python3 mcapper.py --buy 100 --entry 10000 --target 350000
# buy $100 @ $10,000 mcap -> $350,000 mcap: 1.0000% of supply = $3,500 (35x, +$3,400)
```

Multiple targets:

```
python3 mcapper.py --buy 100 --entry 10000 --targets 350000 700000 5000000
buy $100 @ $10,000 mcap -> $350,000 mcap: 1.0000% of supply = $3,500 (35x, +$3,400)
buy $100 @ $10,000 mcap -> $700,000 mcap: 1.0000% of supply = $7,000 (70x, +$6,900)
buy $100 @ $10,000 mcap -> $5,000,000 mcap: 1.0000% of supply = $50,000 (500x, +$49,900)
```

Assumes full hold, no fees, no slippage, no staged entries. Real results differ (fees, slippage, bonding curve, DEX LP pricing after graduation).

## Tests

```
python3 -m unittest test_mcapper.py
```

Run with any Python 3.
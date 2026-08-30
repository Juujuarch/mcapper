#!/usr/bin/env python3
"""mcapper — memecoin position calculator.

Compute position value and multiple given buy amount, entry market cap,
and target market cap. Assumes you bought a fixed % of supply (no fees,
no slippage, no staged entries).

Usage:
  mcapper.py --buy 100 --entry 10000 --target 350000  # -> value + x
  mcapper.py --buy 100 --entry 10000 --targets 350000 700000 5000000
"""

import argparse
import sys


def position(buy: float, entry_mcap: float, target_mcap: float) -> dict:
    """Return position stats for a buy at a given entry mcap and target mcap."""
    if entry_mcap <= 0 or target_mcap <= 0 or buy <= 0:
        raise ValueError("buy, entry and target must be positive")
    share = buy / entry_mcap
    value = share * target_mcap
    return {
        "buy": buy,
        "entry_mcap": entry_mcap,
        "target_mcap": target_mcap,
        "supply_share_pct": share * 100,
        "value": value,
        "multiple": value / buy,
        "profit": value - buy,
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--buy", type=float, required=True, help="amount spent (USD)")
    p.add_argument("--entry", type=float, required=True, help="entry market cap (USD)")
    p.add_argument("--target", type=float, help="single target market cap (USD)")
    p.add_argument("--targets", type=float, nargs="*", help="multiple target market caps (USD)")
    args = p.parse_args(argv)

    targets = [args.target] if args.target is not None else (args.targets or [])
    if not targets:
        p.error("provide --target or --targets")

    for t in targets:
        try:
            r = position(args.buy, args.entry, t)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
        print(
            f"buy ${r['buy']:,.0f} @ ${r['entry_mcap']:,.0f} mcap "
            f"-> ${r['target_mcap']:,.0f} mcap: "
            f"{r['supply_share_pct']:.4f}% of supply = ${r['value']:,.0f} "
            f"({r['multiple']:,.0f}x, +${r['profit']:,.0f})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

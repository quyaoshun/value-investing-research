#!/usr/bin/env python3
"""Deterministic helpers for value-investing research. Standard library only."""
from __future__ import annotations
import argparse, json


def dcf(fcf0, growth, years, wacc, terminal_growth):
    if wacc <= terminal_growth:
        raise ValueError("wacc must exceed terminal_growth")
    pv = 0.0
    fcf = float(fcf0)
    for t in range(1, years + 1):
        fcf *= 1 + growth
        pv += fcf / ((1 + wacc) ** t)
    terminal = fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal / ((1 + wacc) ** years)
    return {"pv_explicit": pv, "pv_terminal": pv_terminal, "operating_value": pv + pv_terminal}


def metrics(a):
    out = {}
    if "normalized_operating_profit" in a and "tax_rate" in a:
        out["normalized_nopat"] = a["normalized_operating_profit"] * (1-a["tax_rate"])
    if "intrinsic_value" in a and "market_price" in a:
        out["margin_of_safety"] = (a["intrinsic_value"]-a["market_price"])/a["intrinsic_value"]
    if "current_assets" in a and "total_liabilities" in a:
        out["ncav"] = a["current_assets"]-a["total_liabilities"]
    return out


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest="cmd", required=True)
    d=sub.add_parser("dcf")
    d.add_argument("--fcf0",type=float,required=True); d.add_argument("--growth",type=float,required=True)
    d.add_argument("--years",type=int,default=5); d.add_argument("--wacc",type=float,required=True); d.add_argument("--terminal-growth",type=float,required=True)
    m=sub.add_parser("metrics"); m.add_argument("--json",required=True)
    x=p.parse_args()
    if x.cmd=="dcf": r=dcf(x.fcf0,x.growth,x.years,x.wacc,x.terminal_growth)
    else: r=metrics(json.loads(x.json))
    print(json.dumps(r, ensure_ascii=False, indent=2))
if __name__=="__main__": main()


def adjusted_cash(excess_cash, haircut):
    """Shareholder value of excess cash after explicit capital-allocation haircut."""
    return excess_cash * (1.0 - haircut)

def reality_anchor_ratio(steady_state, latest_quarter_actual):
    """Compare a steady-state assumption with annualized latest-quarter actual."""
    annualized = latest_quarter_actual * 4.0
    return steady_state / annualized if annualized != 0 else None

def adjusted_ev(market_cap, debt, excess_cash, haircut=0.0):
    """EV using only the shareholder-valued portion of excess cash."""
    return market_cap + debt - adjusted_cash(excess_cash, haircut)

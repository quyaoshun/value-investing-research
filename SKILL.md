---
name: value-investing-research
description: Deep fundamental and comparative equity research for US-listed stocks and ADRs using Graham-Dodd, Buffett owner earnings, reality-anchor tests, three-lens trend checks, strategic-loss verification, capital-allocation-adjusted cash, DCF/EPV/Graham/tangible-book cross-checks, forced falsification, and event-driven monitoring. Use for single-stock value-investing reports, intrinsic-value analysis, or apples-to-apples comparisons between two or more stocks. Do not use for short-term trading signals or personalized investment instructions.
---

# Value Investing Research v2.0

Produce source-driven, auditable value-investing research. The goal is not to tell a persuasive story; it is to expose what is known, what is estimated, what cannot be verified, what the valuation assumes, and what future evidence would overturn the conclusion.

## 0. Mandatory data integrity gate

Before analysis, freeze the data basis:
- ticker/company, listing venue, ordinary-share/ADS ratio;
- reporting currency, market-price currency, FX rate and FX date;
- price/as-of date, market cap and share-count date;
- latest annual/interim/quarterly filing dates;
- segment definitions and any reclassification breaks.

For ADRs/cross-currency stocks, never combine balance-sheet CNY/HKD/etc. with USD market cap before conversion. Prefer modeling in the financial-statement currency and convert only per-share/equity outputs once. Reconcile market cap from price × diluted shares/ADSs where possible.

Label every material input as one of: `[R]` company-reported, `[C]` calculated, `[E]` estimate/assumption, `[3P]` third-party estimate. Never present `[3P]` as company disclosure.

## 1. Research hierarchy

1. Primary filings and official earnings materials.
2. Official regulator/government sources for regulatory facts.
3. Credible third-party research/news for industry context or undisclosed variables.
4. Aggregators only as discovery/cross-check tools; recompute important ratios.

If a decisive input is not disclosed, say **“不可独立验证 / not independently verifiable”**. Do not manufacture precision by reverse-engineering an unsupported number.

## 2. Business-model physics

Analyze the economic architecture before valuation: platform vs first-party, asset intensity, inventory ownership, fulfillment burden, gross margin, operating margin, capex/revenue, working-capital model, employee intensity, revenue/profit per employee, network effects, switching costs, and reinvestment requirements.

For comparisons, explicitly separate **business quality** from **valuation**. A superior business is not automatically the cheaper security. Test whether differences in margin/asset intensity have already been absorbed by P/S, P/B, EV/Sales or other upstream multiples, and whether forward P/E / EV-FCF / FCF yield converge downstream.

## 3. Earnings normalization and strategic-loss map

Build reported → normalized operating profit → NOPAT → FCF/owner-earnings bridges. Inspect investment gains/losses, impairments, disposals, SBC, interest income, minority interests, subsidies, one-time items, and temporary strategic spending.

For every large loss-making strategic initiative, record:
- disclosed separately? yes/no;
- latest actual quarterly loss or closest observable proxy;
- internally controllable vs externally imposed driver;
- management can stop/scale it? yes/no/partial;
- current direction of loss and revenue contribution;
- evidence source and confidence.

Never normalize a strategic loss away merely because management calls it investment.

## 4. Reality-anchor test (mandatory)

Any steady-state assumption for a currently loss-making or abnormally depressed business must be compared with the latest actual run-rate.

`reality_anchor = latest_quarter_actual × 4` (or a more appropriate disclosed run-rate).

Report `steady_state_assumption / reality_anchor` and explain the gap. Default red flag: the assumed steady-state loss/profit improvement is more than 50% away from the latest annualized actual without concrete evidence for the bridge.

If the company does not disclose the input needed for the test:
1. mark the test **FAILED: INPUT UNAVAILABLE** rather than passing it;
2. identify any `[3P]` proxy separately;
3. apply an explicit uncertainty/verifiability adjustment in scenario value or non-operating-asset treatment instead of silently hiding it in WACC;
4. make disclosure improvement a monitoring trigger.

## 5. Three-lens trend test (mandatory)

For the dominant earnings/revenue variable, show all three when data permit:
- YoY: latest quarter vs same quarter last year;
- QoQ/sequential: latest quarter vs immediately prior quarter;
- YTD annualized or LTM vs prior full year.

Do not call an inflection from one lens alone. Explain base effects and why the lenses agree or conflict. For 6-8 recent quarters, include earnings-surprise history when reliable consensus data are available; use it as evidence about predictability, not as a trading signal.

## 6. Cash-flow and balance-sheet quality

Reconcile OCF to earnings and quantify working-capital contribution. For structurally negative-working-capital retailers/platforms, distinguish supplier/customer financing from durable distributable cash.

Calculate current/quick ratios where meaningful, debt, net debt, interest coverage, tangible assets, goodwill, receivables, inventory, minority interests, NCAV, and Piotroski F-Score where inputs are reliable. Interpret rather than mechanically score.

Owner earnings = NOPAT - minority-interest economic claim + D&A - maintenance capex - necessary working-capital increase.

Default necessary working-capital benefit to zero when historical benefits are not safely repeatable.

## 7. Capital allocation: cash is not automatically worth par

Review dividends, actual repurchases, dilution/SBC, acquisitions/investments, and explicit management statements about returning capital.

Separate:
- operating cash required for the business;
- genuinely excess/non-operating cash;
- cash legally/operationally trapped or strategically committed;
- cash that management has demonstrated willingness to return.

If management behavior makes excess cash less valuable to minority shareholders, use an **explicit capital-allocation haircut** and show sensitivity. Never bury this haircut in WACC.

`shareholder_value_of_cash = excess_cash × (1 - haircut)`

Haircut must be evidence-based and scenario-tested, not asserted as fact. At minimum show 0%, base haircut, and a harsher case when cash treatment is thesis-critical. State the **reversal trigger** (e.g. material dividend/buyback announcement) that would invalidate the haircut.

## 8. ROIC and competitive durability

Calculate normalized NOPAT / average invested capital and disclose the invested-capital definition. Compare with a documented WACC assumption. Explain whether value creation comes from operating returns, leverage, float/supplier financing, or asset-light economics.

Perform competitive due diligence: identify major rivals, where each competitor is investing, whether the company is forced to respond, and whether apparent margin improvement is sustainable under rational competitive response.

## 9. Valuation architecture

Use multiple methods; DCF is primary, not sacred:
- operating-asset DCF;
- EPV where normalized economics are defensible;
- conservative Graham-style earnings formula where applicable;
- tangible book / liquidation anchors where economically relevant;
- market-multiple comparison only as a cross-check.

Operating-asset DCF equity value = PV(operating FCF) + shareholder-value-of-non-operating-assets - debt/senior claims - minority-interest adjustments.

Use bear/base/bull scenarios. Change the dominant economic variables, not cosmetic assumptions. Avoid probability weights unless justified. If combining methods, disclose weights and why; never let a low-quality method dominate simply because it outputs a number.

Show sensitivity for the one or two variables with the highest valuation elasticity. For comparisons, use the same date, currency treatment, metric definitions, and calculation script across companies.

## 10. Forced falsification (mandatory)

Before the conclusion, add **“本报告最可能错在哪里 / Where this report is most likely wrong”** containing:
1. the single assumption the conclusion depends on most;
2. a sensitivity table around that assumption;
3. the exact threshold where the conclusion materially changes;
4. the strongest reasonable counterargument;
5. 3-6 observable data points/events in the next 1-2 reporting periods that would adjudicate the thesis.

A good thesis must be falsifiable by future evidence. If no observable test exists, lower confidence explicitly.

## 11. Comparative mode

When comparing two or more stocks, follow `references/comparison-protocol.md` and do not merely place two standalone reports side by side.

Required comparison axes:
- business-model physics;
- normalized profitability and capital intensity;
- same-basis valuation convergence/divergence;
- strategic-loss controllability and disclosure;
- earnings predictability;
- capital return and cash accessibility;
- risk structure (internal/controllable vs external/non-controllable);
- verifiability of the key thesis inputs;
- falsification triggers and next adjudication date.

Do not collapse these axes into one opaque score. State trade-offs directly.

## 12. Revision protocol

For every revision keep a change log:
`old assumption → new evidence → new assumption → valuation impact → conclusion impact`.

If a segment definition changes, mark the comparability break and replace broken monitoring metrics with observable proxies. If new evidence materially changes intrinsic value, margin of safety, or a key risk, revise the conclusion instead of defending the old one.

## 13. Deterministic calculations

Use `scripts/valuation.py` when useful. Show formulas, units and source dates. Required formulas include:
- Normalized NOPAT = normalized operating profit × (1 - normalized tax rate)
- Normalized FCF = NOPAT - minority claim + D&A - normalized capex - necessary WC increase
- ROIC = normalized NOPAT / average invested capital
- NCAV = current assets - total liabilities
- Margin of safety = (intrinsic value - market price) / intrinsic value
- Adjusted excess cash = excess cash × (1 - capital-allocation haircut)
- Reality-anchor ratio = steady-state assumption / annualized latest actual

## 14. Output

Follow `references/report-structure.md`. Write in Chinese when the user writes in Chinese unless asked otherwise. Separate facts, assumptions, calculations, third-party estimates, and interpretations. Use compact tables for comparisons. Avoid hype, certainty language, and personalized buy/sell instructions. End with a source table and non-advisory note.

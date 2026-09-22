# Language and financial terminology / 语言与财务术语

Read when composing a report in English, Chinese, or both. Language selection is defined in SKILL.md.

## Presentation

Use natural financial prose in the selected language, including all report headings and table labels. In Chinese, give the English acronym at the first mention of a technical term where useful; in English, do not add Chinese translations unless requested. Use Simplified or Traditional Chinese as selected, including translated terms below.

For bilingual reports, use paired Chinese/English headings and consecutive language versions within each section. Use one shared numeric table with bilingual labels rather than independently calculated copies. A request for an English summary and Chinese body requires only that split, not a full duplicate report.

Retain company/ticker identifiers, filing form names (10-K, 20-F), URLs, code paths, CLI flags, and JSON keys unchanged. Keep source titles as published, optionally followed by a translated title. Mark translated quotations as translations; keep quoted text distinct from the analyst's interpretation. Source language does not determine report language. Prefer authoritative primary sources in either language over weaker sources merely available in the requested language.

## Consistent terminology

| English | 简体中文 |
| --- | --- |
| Owner earnings | 所有者盈余 |
| Normalized earnings | 正常化盈利 |
| Reality-anchor test | 现实锚检验 |
| Three-lens trend test | 趋势三口径检验 |
| Excess cash | 超额现金 |
| Capital-allocation haircut | 资本配置折价 |
| Margin of safety | 安全边际 |
| Net current asset value (NCAV) | 净流动资产价值（NCAV） |
| Earnings power value (EPV) | 盈利能力价值（EPV） |
| Tangible book value | 有形账面价值 |
| Forced falsification | 强制自证伪 |
| Reversal threshold | 结论反转阈值 |
| Bear / Base / Bull | 悲观 / 基准 / 乐观 |

Preserve the evidence tags while explaining them in the selected language: `[R]` reported / 公司披露, `[C]` calculated / 计算所得, `[E]` assumption / 估计或假设, `[3P]` third-party estimate / 第三方估计.

When an input is missing, preserve the auditable status `FAILED: INPUT UNAVAILABLE`, adding “检验未通过：输入数据缺失” in Chinese reports. Explain that this is a data-availability failure, not proof of business deterioration. Translate “not independently verifiable” as “不可独立验证”; never turn unavailable data into zero.

## Numbers, dates, and currencies

State currency and scale on every monetary table (for example, CNY million / 人民币百万元). Language choice must not silently switch the modeling currency or price date. If the user requests localized scales, convert every affected value and label together: 1 万 = 10,000; 1 亿 = 100 million; 1 billion = 10 亿; 1 万亿 = 1 trillion. For example, CNY 39.4 billion = 人民币 394 亿元, not 39.4 亿元.

Use unambiguous dates such as YYYY-MM-DD. Distinguish percentage changes from percentage-point changes (百分点). Keep ratios, ADS/share conventions, signs, rounding precision, and valuation conclusions identical across translations. Translate displayed script results if useful, but preserve machine-readable field names and numeric values.

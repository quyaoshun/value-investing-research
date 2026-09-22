# 价值投资研究 v2.2 / Value Investing Research

以中文为主编写的价值投资研究 Skill，支持美股及 ADR 单公司深度分析与同口径股票对比，也支持完整英文报告。

研究框架包含 Graham-Dodd、巴菲特所有者盈余、现实锚检验、趋势三口径、战略亏损分析、超额现金折价、多方法估值交叉验证，以及带反转阈值的强制自证伪。

v2.2 将主流程、参考文档、界面提示及脚本说明改为中文优先，保留必要英文术语、英文使用示例与安装说明。明确指定的输出语言优先；否则跟随提问语言，支持简体、繁体及按需双语输出。

## 安装到 Codex

本仓库根目录就是完整的 `value-investing-research` Skill。私有仓库需要先登录有访问权限的 GitHub 账户。

### 使用 skill-installer

在 Codex 中输入：

```text
$skill-installer 从 https://github.com/quyaoshun/value-investing-research 安装 Skill，仓库内路径为 .，安装名称为 value-investing-research。
```

### 手动安装

将仓库克隆到用户级 Skills 目录；若目标目录已经存在，请先检查已有内容，避免覆盖。

```bash
mkdir -p "$HOME/.agents/skills"
gh repo clone quyaoshun/value-investing-research "$HOME/.agents/skills/value-investing-research"
```

## 使用示例

```text
$value-investing-research 深度对比 PDD 和 JD，使用最新财报和同一交易日价格，输出完整中文价值投资报告。
```

## 目录与运行要求

- `SKILL.md`：研究流程、数据口径及自证伪规则。
- `agents/openai.yaml`：Skill 展示信息及默认提示。
- `scripts/valuation.py`：确定性估值辅助计算，仅依赖 Python 3 标准库。
- `references/report-structure.md`：报告结构和表格清单。
- `references/comparison-protocol.md`：同口径多公司比较规则。
- `references/language-guide.md`：中英文术语、双语排版和金额单位规范。

计算示例（在仓库目录运行）：

```bash
python3 scripts/valuation.py dcf --fcf0 100 --growth 0.05 --years 5 --wacc 0.10 --terminal-growth 0.02
python3 scripts/valuation.py metrics --json '{"intrinsic_value":100,"market_price":70,"current_assets":200,"total_liabilities":120}'
```

增长率、折现率均以小数输入；金额必须使用一致的币种和单位。DCF 输出为经营资产价值，仍需按研究流程调整现金、债务及其他权益要求。现金折价和现实锚辅助函数可通过 Python 导入，尚未提供独立命令行子命令。

本包提供研究方法和估值辅助脚本，不包含自动抓取财报、行情或自动生成 PDF 的完整管线。研究时需要另行获取并核验一手数据。

## 来源与范围

此 Skill 根据此前提供的研究报告逆向整理研究方法，不代表报告原作者的私有 Skill。仓库不包含原始 PDF 研究报告。研究输出仅用于信息分析，不构成个性化投资建议。


## 中英文使用 / Language examples

```text
$value-investing-research 分析 BABA，以最新财报为准，用简体中文输出。
$value-investing-research 分析 PDD，請用繁體中文呈現估值與風險。
$value-investing-research Compare GOOG and META using the latest filings and same-date prices. Write the report in English.
$value-investing-research 分析 JD，完整报告用英文输出。
$value-investing-research Compare PDD and JD. Use a Chinese body with an English executive summary.
$value-investing-research 对比 PDD 和 JD，输出中英双语报告，共用一套估值数据和来源。
```

股票代码、英文财报或英文默认提示不会覆盖用户的语言选择；只有股票代码时沿用当前对话语言，无对话语言时默认中文。

## 英文安装说明 / Installation (English)

This Skill is authored primarily in Chinese and supports full English reports with the same methodology. The repository root is the complete Skill. For this private repository, authenticate with a GitHub account that has access.

Ask Codex:

```text
$skill-installer Install https://github.com/quyaoshun/value-investing-research using repository path . and installation name value-investing-research.
```

Or clone it into the user Skills directory. Inspect any existing destination before proceeding to avoid overwriting it:

```bash
mkdir -p "$HOME/.agents/skills"
gh repo clone quyaoshun/value-investing-research "$HOME/.agents/skills/value-investing-research"
```

## 英文使用说明 / Usage and package contents (English)

Explicit output-language instructions take precedence over the language of the prompt. Otherwise the report follows the substantive request language, preserving Simplified or Traditional Chinese. Mixed-language prompts use the main prose language. Ticker-only prompts inherit the conversation language, defaulting to Chinese when none exists. Bilingual reports are produced when requested and share figures, assumptions, and sources.

- `SKILL.md`: research workflow, evidence requirements, and language selection.
- `agents/openai.yaml`: bilingual display metadata and default prompt.
- `scripts/valuation.py`: deterministic valuation helpers using only the Python 3 standard library.
- `references/report-structure.md`: report sections and suggested tables.
- `references/comparison-protocol.md`: same-basis comparisons.
- `references/language-guide.md`: terminology, bilingual presentation, and monetary scales.

Run the calculation commands shown above from the repository directory. Rates are decimals; monetary inputs must share a currency and scale. DCF returns operating-asset value, requiring subsequent cash, debt, and other equity-claim adjustments. Cash-haircut and reality-anchor helpers are Python functions, not separate CLI subcommands. CLI flags and JSON keys remain in English in either report language.

This package supplies a research methodology and calculation helpers. It does not include a complete pipeline for fetching filings/prices or generating PDFs; authoritative research inputs must be obtained and verified separately. The methodology was reconstructed from previously supplied reports and is not represented as their author's private Skill. Original PDF reports are excluded. Outputs are informational research, not personalized investment advice.

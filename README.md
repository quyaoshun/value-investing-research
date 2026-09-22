# Value Investing Research v2.0

Installable agent skill for rigorous single-stock and comparative value-investing research.

v2.0 adds: mandatory reality-anchor tests, three-lens trend analysis, strategic-loss controllability/disclosure mapping, explicit capital-allocation haircuts for excess cash, same-basis comparison mode, valuation-convergence analysis, forced falsification with reversal thresholds, and event-driven monitoring.

Example:
`$value-investing-research compare PDD and JD using the latest filings, same-date valuation, reality-anchor tests, cash-accessibility adjustments, and forced falsification.`

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

计算示例（在仓库目录运行）：

```bash
python3 scripts/valuation.py dcf --fcf0 100 --growth 0.05 --years 5 --wacc 0.10 --terminal-growth 0.02
python3 scripts/valuation.py metrics --json '{"intrinsic_value":100,"market_price":70,"current_assets":200,"total_liabilities":120}'
```

增长率、折现率均以小数输入；金额必须使用一致的币种和单位。DCF 输出为经营资产价值，仍需按研究流程调整现金、债务及其他权益要求。现金折价和现实锚辅助函数可通过 Python 导入，尚未提供独立命令行子命令。

本包提供研究方法和估值辅助脚本，不包含自动抓取财报、行情或自动生成 PDF 的完整管线。研究时需要另行获取并核验一手数据。

## 来源与范围

此 Skill 根据此前提供的研究报告逆向整理研究方法，不代表报告原作者的私有 Skill。仓库不包含原始 PDF 研究报告。研究输出仅用于信息分析，不构成个性化投资建议。

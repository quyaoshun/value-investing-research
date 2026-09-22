# 语言与财务术语 / Language Guide

撰写中文、英文或双语报告时使用。输出语言的选择遵循 `SKILL.md`；本文使用中文不代表所有报告都必须使用中文。

## 呈现方式

正文、章节标题与表头均使用选定语言，以自然的财务研究表达为准。中文报告首次使用专业术语时，按需附英文名称或缩写；英文报告除非用户要求，不附中文翻译。中文术语随用户选择使用简体或繁体。

双语报告使用中英文对应标题，在每节内依次呈现两种语言。数字表共用一套数据并使用双语标签，避免重复计算。用户只要求“中文正文、英文摘要”时，仅按该分工输出，无需全文双语。

保留公司及股票标识、申报文件名称（10-K、20-F）、网址、代码路径、命令行参数及 JSON 字段名。来源标题保留原文，可附译名。译文引语须标记为翻译，并与研究者判断区分。资料语言不决定报告语言；优先使用权威的一手资料，不为匹配输出语言而改用较弱来源。

## 统一术语

| 中文 | English |
| --- | --- |
| 所有者盈余 | Owner earnings |
| 正常化盈利 | Normalized earnings |
| 现实锚检验 | Reality-anchor test |
| 趋势三口径检验 | Three-lens trend test |
| 超额现金 | Excess cash |
| 资本配置折价 | Capital-allocation haircut |
| 安全边际 | Margin of safety |
| 净流动资产价值（NCAV） | Net current asset value |
| 盈利能力价值（EPV） | Earnings power value |
| 有形账面价值 | Tangible book value |
| 强制自证伪 | Forced falsification |
| 结论反转阈值 | Reversal threshold |
| 悲观 / 基准 / 乐观 | Bear / Base / Bull |

保留证据标签，并用报告语言解释：`[R]` 公司披露（reported）、`[C]` 计算所得（calculated）、`[E]` 估计或假设（estimate/assumption）、`[3P]` 第三方估计（third-party estimate）。

输入缺失时，保留可追溯的状态码 `FAILED: INPUT UNAVAILABLE`，中文报告先写“检验未通过：输入数据缺失”。说明这是数据可用性不足，不代表业务已经恶化。“not independently verifiable”译为“不可独立验证”；不得将缺失数据当作零。

## 数字、日期与币种

每张金额表均注明币种与数量级，例如“人民币百万元 / CNY million”。不能因输出语言变化就切换建模币种或股价日期。用户要求转换数量级时，同步换算所有受影响数字及表头：

- 1 万 = 10,000
- 1 亿 = 100 million
- 1 billion = 10 亿
- 1 万亿 = 1 trillion

例如 CNY 39.4 billion = 人民币 394 亿元，不能写成 39.4 亿元。

日期使用 YYYY-MM-DD 等无歧义格式。区分百分比变化与百分点变化（percentage points）。不同语言版本须保持比率、ADS/普通股口径、正负号、舍入精度和估值结论一致。脚本结果可按需翻译展示，但机器可读字段名及其数值保持不变。

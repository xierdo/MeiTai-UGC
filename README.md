# MeiTai UGC — Thai TikTok UGC Creative v1.0

An AI agent skill for Thai TikTok Shop haircare and beauty UGC: creative strategy, localized Thai dialogue, product-reference fidelity, video prompts and quality checks.

面向泰国 TikTok Shop 洗护、美妆短视频的独立 Agent Skill。核心指令简洁，详细规则按需读取；不依赖网络、API Key 或第三方 Python 库。不是视频生成器或自动投放系统。

## 使用
将完整 `thai-tiktok-ugc-creative/` 文件夹放入当前 Codex 环境可识别的 skills 目录。保留目录结构；具体路径以客户端版本及工作区配置为准。可以先在 Codex 中要求读取该文件夹的 SKILL.md 并按其工作，再配置持久技能发现。没有执行自动安装脚本。

示例请求：
- 使用 thai-tiktok-ugc-creative，基于我提供的产品图写 3 条 15–20 秒泰国 UGC 脚本，英文指令、泰语对白、中文翻译，每条不超过 2500 字符。
- 使用 thai-tiktok-ugc-creative，审核这条脚本的泰语自然度、物理可执行性及产品一致性，尽量保留原剧情。
- 使用 thai-tiktok-ugc-creative，把这条参考广告拆解为功能模块，再生成两条符合当前产品事实的变体。

## 字符校验
在技能目录运行：`python scripts/check_prompt.py examples/beauty-store-28s.txt --max 2500`。
默认 Unicode 码点，同时输出 UTF-16 单元与 UTF-8 字节。若目标平台按 UTF-16 或字节限制，分别加 `--unit utf16` 或 `--unit bytes`。不自动去除空格、换行或 BOM；请确保校验的文件与最终粘贴内容相同。平台计数仍须实际验证。

## 版本说明
v1.0 采用独立实现：借鉴四次销售、先 brief 再脚本、认知阶段、爆款结构与创意变量控制；增加泰语对白、参考图分工、发质锁定、剪辑逻辑、字符校验和真实广告审核。营销来源记录于 references/marketing.md。产品库、真实投放数据、参考图片为外部资产；示例不代表真实门店销售或已验证效果。未安装进用户账户，也未实际调用视频生成或投放系统；泰语未做母语者录音审核。

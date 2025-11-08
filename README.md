# Auto dosbox_asm
# 🚀MASM8086 一键汇编运行工具 🚀
一个开箱即用的 MASM8086 汇编环境 + 优雅高效的代码运行方案，彻底告别配置烦恼和繁琐操作！

## 🤔 解决的核心痛点
1. ❌ Windows 下 MASM8086 环境配置复杂，依赖缺失、路径混乱频发
2. ❌ DOSBox 手动操作繁琐：反复输入 `masm`/`link` 命令，步骤冗余，运行体验差
3. ❌ 临时文件管理麻烦，汇编-链接-运行流程割裂

## ✨ 核心成果
✅ **零配置开箱即用**：仓库内置完整 MASM8086 编译工具链（masm.exe + link.exe），git clone 后直接上手  
✅ **一键自动化运行**：Python 脚本封装全流程，无需手动敲命令，代码执行更优雅  
✅ **智能环境适配**：自动识别 DOSBox 路径，支持自定义指定，兼容多系统安装目录  
✅ **干净无残留**：自动生成临时脚本，运行后自动清理，不污染工作目录  

## 📦 环境准备
1. **安装 Python**：确保系统已安装 Python 3.6+（下载地址：[https://www.python.org/downloads/）](https://www.python.org/downloads/）)
2. **安装 DOSBox**：
    - 推荐版本：DOSBox-0.74-3（兼容稳定性最佳）
    - 仓库内的“dosbox安装包”文件夹下已经准备好了安装包，安装即可
3. **克隆仓库**：

```bash
git clone <仓库地址>
cd <仓库目录>
```

## 🚀 快速使用
### 基础用法（自动查找 DOSBox）
```bash
python run_asm.py <你的汇编文件名>
```

👉 示例：运行 `test.asm`

```bash
python run_asm.py test.asm
```

👉或省略 .asm 后缀（脚本自动补全）

```bash
python run_asm.py test
```

### 自定义 DOSBox 路径（可选）
如果 DOSBox 未安装在默认目录，手动指定路径：

```bash
python run_asm.py <你的汇编文件名> --dosbox "E:\DOSBox-0.74-3\DOSBox.exe"
```

### 永久配置 DOSBox 路径（推荐）
直接修改脚本内默认路径，无需每次手动输入：  
打开 `run_asm.py`，找到以下代码并修改为你的 DOSBox 路径：

```python
if __name__ == "__main__":
    # 直接填写你的 DOSBox 完整路径（字符串格式）
    dosbox=Path("E:\DOSBox-0.74-3\DOSBox.exe")
    main(dosbox_path=dosbox)
```

## 🔍 工作流程揭秘
1. 📝 脚本自动检查汇编文件（支持带/不带 `.asm` 后缀）
2. 🔧 验证 masm.exe 和 link.exe 是否存在（仓库已内置，无需额外配置）
3. 📜 生成随机临时 BAT 脚本（自动执行汇编-链接-运行全流程）
4. 🖥️ 启动 DOSBox，自动挂载工作目录并执行脚本
5. 🧹 运行结束后自动删除临时文件，干净无残留

## 📋 目录结构说明
```plain
├── run_asm.py          # 核心一键运行脚本
├── masm.exe            # MASM 汇编器（内置）
├── link.exe            # 链接器（内置）
├── your_code.asm       # 你的汇编源代码（自定义）
└── README.md           # 使用说明
└─dosbox安装包  				# 存放dosbox安装包
```

## ⚠️ 注意事项
1. 汇编文件名建议使用英文/数字，避免中文路径和特殊字符
2. 确保 DOSBox 路径正确（默认支持常见安装目录，自定义路径需用引号包裹）
3. 脚本会自动清理临时 BAT 文件，若运行中断可手动删除残留文件
4. 仅支持 MASM8086 汇编语法，其他汇编语法需自行适配

## 🎉 优势总结
| 传统方式 | 本工具方式 |
| --- | --- |
| 手动配置环境，步骤繁琐 | 零配置，clone 即使用 |
| 反复输入 masm/link 命令 | 一键运行，自动完成全流程 |
| 手动管理临时文件 | 自动清理，目录整洁 |
| 路径配置易出错 | 智能识别，支持自定义路径 |


让汇编编程更专注于代码本身，告别环境配置和繁琐操作的困扰！🎉


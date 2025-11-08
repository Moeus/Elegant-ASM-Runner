# 使用方法，
# python run_asm.py <ASM filename> [--dosbox <path>]
# ASM filename是指
# 括号内内容为可选的
import os
import sys
import subprocess
from pathlib import Path
import random
import string


def random_8_3():
    prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{prefix}.BAT"


def main(dosbox_path:str=""):
    if len(sys.argv) < 2:
        print("Usage: python run_asm.py <ASM filename> [--dosbox <path>]")
        sys.exit(1)

    asm_name = sys.argv[1]
    # 防呆设计，可能带后缀也可能不带后缀
    if asm_name[-4:]==".asm":
        asm_file=Path(asm_name)
        asm_name=asm_name[:-4]
    else :
        asm_file = Path(f"{asm_name}.asm")
        
    custom_dosbox = None

    # Parse --dosbox parameter
    if "--dosbox" in sys.argv:
        idx = sys.argv.index("--dosbox")
        if idx + 1 >= len(sys.argv):
            print("Error: --dosbox requires a path")
            sys.exit(1)
        custom_dosbox = sys.argv[idx + 1]

    current_dir = Path.cwd().resolve()

    # Check ASM file
    if not asm_file.exists():
        print(f"Error: ASM file not found: {asm_file.resolve()}")
        sys.exit(1)

    # Check MASM and LINK
    for tool in ["masm.exe", "link.exe"]:
        tool_path = current_dir / tool
        if not tool_path.exists():
            print(f"Error: Missing {tool} in current directory. Path: {tool_path}")
            sys.exit(1)

    # Create temporary BAT file
    bat_filename = random_8_3()
    bat_path = current_dir / bat_filename

    # ✅ 新版 BAT：只运行，不打印多余内容
    with open(bat_path, "w", encoding="ascii") as f:
        f.write(f"""
masm {asm_name}.asm;
link {asm_name}.obj;
{asm_name}.exe
""")

    # Find DOSBox
    def find_dosbox():
        if custom_dosbox:
            p = Path(custom_dosbox)
            if p.exists() and p.is_file():
                return str(p)
            print(f"Error: invalid DOSBox path: {custom_dosbox}")
            sys.exit(1)

        default_paths = [
            r"C:\Program Files\DOSBox-0.74-3\DOSBox.exe",
            r"C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe",
            r"D:\Program Files\DOSBox-0.74-3\DOSBox.exe",
            dosbox_path
        ]

        for p in default_paths:
            if Path(p).exists():
                return p

        try:
            subprocess.run(["dosbox", "--version"],
                           capture_output=True,
                           check=True,
                           text=True)
            return "dosbox"
        except Exception:
            return None

    dosbox = find_dosbox()
    if not dosbox:
        print("Error: DOSBox not found. Use --dosbox <path> to specify manually.")
        sys.exit(1)

    print(f"[Python] Using DOSBox: {dosbox}")
    print(f"[Python] Running: {bat_filename}")

    # Run DOSBox
    try:
        subprocess.run([
            dosbox,
            "-c", f"mount d \"{current_dir}\"",
            "-c", "d:",
            "-c", bat_filename,
            "-c", "exit"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[Python] DOSBox execution failed: {e}")
    finally:
        try:
            if bat_path.exists():
                bat_path.unlink()
                print(f"[Python] Deleted temporary BAT: {bat_filename}")
        except Exception as e:
            print(f"[Python] Warning: failed to delete {bat_filename}: {e}")

    print("[Python] Done.")


if __name__ == "__main__":
    # 将dosbox的路径写在Path括号内，字符串形式
    dosbox=Path("E:\DOSBox-0.74-3\DOSBox.exe")
    main(dosbox_path=dosbox)
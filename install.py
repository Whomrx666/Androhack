#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AndroHack Installer & Setup Utility
Author : Mr.X
Website: https://whomrx.pages.dev
Blog   : https://whomrxhackers.blogspot.com
Github : https://github.com/Whomrx666
Bot    : https://whomrx-bot.netlify.app
Market : https://whomrx-market.pages.dev
"""

import os
import sys
import shutil
import platform
import subprocess
import importlib.util
import time

# ==================== ANSI COLOR CODES ====================
class ANSI:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"

# ==================== BANNER (INSTALLER) ====================
INSTALLER_BANNER = r"""
  _____           _        _ _           
  \_   \_ __  ___| |_ __ _| | | ___ _ __ 
   / /\/ '_ \/ __| __/ _` | | |/ _ \ '__|
/\/ /_ | | | \__ \ || (_| | | |  __/ |   
\____/ |_| |_|___/\__\__,_|_|_|\___|_|   
                                         
"""

# ==================== CONFIG ====================
REQUIRED_PYTHON_MODULES = ["rich"]
ANDROHACK_SCRIPT = "androhack.py"

# ==================== UTILITY FUNCTIONS ====================
def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_info():
    """Detect operating system / terminal type."""
    system = platform.system()
    if os.environ.get("TERMUX_VERSION"):
        return "Termux (Android)"
    elif system == "Linux":
        return "Linux"
    elif system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "macOS"
    else:
        return system if system else "Unknown"

def print_separator(char="═"):
    """Print a separator line across terminal width."""
    try:
        width = shutil.get_terminal_size().columns
    except:
        width = 80
    print(f"{ANSI.CYAN}{ANSI.BOLD}{char * width}{ANSI.RESET}")

def print_banner():
    """Display installer banner."""
    clear_screen()
    print(f"{ANSI.MAGENTA}{ANSI.BOLD}{INSTALLER_BANNER}{ANSI.RESET}")
    print()
    print(f"{ANSI.CYAN}{ANSI.BOLD}  AndroHack Installer & Setup Utility{ANSI.RESET}")
    print(f"{ANSI.DIM}  Author : {ANSI.WHITE}Mr.X{ANSI.RESET}")
    print(f"{ANSI.DIM}  Website: {ANSI.WHITE}https://whomrx.pages.dev{ANSI.RESET}")
    print()
    print_separator()

def check_python():
    """Check Python version."""
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major < 3 or (major == 3 and minor < 6):
        print(f"{ANSI.RED}{ANSI.BOLD}✗ Python 3.6 or higher is required!{ANSI.RESET}")
        sys.exit(1)
    return f"{major}.{minor}.{sys.version_info.micro}"

def check_pip():
    """Check if pip is available."""
    pip_cmd = None
    for cmd in ["pip3", "pip"]:
        if shutil.which(cmd):
            pip_cmd = cmd
            break
    return pip_cmd

def check_module(module_name):
    """Check if Python module is installed."""
    return importlib.util.find_spec(module_name) is not None

def install_module(module_name, pip_cmd):
    """Install a Python module using pip."""
    print(f"{ANSI.YELLOW}  ⚡ Installing {module_name}...{ANSI.RESET}")
    try:
        subprocess.check_call([pip_cmd, "install", module_name],
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def check_adb():
    """Check if adb is installed."""
    return shutil.which("adb") is not None

def get_adb_install_command(terminal):
    """Return installation command for adb based on OS."""
    if terminal == "Termux (Android)":
        return "pkg install android-tools -y"
    elif terminal == "Linux":
        return "sudo apt install adb -y"
    elif terminal == "Windows":
        return None  # manual download
    elif terminal == "macOS":
        return "brew install android-platform-tools"
    else:
        return None

def install_adb(terminal):
    """Try to install ADB automatically for supported terminals."""
    cmd = get_adb_install_command(terminal)
    if cmd is None:
        if terminal == "Windows":
            print(f"{ANSI.YELLOW}  Please download ADB manually from:{ANSI.RESET}")
            print(f"{ANSI.WHITE}  https://developer.android.com/studio/releases/platform-tools{ANSI.RESET}")
        else:
            print(f"{ANSI.YELLOW}  ADB installation is not automated for this OS.{ANSI.RESET}")
        return False
    print(f"{ANSI.YELLOW}  Running: {cmd}{ANSI.RESET}")
    try:
        subprocess.check_call(cmd, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def prompt_yes_no(question):
    """Ask a yes/no question."""
    while True:
        answer = input(f"{ANSI.YELLOW}{ANSI.BOLD}{question} (y/n): {ANSI.RESET}").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print(f"{ANSI.RED}  Please answer 'y' or 'n'.{ANSI.RESET}")

def run_androhack():
    """Launch AndroHack main script."""
    if not os.path.exists(ANDROHACK_SCRIPT):
        print(f"{ANSI.RED}{ANSI.BOLD}✗ {ANDROHACK_SCRIPT} not found in current directory!{ANSI.RESET}")
        return False
    print(f"{ANSI.CYAN}{ANSI.BOLD}  🚀 Launching AndroHack...{ANSI.RESET}")
    time.sleep(1)
    subprocess.call([sys.executable, ANDROHACK_SCRIPT])
    return True

# ==================== MAIN ====================
def main():
    print_banner()

    # Detect terminal
    terminal = get_terminal_info()
    print(f"  {ANSI.CYAN}{ANSI.BOLD}Terminal:{ANSI.RESET} {ANSI.WHITE}{terminal}{ANSI.RESET}")

    # Check Python version
    python_version = check_python()
    print(f"  {ANSI.CYAN}{ANSI.BOLD}Python  :{ANSI.RESET} {ANSI.WHITE}version {python_version}{ANSI.RESET}")
    print_separator()

    # Check pip
    pip_cmd = check_pip()
    if not pip_cmd:
        print(f"{ANSI.RED}{ANSI.BOLD}✗ pip not found! Please install pip first.{ANSI.RESET}")
        sys.exit(1)
    print(f"  {ANSI.GREEN}✓ pip found: {pip_cmd}{ANSI.RESET}")

    # Check and install required Python modules
    missing_modules = []
    for module in REQUIRED_PYTHON_MODULES:
        if check_module(module):
            print(f"  {ANSI.GREEN}✓ {module} already installed{ANSI.RESET}")
        else:
            print(f"  {ANSI.YELLOW}⚠ {module} not found{ANSI.RESET}")
            missing_modules.append(module)

    if missing_modules:
        print()
        print(f"{ANSI.MAGENTA}{ANSI.BOLD}  Installing missing modules...{ANSI.RESET}")
        for module in missing_modules:
            if install_module(module, pip_cmd):
                print(f"  {ANSI.GREEN}✓ {module} installed successfully{ANSI.RESET}")
            else:
                print(f"  {ANSI.RED}✗ Failed to install {module}{ANSI.RESET}")
                print(f"  {ANSI.YELLOW}  Try manually: {pip_cmd} install {module}{ANSI.RESET}")
                sys.exit(1)

    # Check ADB
    print_separator()
    if check_adb():
        print(f"  {ANSI.GREEN}✓ ADB is installed{ANSI.RESET}")
    else:
        print(f"  {ANSI.YELLOW}⚠ ADB not found{ANSI.RESET}")
        if prompt_yes_no("Do you want to install ADB now?"):
            if install_adb(terminal):
                if check_adb():
                    print(f"  {ANSI.GREEN}✓ ADB installed successfully{ANSI.RESET}")
                else:
                    print(f"  {ANSI.RED}✗ ADB installation failed or not detected after install.{ANSI.RESET}")
                    print(f"  {ANSI.YELLOW}  Please install manually and re-run this installer or continue without ADB.{ANSI.RESET}")
            else:
                print(f"  {ANSI.RED}✗ ADB installation failed. You can continue without it.{ANSI.RESET}")
        else:
            print(f"  {ANSI.YELLOW}  Skipping ADB installation.{ANSI.RESET}")

    # Offer to launch AndroHack
    print_separator()
    print()
    if prompt_yes_no("Do you want to launch AndroHack now?"):
        run_androhack()
    else:
        print(f"{ANSI.CYAN}{ANSI.BOLD}  Setup complete. You can run AndroHack anytime with:{ANSI.RESET}")
        print(f"  {ANSI.WHITE}python3 {ANDROHACK_SCRIPT}{ANSI.RESET}")
        print()

    print(f"{ANSI.GREEN}{ANSI.BOLD}  Thank you for using AndroHack!{ANSI.RESET}")
    print(f"{ANSI.DIM}  Author: Mr.X | @whomrx{ANSI.RESET}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{ANSI.YELLOW}{ANSI.BOLD}  Interrupted. Setup cancelled.{ANSI.RESET}\n")
        sys.exit(0)
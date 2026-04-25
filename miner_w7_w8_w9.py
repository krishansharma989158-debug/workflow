#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miner Automation - W7, W8, W9 (Terminals 181-270 Only)
"""

import os
import sys
import subprocess
import time
import argparse
import psutil
from datetime import datetime
from typing import Optional

def auto_install_dependencies():
    required = ['requests', 'psutil', 'pillow']
    for package in required:
        try:
            if package == 'pillow':
                __import__('PIL')
            else:
                __import__(package)
            print(f"[OK] {package} already installed")
        except ImportError:
            print(f"[*] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"[OK] {package} installed")

auto_install_dependencies()

import requests
from PIL import ImageGrab

# ==================== TELEGRAM ====================
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8670890083:AAFdQaEiC67jmk6l8jxxdG01NTEN4JxvPUc")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6955911349")

class TelegramLogger:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    def send_message(self, message: str):
        try:
            requests.post(f"{self.base_url}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        except:
            pass
    def send_photo(self, image_path: str, caption: str):
        try:
            with open(image_path, 'rb') as f:
                requests.post(f"{self.base_url}/sendPhoto", files={'photo': f}, data={'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'parse_mode': 'HTML'}, timeout=30)
            os.remove(image_path)
        except:
            pass

telegram = TelegramLogger()

# ==================== CONFIG ====================
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
API_BASE = "https://api.unmineable.com/v5"
WALLET_ADDRESS = "nano_1g97x3h6wxd4h577p6dricapigs78ccc7tcowjfm67hewsmg7qob4xwc8jak"
COIN = "NANO"
BATCH_SIZE = 3
GAP_BETWEEN_BATCHES = 60
CHECK_INTERVAL = 360

# ==================== TERMINALS 181-270 ONLY ====================
W7_TERMINALS = [
    [181, "Terminal 181", "nhc5cz5e6oopoerdauuy6y", "https://ais-pre-nhc5cz5e6oopoerdauuy6y-176013927578.asia-east1.run.app"],
    [182, "Terminal 182", "ikrxidnxd6khp6qdmm6jgp", "https://ais-pre-ikrxidnxd6khp6qdmm6jgp-176013927578.asia-east1.run.app"],
    [183, "Terminal 183", "stqjfovfjtpvn6kc7dkzhj", "https://ais-pre-stqjfovfjtpvn6kc7dkzhj-176013927578.asia-east1.run.app"],
    [184, "Terminal 184", "vdl5mj3gjtvpkzx4lqjbid", "https://ais-pre-vdl5mj3gjtvpkzx4lqjbid-176013927578.asia-east1.run.app"],
    [185, "Terminal 185", "7kw6tkmgbagtn6wce25tuj", "https://ais-pre-7kw6tkmgbagtn6wce25tuj-176013927578.asia-east1.run.app"],
    [186, "Terminal 186", "ftcynwlv7uxsxk7csfjinc", "https://ais-pre-ftcynwlv7uxsxk7csfjinc-176013927578.asia-east1.run.app"],
    [187, "Terminal 187", "kdeka33uxwymolgj3dj4rq", "https://ais-pre-kdeka33uxwymolgj3dj4rq-176013927578.asia-east1.run.app"],
    [188, "Terminal 188", "p3adwbhulq3utk7cyiswcr", "https://ais-pre-p3adwbhulq3utk7cyiswcr-176013927578.asia-east1.run.app"],
    [189, "Terminal 189", "p2bzftlaes3mjeeipztv6y", "https://ais-pre-p2bzftlaes3mjeeipztv6y-176013927578.asia-east1.run.app"],
    [190, "Terminal 190", "wtgljxjas5lbys4t4eieny", "https://ais-pre-wtgljxjas5lbys4t4eieny-176013927578.asia-east1.run.app"],
    [191, "Terminal 191", "mkqjmpnsd6slzdktchipvh", "https://ais-pre-mkqjmpnsd6slzdktchipvh-176013927578.asia-east1.run.app"],
    [192, "Terminal 192", "liuiygrbr24ir6ubfbingq", "https://ais-pre-liuiygrbr24ir6ubfbingq-176013927578.asia-east1.run.app"],
    [193, "Terminal 193", "rpb6hiqsyhwwzrong54zfn", "https://ais-pre-rpb6hiqsyhwwzrong54zfn-176013927578.asia-east1.run.app"],
    [194, "Terminal 194", "cvij5vovanr4jsypfvcz3w", "https://ais-pre-cvij5vovanr4jsypfvcz3w-176013927578.asia-east1.run.app"],
    [195, "Terminal 195", "ryzxst2pj4ght47fbhdsbu", "https://ais-pre-ryzxst2pj4ght47fbhdsbu-176013927578.asia-east1.run.app"],
    [196, "Terminal 196", "dknhwrmcmhleboddxzh4um", "https://ais-pre-dknhwrmcmhleboddxzh4um-176013927578.asia-east1.run.app"],
    [197, "Terminal 197", "vwpsl3mearhyogc426yrcl", "https://ais-pre-vwpsl3mearhyogc426yrcl-176013927578.asia-east1.run.app"],
    [198, "Terminal 198", "qe5jppc4c72viy4swwjn2q", "https://ais-pre-qe5jppc4c72viy4swwjn2q-176013927578.asia-east1.run.app"],
    [199, "Terminal 199", "z6j5f3v7sqduinmzho67pg", "https://ais-pre-z6j5f3v7sqduinmzho67pg-176013927578.asia-east1.run.app"],
    [200, "Terminal 200", "msbe6zaj7xnavdo43am4fx", "https://ais-pre-msbe6zaj7xnavdo43am4fx-176013927578.asia-east1.run.app"],
    [201, "Terminal 201", "6tmcfbwge5u4p44xnh7opp", "https://ais-pre-6tmcfbwge5u4p44xnh7opp-176013927578.asia-east1.run.app"],
    [202, "Terminal 202", "jeq5aucreb43u7et5cpmr7", "https://ais-pre-jeq5aucreb43u7et5cpmr7-176013927578.asia-east1.run.app"],
    [203, "Terminal 203", "omvwie3qjvgmkcwgmn47fl", "https://ais-pre-omvwie3qjvgmkcwgmn47fl-176013927578.asia-east1.run.app"],
    [204, "Terminal 204", "b7kmc72w65kmhc43ul6pxo", "https://ais-pre-b7kmc72w65kmhc43ul6pxo-176013927578.asia-east1.run.app"],
    [205, "Terminal 205", "hv3ismifjyf2lmxwku3rgh", "https://ais-pre-hv3ismifjyf2lmxwku3rgh-176013927578.asia-east1.run.app"],
    [206, "Terminal 206", "t7z7zyrex5737yvgiom5mz", "https://ais-pre-t7z7zyrex5737yvgiom5mz-176013927578.asia-east1.run.app"],
    [207, "Terminal 207", "zbztoym765riuec262jyik", "https://ais-pre-zbztoym765riuec262jyik-176013927578.asia-east1.run.app"],
    [208, "Terminal 208", "lizxpn4fz7y4g5tsu3pc4g", "https://ais-pre-lizxpn4fz7y4g5tsu3pc4g-176013927578.asia-east1.run.app"],
    [209, "Terminal 209", "xar2klfffkfclp7nn2n5zd", "https://ais-pre-xar2klfffkfclp7nn2n5zd-176013927578.asia-east1.run.app"],
    [210, "Terminal 210", "6sf7ahgha2psbynf6klbcd", "https://ais-pre-6sf7ahgha2psbynf6klbcd-176013927578.asia-east1.run.app"],
]

W8_TERMINALS = [
    [211, "Terminal 211", "xtithrhgg6o7iwzpxk5ykp", "https://ais-pre-xtithrhgg6o7iwzpxk5ykp-757334599303.asia-east1.run.app"],
    [212, "Terminal 212", "dlfno4t3tvlfjjkl6uvkoy", "https://ais-pre-dlfno4t3tvlfjjkl6uvkoy-757334599303.asia-east1.run.app"],
    [213, "Terminal 213", "tcqynoonlyebrzenvogtfw", "https://ais-pre-tcqynoonlyebrzenvogtfw-757334599303.asia-east1.run.app"],
    [214, "Terminal 214", "eequrd7ajjdpwha26nkysu", "https://ais-pre-eequrd7ajjdpwha26nkysu-757334599303.asia-east1.run.app"],
    [215, "Terminal 215", "f4kroyc77qsdcqufjubhzb", "https://ais-pre-f4kroyc77qsdcqufjubhzb-757334599303.asia-east1.run.app"],
    [216, "Terminal 216", "3hb4gyosydfx5nmhzuzy3n", "https://ais-pre-3hb4gyosydfx5nmhzuzy3n-757334599303.asia-east1.run.app"],
    [217, "Terminal 217", "254eguacchqwdatyqbkddd", "https://ais-pre-254eguacchqwdatyqbkddd-757334599303.asia-east1.run.app"],
    [218, "Terminal 218", "zh62qghc44bvzy3lrqsufz", "https://ais-pre-zh62qghc44bvzy3lrqsufz-757334599303.asia-east1.run.app"],
    [219, "Terminal 219", "sya77afr2c3n3frk7xw7hb", "https://ais-pre-sya77afr2c3n3frk7xw7hb-757334599303.asia-east1.run.app"],
    [220, "Terminal 220", "45b37vrf6m743bek55nket", "https://ais-pre-45b37vrf6m743bek55nket-757334599303.asia-east1.run.app"],
    [221, "Terminal 221", "ppw7ghwn5j2y5otqxp6blo", "https://ais-pre-ppw7ghwn5j2y5otqxp6blo-757334599303.asia-east1.run.app"],
    [222, "Terminal 222", "c2jvv26ejpqyks57nioccd", "https://ais-pre-c2jvv26ejpqyks57nioccd-757334599303.asia-east1.run.app"],
    [223, "Terminal 223", "fjw5y53icoh7n2i6zdgwe5", "https://ais-pre-fjw5y53icoh7n2i6zdgwe5-757334599303.asia-east1.run.app"],
    [224, "Terminal 224", "nplzuhqdkwagsfoy3zn5hi", "https://ais-pre-nplzuhqdkwagsfoy3zn5hi-757334599303.asia-east1.run.app"],
    [225, "Terminal 225", "vk52lvnam5emgvebfnk6lt", "https://ais-pre-vk52lvnam5emgvebfnk6lt-757334599303.asia-east1.run.app"],
    [226, "Terminal 226", "5gxht2jklvag5nyahmj5oj", "https://ais-pre-5gxht2jklvag5nyahmj5oj-757334599303.asia-east1.run.app"],
    [227, "Terminal 227", "qmyvqfsqdzr7svei7m2ore", "https://ais-pre-qmyvqfsqdzr7svei7m2ore-757334599303.asia-east1.run.app"],
    [228, "Terminal 228", "e3fjyphkslazsehqgyu7yj", "https://ais-pre-e3fjyphkslazsehqgyu7yj-757334599303.asia-east1.run.app"],
    [229, "Terminal 229", "wsgilhodroohjgzhknlvcv", "https://ais-pre-wsgilhodroohjgzhknlvcv-757334599303.asia-east1.run.app"],
    [230, "Terminal 230", "7iaqplvfjb2ghbvlioxikd", "https://ais-pre-7iaqplvfjb2ghbvlioxikd-757334599303.asia-east1.run.app"],
    [231, "Terminal 231", "a3yuyq3afgphwn2zjtwaok", "https://ais-pre-a3yuyq3afgphwn2zjtwaok-757334599303.asia-east1.run.app"],
    [232, "Terminal 232", "ljpunoxs2yhswkvvjmn4v7", "https://ais-pre-ljpunoxs2yhswkvvjmn4v7-757334599303.asia-east1.run.app"],
    [233, "Terminal 233", "6vlr2d2x2swyhycoshnoaw", "https://ais-pre-6vlr2d2x2swyhycoshnoaw-757334599303.asia-east1.run.app"],
    [234, "Terminal 234", "faj3a7lxhn6odbwxgbzvbl", "https://ais-pre-faj3a7lxhn6odbwxgbzvbl-757334599303.asia-east1.run.app"],
    [235, "Terminal 235", "2qehn4nhqjp7msfmbkevz4", "https://ais-pre-2qehn4nhqjp7msfmbkevz4-757334599303.asia-east1.run.app"],
    [236, "Terminal 236", "k3qj4ukukyujwsnlb63s7y", "https://ais-pre-k3qj4ukukyujwsnlb63s7y-757334599303.asia-east1.run.app"],
    [237, "Terminal 237", "p3yvih5ydmapfudtghsspy", "https://ais-pre-p3yvih5ydmapfudtghsspy-757334599303.asia-east1.run.app"],
    [238, "Terminal 238", "jxuspfqtngvyz24h6erkep", "https://ais-pre-jxuspfqtngvyz24h6erkep-757334599303.asia-east1.run.app"],
    [239, "Terminal 239", "ocq4ocs5wcqtkwkvrq5y2r", "https://ais-pre-ocq4ocs5wcqtkwkvrq5y2r-757334599303.asia-east1.run.app"],
    [240, "Terminal 240", "o2j7b47inlfmaoix2gnrei", "https://ais-pre-o2j7b47inlfmaoix2gnrei-757334599303.asia-east1.run.app"],
]

W9_TERMINALS = [
    [241, "Terminal 241", "q26vi43f2z7jhqgl5rjgh6", "https://ais-pre-q26vi43f2z7jhqgl5rjgh6-585247436141.asia-east1.run.app"],
    [242, "Terminal 242", "vjbavzwmfhs2l4x53q7fvz", "https://ais-pre-vjbavzwmfhs2l4x53q7fvz-585247436141.asia-east1.run.app"],
    [243, "Terminal 243", "nebj4jva62oggzvcc6k3ez", "https://ais-pre-nebj4jva62oggzvcc6k3ez-585247436141.asia-east1.run.app"],
    [244, "Terminal 244", "q3n2ukroz42fwc7262cokq", "https://ais-pre-q3n2ukroz42fwc7262cokq-585247436141.asia-east1.run.app"],
    [245, "Terminal 245", "z6cfsjiwbud3xpoo3fyyyh", "https://ais-pre-z6cfsjiwbud3xpoo3fyyyh-585247436141.asia-east1.run.app"],
    [246, "Terminal 246", "xvyks3jext7lciduubce3e", "https://ais-pre-xvyks3jext7lciduubce3e-585247436141.asia-east1.run.app"],
    [247, "Terminal 247", "sguor6rumokv6gxr36cnrz", "https://ais-pre-sguor6rumokv6gxr36cnrz-585247436141.asia-east1.run.app"],
    [248, "Terminal 248", "wfhc22ifeoauwh3ojqargi", "https://ais-pre-wfhc22ifeoauwh3ojqargi-585247436141.asia-east1.run.app"],
    [249, "Terminal 249", "62soi5d2uvsrkzzxdrtfyf", "https://ais-pre-62soi5d2uvsrkzzxdrtfyf-585247436141.asia-east1.run.app"],
    [250, "Terminal 250", "z2rjgkmj5xeai7z6ijwiio", "https://ais-pre-z2rjgkmj5xeai7z6ijwiio-585247436141.asia-east1.run.app"],
    [251, "Terminal 251", "ybkeug3d4xrrvzgmsns5g4", "https://ais-pre-ybkeug3d4xrrvzgmsns5g4-585247436141.asia-east1.run.app"],
    [252, "Terminal 252", "st7ew76zb6qvyibubgekup", "https://ais-pre-st7ew76zb6qvyibubgekup-585247436141.asia-east1.run.app"],
    [253, "Terminal 253", "jjfueesiquoplv5wfih3gz", "https://ais-pre-jjfueesiquoplv5wfih3gz-585247436141.asia-east1.run.app"],
    [254, "Terminal 254", "42albendmqmsea6xdhmquv", "https://ais-pre-42albendmqmsea6xdhmquv-585247436141.asia-east1.run.app"],
    [255, "Terminal 255", "2o7zkdnsxas33mhyo3jpvv", "https://ais-pre-2o7zkdnsxas33mhyo3jpvv-585247436141.asia-east1.run.app"],
    [256, "Terminal 256", "gljgdsuzqe3e7r7ep7p25e", "https://ais-pre-gljgdsuzqe3e7r7ep7p25e-585247436141.asia-east1.run.app"],
    [257, "Terminal 257", "wkso7wohw3oxv4xseftktp", "https://ais-pre-wkso7wohw3oxv4xseftktp-585247436141.asia-east1.run.app"],
    [258, "Terminal 258", "nrfwjjjd7znxp5huzadccm", "https://ais-pre-nrfwjjjd7znxp5huzadccm-585247436141.asia-east1.run.app"],
    [259, "Terminal 259", "hatfhw2zxph63oz3jb4rjg", "https://ais-pre-hatfhw2zxph63oz3jb4rjg-585247436141.asia-east1.run.app"],
    [260, "Terminal 260", "tl6kqtdcrhyiirxiwfbc6z", "https://ais-pre-tl6kqtdcrhyiirxiwfbc6z-585247436141.asia-east1.run.app"],
    [261, "Terminal 261", "swmza44rxmo3j3d5zfrvy6", "https://ais-pre-swmza44rxmo3j3d5zfrvy6-585247436141.asia-east1.run.app"],
    [262, "Terminal 262", "27zabh6jsnwkwdyl6qnhkx", "https://ais-pre-27zabh6jsnwkwdyl6qnhkx-585247436141.asia-east1.run.app"],
    [263, "Terminal 263", "6pebfcv2xgcxmlwd6wkhxw", "https://ais-pre-6pebfcv2xgcxmlwd6wkhxw-585247436141.asia-east1.run.app"],
    [264, "Terminal 264", "4hqrzxgau757m6dxltq2jl", "https://ais-pre-4hqrzxgau757m6dxltq2jl-585247436141.asia-east1.run.app"],
    [265, "Terminal 265", "ksgux7ldqya5dvm2ifmb5r", "https://ais-pre-ksgux7ldqya5dvm2ifmb5r-585247436141.asia-east1.run.app"],
    [266, "Terminal 266", "zng7ykjiutnwa6yuxm7xlm", "https://ais-pre-zng7ykjiutnwa6yuxm7xlm-585247436141.asia-east1.run.app"],
    [267, "Terminal 267", "thvksqnqx7aoakgwztk2ai", "https://ais-pre-thvksqnqx7aoakgwztk2ai-585247436141.asia-east1.run.app"],
    [268, "Terminal 268", "wse2qobkltchpqba4ydcxw", "https://ais-pre-wse2qobkltchpqba4ydcxw-585247436141.asia-east1.run.app"],
    [269, "Terminal 269", "p3on5x4z65dnicgkbkskm7", "https://ais-pre-p3on5x4z65dnicgkbkskm7-585247436141.asia-east1.run.app"],
    [270, "Terminal 270", "bqe6pzbekrjboakxthsx3q", "https://ais-pre-bqe6pzbekrjboakxthsx3q-585247436141.asia-east1.run.app"],
]

# ==================== FUNCTIONS (SAME AS ABOVE) ====================
def log(msg): print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
def send_tg(title, msg, emoji="📘"): telegram.send_message(f"{emoji} <b>{title}</b>\n{msg}")
def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        return f"CPU: {cpu}% | RAM: {ram.used/(1024**3):.1f}/{ram.total/(1024**3):.1f}GB ({ram.percent}%)"
    except:
        return "N/A"

def take_screenshot(filename="screenshot.png"):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        return filename
    except:
        return None

def get_uuid():
    try:
        r = requests.get(f"{API_BASE}/address/{WALLET_ADDRESS}?coin={COIN}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        return r.json().get('data', {}).get('uuid')
    except:
        return None

def check_status(miner_name, uuid):
    try:
        r = requests.get(f"{API_BASE}/account/{uuid}/workers", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        workers = r.json().get('data', {}).get('randomx', {}).get('workers', [])
        for w in workers:
            if w.get('name') == miner_name:
                return w.get('online', False)
        return False
    except:
        return False

def open_window(url, name):
    try:
        subprocess.Popen([FIREFOX_PATH, "-new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def close_window(miner_name):
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] == 'firefox.exe' and miner_name in str(proc.info['cmdline']):
                proc.terminate()
                return True
    except:
        pass
    return False

def run_workflow(terminals, workflow_name):
    if not os.path.exists(FIREFOX_PATH):
        send_tg("ERROR", "Firefox not found!", "❌")
        return
    
    total = len(terminals)
    batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    
    log(f"{workflow_name} Started | Total: {total}")
    send_tg("WORKFLOW STARTED", f"{workflow_name}\nTotal: {total}\n{get_system_info()}", "🚀")
    
    uuid = get_uuid()
    if not uuid:
        send_tg("ERROR", "Failed to get UUID!", "❌")
        return
    
    # Open first batch (for screenshot)
    log("Opening BATCH 1...")
    first_batch = terminals[0:BATCH_SIZE]
    for m in first_batch:
        open_window(m[3], m[1])
        time.sleep(2)
    
    time.sleep(30)
    ss = take_screenshot(f"screenshot_{workflow_name.replace(' ', '_')}.png")
    if ss:
        caption = f"📸 BATCH 1 SCREENSHOT\n{workflow_name}\n{get_system_info()}"
        telegram.send_photo(ss, caption)
    
    time.sleep(GAP_BETWEEN_BATCHES)
    
    # Open remaining batches
    for b in range(1, batches):
        start = b * BATCH_SIZE
        end = min(start + BATCH_SIZE, total)
        for m in terminals[start:end]:
            open_window(m[3], m[1])
            time.sleep(2)
        if end < total:
            time.sleep(GAP_BETWEEN_BATCHES)
    
    log("All terminals opened!")
    send_tg("ALL OPENED", f"All {total} terminals opened!\n{get_system_info()}", "✅")
    
    # Monitoring loop
    while True:
        time.sleep(CHECK_INTERVAL)
        offline, online = [], 0
        for m in terminals:
            if check_status(m[2], uuid):
                online += 1
            else:
                offline.append(m)
        
        if offline:
            send_tg(f"STATUS - {len(offline)} OFFLINE", f"{workflow_name}: {online}/{total} ONLINE\n{get_system_info()}", "⚠️")
            for m in offline:
                close_window(m[2])
                time.sleep(2)
                open_window(m[3], m[1])
                time.sleep(3)
            send_tg("RESTART COMPLETE", f"Restarted {len(offline)} miners", "✅")
        else:
            send_tg("STATUS - ALL ONLINE", f"{workflow_name}: {online}/{total} ONLINE (100%)\n{get_system_info()}", "✅")

# ==================== MAIN ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--workflow', type=str, default='W7')
    args = parser.parse_args()
    
    if args.workflow == 'W7':
        run_workflow(W7_TERMINALS, "W7 (181-210)")
    elif args.workflow == 'W8':
        run_workflow(W8_TERMINALS, "W8 (211-240)")
    elif args.workflow == 'W9':
        run_workflow(W9_TERMINALS, "W9 (241-270)")
    else:
        print("Use --workflow W7, W8, or W9")

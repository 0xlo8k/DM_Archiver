import requests
import time
import os

API_BASE   = "https://discord.com/api/v10"
USER_TOKEN = "" # Use your session token here. You can find it in your browser's developer tools while logged into Discord. Be careful with this token, as it grants access to your account.        
OUTPUT_DIR = "dm_exports"            
PAGE_SIZE  = 100
RATE_LIMIT_S = 0.6                   
MAX_DMS    = 200                    

HEADERS = {
    "Authorization": USER_TOKEN,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DMExporter/1.0",
}
def banner():
    print(r"""
░██     ░██            ░██                 ░██████     ░██████  ░█████████     ░███    ░█████████  ░██████████ ░█████████  
░██     ░██            ░██                ░██   ░██   ░██   ░██ ░██     ░██   ░██░██   ░██     ░██ ░██         ░██     ░██ 
░██     ░██  ░███████  ░██ ░██    ░██    ░██         ░██        ░██     ░██  ░██  ░██  ░██     ░██ ░██         ░██     ░██ 
░██████████ ░██    ░██ ░██ ░██    ░██     ░████████  ░██        ░█████████  ░█████████ ░█████████  ░█████████  ░█████████  
░██     ░██ ░██    ░██ ░██ ░██    ░██            ░██ ░██        ░██   ░██   ░██    ░██ ░██         ░██         ░██   ░██   
░██     ░██ ░██    ░██ ░██ ░██   ░███     ░██   ░██   ░██   ░██ ░██    ░██  ░██    ░██ ░██         ░██         ░██    ░██  
░██     ░██  ░███████  ░██  ░█████░██      ░██████     ░██████  ░██     ░██ ░██    ░██ ░██         ░██████████ ░██     ░██ 
                                  ░██                                                                                      
                            ░███████                                                                                       
 
""")
banner()
def get_dm_channels():    
    r = requests.get(f"{API_BASE}/users/@me/channels", headers=HEADERS)
    r.raise_for_status()
    dms = []
    for ch in r.json():
        if ch.get("type") in (1, 3):          
            dms.append(ch)
    return dms

def fetch_all_messages(channel_id):
    messages, before = [], None
    while True:
        params = {"limit": PAGE_SIZE}
        if before:
            params["before"] = before
        r = requests.get(f"{API_BASE}/channels/{channel_id}/messages",
                         headers=HEADERS, params=params)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        messages.extend(batch)
        oldest = batch[-1]["id"]
        if oldest == before:
            break
        before = oldest
        time.sleep(RATE_LIMIT_S)
        if len(batch) < PAGE_SIZE:
            break
    return messages


def dm_label(ch):
    typ = ch.get("type")
    if typ == 1:
        user = (ch.get("recipients") or [{}])[0]
        return f"dm_{user.get('username', 'unknown')}_{ch['id']}"
    if typ == 3:
        name = ch.get("name") or "group"
        return f"group_{name}_{ch['id']}"
    return f"dm_{ch['id']}"


def format_message(m):
    ts = m.get("timestamp", "?")
    auth = m.get("author", {}).get("username", "?")
    content = m.get("content") or ""
    for att in (m.get("attachments") or []):
        content += f"\n  [attachment: {att.get('url')}]"
    for emb in (m.get("embeds") or []):
        if emb.get("title") or emb.get("description"):
            content += f"\n  [embed: {emb.get('title','')} - {emb.get('description','')}]"
    return f"[{ts}] ({auth}): {content}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dms = get_dm_channels()[:MAX_DMS]
    print(f"Found {len(dms)} DM/group channels. Exporting...\n")

    for i, ch in enumerate(dms, 1):
        name = dm_label(ch)
        path = os.path.join(OUTPUT_DIR, f"{name}.txt")
        msgs = fetch_all_messages(ch["id"])
        lines = [format_message(m) for m in reversed(msgs)]
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {name} - {ch['id']} - {len(lines)} messages\n\n")
            f.write("\n".join(lines))
        print(f"[{i}/{len(dms)}] {name}: {len(lines)} msgs -> {path}")
        time.sleep(RATE_LIMIT_S)

    print(f"\nDone. Exports written to ./{OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
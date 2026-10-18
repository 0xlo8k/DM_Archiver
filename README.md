# DM_Archiver

<div align="center">

# ░ DM ARCHIVE

### `Your conversations. Your archive. Your control.`

A lightweight Python utility for exporting Discord DM and group chat history into readable, timestamped `.txt` files.

<br>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/Discord-API%20v10-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Format](https://img.shields.io/badge/Export-Plain%20Text-00C853?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A simple way to preserve your Discord conversations locally.**

</div>

---

## `01` — Overview

**DM Archive** is a Python-based conversation export utility that retrieves direct message and group DM history through the Discord API and saves it locally in an organized, human-readable format.

No database. No complicated setup. Just Python and your exported conversations.

### ✨ Features

- **DM & Group Export** — Retrieve one-to-one and group DM channel histories.
- **Full Message Pagination** — Fetch message history in batches of up to 100.
- **Chronological Output** — Save messages from oldest to newest.
- **Timestamped Messages** — Include message timestamps and author usernames.
- **Attachment References** — Preserve links to message attachments.
- **Embed References** — Include available embed titles and descriptions.
- **Rate-Limit Pacing** — Add delays between requests.
- **Export Limits** — Configure how many DM channels to process.
- **Plain-Text Archives** — Read your exports in any text editor.

---

## `02` — Preview

```text
dm_exports/
├── dm_username_123456789.txt
├── dm_another_user_234567890.txt
├── group_project_chat_345678901.txt
└── ...
```

### Inside an exported file

```text
# dm_username_123456789 - 123456789 - 3 messages

[2026-01-12T09:30:00.000Z] (username): Hey, what's up?
[2026-01-12T09:31:12.000Z] (you): All good!
[2026-01-12T09:32:45.000Z] (username): Check this out.
  [attachment: https://cdn.discordapp.com/...]
```

*Example output for illustration; actual content depends on the messages returned by the API.*

---

## `03` — Requirements

- Python 3.9 or newer
- `requests`
- A Discord account with access to the conversations being exported

---

## `04` — Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/dm-archive.git
cd dm-archive
```

**2. Install dependencies**

```bash
python -m pip install requests
```

**3. Configure the script**

Set your output preferences in the configuration section:

```python
OUTPUT_DIR = "dm_exports"
PAGE_SIZE = 100
RATE_LIMIT_S = 0.6
MAX_DMS = 200
```

| Setting | Description |
|---|---|
| `OUTPUT_DIR` | Directory where text exports are saved |
| `PAGE_SIZE` | Number of messages requested per API call |
| `RATE_LIMIT_S` | Delay between requests |
| `MAX_DMS` | Maximum number of DM channels processed |

---

## `05` — Usage

Run the script:

```bash
python dm_archive.py
```

The utility will:

1. Create the output directory if it doesn't exist.
2. Retrieve accessible DM and group DM channels.
3. Fetch message history in batches.
4. Format messages and attachment/embed references.
5. Write each conversation to its own `.txt` file.

When finished, your exports will be available in:

```text
./dm_exports/
```

---

## `06` — Security & Privacy

> [!CAUTION]
> **Never commit authentication tokens, private conversations, or personal exports to a public repository.**

This script interacts with your Discord account, so handle authentication and exported data carefully.

- Never hardcode a personal authentication token into a publicly shared script.
- Never upload session tokens, cookies, `.env` files containing secrets, or exported DM archives.
- Do not use another person's credentials or access conversations without authorization.
- Keep exported messages and attachment URLs private.
- Prefer Discord's official data package for personal archival whenever it meets your needs.

**Important:** User-account automation through private session tokens is not an officially supported Discord bot workflow and may violate Discord's Terms of Service. This repository is intended for authorized personal archiving, not surveillance, scraping other users' data, or bulk messaging.

For a public release, consider implementing supported authentication and a safer credential-handling workflow before distributing the executable script.

---

## `07` — Known Limitations

- Exports are plain text, not a complete Discord data replica.
- Message edits, deletions, reactions, and thread context are not fully preserved.
- Attachments are referenced by URL rather than downloaded.
- Embed output is limited to available titles and descriptions.
- Channel processing is capped by `MAX_DMS`.
- The configured request delay is not a guarantee against API rate limits.
- Export success depends on account access and API availability.

---

## `08` — Roadmap

Potential improvements for future releases:

- [ ] JSON export support
- [ ] CSV export support
- [ ] Optional attachment downloading
- [ ] Better filename sanitization
- [ ] Progress bars and export summaries
- [ ] Retry handling for HTTP 429 responses
- [ ] Duplicate-safe incremental backups
- [ ] Export filtering by date
- [ ] Officially supported authentication workflow

---

## `09` — Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes locally.
5. Open a pull request with a clear description.

Please never include private conversation data, credentials, or authentication tokens in issues or pull requests.

<div align="center">

### `ARCHIVE YOUR HISTORY. KEEP YOUR DATA YOURS.`

Made with Python 🐍

**If you find this project useful, consider giving it a ⭐**

</div>

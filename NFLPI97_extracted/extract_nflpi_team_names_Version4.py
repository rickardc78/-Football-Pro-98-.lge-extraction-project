import re

def decrypt_team_block(data):
    id = data[0]
    xor = 0x69 * id
    decrypted = bytearray()
    decrypted.append(id)
    for i, b in enumerate(data[1:], start=1):
        decrypted.append((b ^ (xor + i - 1) & 0xFF))
    return decrypted

def find_strings_in_block(block):
    pattern = rb'[\x20-\x7E]{3,}'  # any ASCII string of 3+ chars
    results = []
    for match in re.finditer(pattern, block):
        try:
            results.append(match.group().decode('ascii'))
        except:
            continue
    return results

def extract_all_team_names(lge_bytes, block_size=171):
    block_marker = b'T03:'
    team_names = []
    i = 0
    while True:
        idx = lge_bytes.find(block_marker, i)
        if idx == -1:
            break
        block_start = idx + len(block_marker)
        team_block = lge_bytes[block_start:block_start+block_size]
        if len(team_block) != block_size:
            i = block_start + 1
            continue
        decrypted = decrypt_team_block(team_block)
        readable_strings = find_strings_in_block(decrypted)
        for s in readable_strings:
            if 3 <= len(s) <= 20:
                team_names.append(s)
        i = block_start + block_size
    return team_names

with open("NFLPI97.lge", "rb") as f:
    lge_bytes = f.read()

team_names = extract_all_team_names(lge_bytes)

# NFL teams filter starts here
known_teams = [
    "Packers", "Cowboys", "Bears", "Giants", "Patriots", "49ers", "Eagles", "Dolphins",
    "Jets", "Raiders", "Steelers", "Saints", "Broncos", "Rams", "Chiefs", "Vikings",
    "Seahawks", "Bills", "Buccaneers", "Falcons", "Panthers", "Ravens", "Bengals",
    "Colts", "Jaguars", "Texans", "Titans", "Cardinals", "Commanders", "Lions", "Browns",
    "Chargers"
]

print("NFL teams found in extracted strings:")
for s in team_names:
    for team in known_teams:
        if team.lower() in s.lower():
            print(f"Found NFL team: {s}")
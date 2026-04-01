#!/usr/bin/env python3
"""
download_images.py — Downloads all photos for warren_library.html.

Run ONCE from the same folder as this file:
    python3 download_images.py

Creates an ./images/ folder. Then open the HTML via:
    python3 serve.py   →   http://localhost:8765

Why this script? Chrome blocks loading local images when opening HTML files
directly (file:// protocol security restriction). Running via a local server
(serve.py) fixes this — but images must be downloaded first.
"""
import urllib.request, os, time, sys

os.makedirs("images", exist_ok=True)

IMAGES = [
    # Town Hall / Library
    ("warren_town_hall_2008.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/2008_library_Warren_Vermont_2611591841.jpg/800px-2008_library_Warren_Vermont_2611591841.jpg",
     "Warren Town Hall exterior, 2008 (year before library moved in)"),
    # Library interior
    ("warren_library_interior_2018.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Second_floor_of_Warren_Public_Library%2C_August_2018.JPG/800px-Second_floor_of_Warren_Public_Library%2C_August_2018.JPG",
     "Warren Public Library interior, second floor, 2018"),
    # Main Street
    ("warren_main_street_north.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Main_Street%2C_Looking_North%2C_Warren%2C_VT.jpg/800px-Main_Street%2C_Looking_North%2C_Warren%2C_VT.jpg",
     "Main Street Warren VT, looking north"),
    # Church / Meetinghouse
    ("warren_church.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Warren_Church%2C_Warren%2C_Vermont.jpg/800px-Warren_Church%2C_Warren%2C_Vermont.jpg",
     "Warren Church (1838-39 meetinghouse)"),
    # Covered Bridge (two angles)
    ("warren_covered_bridge.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/WARREN_VILLAGE_COVERED_BRIDGE.jpg/800px-WARREN_VILLAGE_COVERED_BRIDGE.jpg",
     "Warren Village Covered Bridge"),
    ("warren_bridge_2.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/WarrenBridge.JPG/800px-WarrenBridge.JPG",
     "Warren Covered Bridge, alternate view"),
    # East Warren farmstead (illustrates Red School House era)
    ("warren_sibley_house_1967.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Sibley_House_1967.jpg/600px-Sibley_House_1967.jpg",
     "Sibley House, East Warren, 1967 — typical East Warren farmstead"),
    # Historic District home
    ("warren_hickox_house.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Warren_Hickox_House.JPG/800px-Warren_Hickox_House.JPG",
     "Warren Hickox House, Warren Village Historic District"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "https://commons.wikimedia.org/",
}

print(f"Downloading {len(IMAGES)} images to ./images/ ...\n")
ok = 0
for fname, url, desc in IMAGES:
    out = os.path.join("images", fname)
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        print(f"  ✓ Already have: {fname}")
        ok += 1
        continue
    print(f"  ↓ {desc[:55]:<55}", end=" ", flush=True)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(out, "wb") as f:
            f.write(data)
        print(f"  {len(data)//1024}KB ✓")
        ok += 1
        time.sleep(0.5)
    except Exception as e:
        print(f"  FAILED: {e}")

print(f"\n{'='*50}")
print(f"{ok}/{len(IMAGES)} images downloaded to ./images/")
if ok == len(IMAGES):
    print("\nAll done! Now run:  python3 serve.py")
    print("Then open:         http://localhost:8765")
else:
    print(f"\n{len(IMAGES)-ok} failed. Try running again (Wikimedia rate-limits occasionally).")
    print("Or open warren_library.html via serve.py anyway — missing images show placeholders.")

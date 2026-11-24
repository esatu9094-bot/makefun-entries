import os
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Your context window is full, yet you keep going. Fortune favors the compact prompt.")
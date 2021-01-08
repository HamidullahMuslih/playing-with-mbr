from pathlib import Path


beforeenc = Path('mbr-before-enc.bin').read_bytes()
afterenc = Path('mbr-after-enc.bin').read_bytes()

if beforeenc == afterenc:
    print("MBR code integrity check has been succesfull")

else:
    print("MBR code has been modified")

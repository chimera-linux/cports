import sys
import subprocess

# the struct consists of 16 zero bytes followed by the kind byte (values 1-3)
# followed by 23 more zero bytes (a total size of 40 on a 64-bit system)

pfx_bytes = 16
total_bytes = 40

pfx = b"\x00" * pfx_bytes
sfx = b"\x00" * (total_bytes - len(pfx) - 1)

# first check if we're referencing the symbols at all
syms = subprocess.run(
    ["nm", "-D", "--format=just-symbols", "--undefined-only", sys.argv[1]],
    capture_output=True,
    check=False,
)
if syms.returncode != 0:
    sys.exit(1)

symset = set(map(lambda s: s.split(b"@")[0], syms.stdout.strip().split()))
needsyms = [
    b"pthread_mutex_lock",
    b"pthread_mutex_timedlock",
    b"pthread_mutex_trylock",
]
for sym in needsyms:
    if sym in symset:
        break
else:
    sys.exit(1)

sp = subprocess.run(
    ["objcopy", "-Obinary", "--only-section=.data", sys.argv[1], "-"],
    capture_output=True,
    check=False,
)
if sp.returncode != 0:
    sys.exit(1)

data = sp.stdout
start = 0

while True:
    pat = data.find(pfx, start)
    if pat < 0:
        break
    if pat % 8 != 0:
        # round up to alignment
        pat += 8 - (pat % 8)
    # get the piece
    chunk = data[pat : pat + total_bytes]
    if len(chunk) != total_bytes:
        break
    # check if pfx and sfx is okay
    if chunk[0:pfx_bytes] != pfx or chunk[pfx_bytes + 1 :] != sfx:
        start = pat + 8
        continue
    # see if the inbetween byte matches anything...
    match chunk[pfx_bytes]:
        case 1 | 2 | 3:
            print(
                f"Found potential non-portable mutex initializer in {sys.argv[1]}..."
            )
            sys.exit(0)
    # try from next aligned piece
    start = pat + 8

sys.exit(1)

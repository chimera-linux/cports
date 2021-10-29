import struct
import mmap
import stat
import pathlib

_tsizes = "_BH_I___Q"

def _make_struct(l):
    v32 = "".join(map(lambda x: _tsizes[x[1]], l))
    v64 = "".join(map(lambda x: _tsizes[x[2]], l))
    return (v32, v64)

elf_types = [
    "ET_NONE", "ET_REL", "ET_EXEC", "ET_DYN", "ET_CORE"
]

hdrdef_elf = [
    ("magic",     4, 4),
    ("wordsize",  1, 1),
    ("endian",    1, 1),
    ("version",   1, 1),
    ("abi",       1, 1),
    ("abiver",    1, 1),
    ("pad1",      4, 4),
    ("pad2",      2, 2),
    ("pad3",      1, 1),
    ("type",      2, 2),
    ("machine",   2, 2),
    ("oversion",  4, 4),
    ("entry",     4, 8),
    ("phoff",     4, 8),
    ("shoff",     4, 8),
    ("flags",     4, 4),
    ("ehsize",    2, 2),
    ("phentsize", 2, 2),
    ("phnum",     2, 2),
    ("shentsize", 2, 2),
    ("shnum",     2, 2),
    ("shstrndx",  2, 2)
]

hdr_elf = _make_struct(hdrdef_elf)

hdrdef_sect = [
    ("name",      4, 4),
    ("type",      4, 4),
    ("flags",     4, 8),
    ("addr",      4, 8),
    ("offset",    4, 8),
    ("size",      4, 8),
    ("link",      4, 4),
    ("info",      4, 4),
    ("addralign", 4, 8),
    ("entsize",   4, 8)
]

hdr_sect = _make_struct(hdrdef_sect)

# we only scan program headers for presence of PT_INTERP, that means we can
# skip scanning all the other fields, as that would be a pain (the field
# order differs between 32-bit and 64-bit ELF files)
hdrdef_prog = [
    ("type", 4, 4),
]

hdr_prog = _make_struct(hdrdef_prog)

dyndef = [
    ("tag", 4, 8),
    ("val", 4, 8)
]

dyn_entry = _make_struct(dyndef)

def _unpack(sdef, sstr, offset, endian, mm):
    endian = ("<>")[endian]
    sstr = endian + sstr
    bytes = mm[offset:offset + struct.calcsize(sstr)]
    return {sdef[i][0]:v for i, v in enumerate(struct.unpack(sstr, bytes))}

def _get_nullstr(offset, strtab, mm):
    sbeg = strtab + offset
    send = mm.find(b"\0", sbeg)
    if send < 0:
        return mm[sbeg:]
    else:
        return mm[sbeg:send]

def _scan_one(fpath):
    inf = open(fpath, "rb")
    mm = mmap.mmap(inf.fileno(), 0, prot = mmap.PROT_READ)

    if mm[0:4] != b"\x7FELF":
        mm.close()
        inf.close()
        return None

    wsi = mm[4:5]
    if len(wsi) == 0 or wsi[0] > 2:
        mm.close()
        inf.close()
        return None
    wsi = wsi[0] - 1

    endian = mm[5:6]
    if len(endian) == 0 or endian[0] > 2:
        mm.close()
        inf.close()
        return None
    endian = endian[0] - 1

    ehdr = _unpack(hdrdef_elf, hdr_elf[wsi], 0, endian, mm)

    etype = ehdr["type"]
    if etype >= len(elf_types):
        mm.close()
        inf.close()
        return None

    shoff = ehdr["shoff"]
    shents = ehdr["shentsize"]
    phoff = ehdr["phoff"]
    phents = ehdr["phentsize"]

    interp = False
    for i in range(ehdr["phnum"]):
        phdr = _unpack(hdrdef_prog, hdr_prog[wsi], phoff, endian, mm)
        if phdr["type"] == 0x3:
            # PT_INTERP
            interp = True
            break
        phoff += phents

    dynsect = None
    for i in range(ehdr["shnum"]):
        shdr = _unpack(hdrdef_sect, hdr_sect[wsi], shoff, endian, mm)
        # SHT_DYNAMIC
        if shdr["type"] == 0x6:
            dynsect = shdr
            break
        # march on
        shoff += shents

    needed = []
    soname = None
    textrel = False

    if dynsect:
        dynoff = dynsect["offset"]
        dynsz = struct.calcsize("=" + dyn_entry[wsi])
        strtab = None

        while True:
            dynent = _unpack(dyndef, dyn_entry[wsi], dynoff, endian, mm)
            dyntag = dynent["tag"]
            # sentinel
            if dyntag == 0:
                break
            # read tags relevant to us
            if dyntag == 1:
                # DT_NEEDED
                needed.append(dynent["val"])
            elif dyntag == 14:
                # DT_SONAME
                soname = dynent["val"]
            elif dyntag == 5:
                # DT_STRTAB
                strtab = dynent["val"]
            elif dyntag == 22:
                # DT_TEXTREL
                textrel = True
            elif dyntag == 30:
                # DT_FLAGS
                if not textrel:
                    textrel = (dynent["val"] & 0x4) != 0

            dynoff += dynsz

        if not strtab and (len(needed) > 0 or soname):
            mm.close()
            inf.close()
            return None

        for i in range(len(needed)):
            needed[i] = _get_nullstr(needed[i], strtab, mm).decode()

        if soname:
            soname = _get_nullstr(soname, strtab, mm).decode()

    mm.close()
    inf.close()

    # sanitize
    if soname and len(soname) == 0:
        soname = None

    return (
        ehdr["machine"], elf_types[etype],
        not dynsect, interp, textrel, needed, soname
    )

def scan(pkg, somap):
    scandir = pkg.destdir
    elf_usrshare = []
    elf_textrels = []
    elf_foreign  = []

    # only test machine type against libc when not bootstrapping
    # as otherise we cannot provide guarantees about the host system
    if pkg.stage > 0:
        libc = _scan_one(pkg.rparent.profile().sysroot / "usr/lib/libc.so")

    for fpath in scandir.rglob("*"):
        st = fpath.lstat()
        # skip empty files, non-regular files
        if st.st_size == 0 or not stat.S_ISREG(st.st_mode):
            continue
        # try scan
        scanned = _scan_one(fpath)
        # not suitable
        if not scanned:
            continue
        # object file?
        if scanned[1] == "ET_REL":
            continue
        # relativize path
        fpath = fpath.relative_to(scandir)
        # probably a container file
        if scanned[0] == 0:
            pkg.log_warn(f"ELF file with no machine type (container?): {fpath}")
            continue
        # foreign file
        if pkg.stage > 0:
            if scanned[0] != libc[0] and not pkg.rparent.options["foreignelf"]:
                elf_foreign.append(fpath)
        # deny /usr/share files
        if fpath.is_relative_to("usr/share"):
            elf_usrshare.append(fpath)
        # expand
        mtype, etype, is_static, interp, textrel, needed, soname = scanned
        # has textrels
        if textrel and not pkg.rparent.options["textrels"]:
            elf_textrels.append(fpath)
        # store
        somap[str(fpath)] = (
            soname, needed, pkg.pkgname, is_static, etype, interp
        )

    # some linting

    if len(elf_usrshare) > 0:
        try:
            pkg.error("ELF files in /usr/share:")
        except:
            for f in elf_usrshare:
                print(f"   {f}")
            raise

    if len(elf_textrels) > 0:
        try:
            pkg.error("found textrels:")
        except:
            for f in elf_textrels:
                print(f"   {f}")
            raise

    if len(elf_foreign) > 0:
        try:
            pkg.error("found foreign-machine ELF files:")
        except:
            for f in elf_foreign:
                print(f"   {f}")
            raise

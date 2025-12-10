import struct
import mmap
import stat

from cbuild.core import paths

_tsizes = "_BH_I___Q"


def _make_struct(lst):
    v32 = "".join(map(lambda x: _tsizes[x[1]], lst))
    v64 = "".join(map(lambda x: _tsizes[x[2]], lst))
    return (v32, v64)


def _make_sepstruct(l32, l64):
    v32 = "".join(map(lambda x: _tsizes[x[1]], l32))
    v64 = "".join(map(lambda x: _tsizes[x[1]], l64))
    return (v32, v64)


elf_types = ["ET_NONE", "ET_REL", "ET_EXEC", "ET_DYN", "ET_CORE"]

hdrdef_elf = [
    ("magic", 4, 4),
    ("wordsize", 1, 1),
    ("endian", 1, 1),
    ("version", 1, 1),
    ("abi", 1, 1),
    ("abiver", 1, 1),
    ("pad1", 4, 4),
    ("pad2", 2, 2),
    ("pad3", 1, 1),
    ("type", 2, 2),
    ("machine", 2, 2),
    ("oversion", 4, 4),
    ("entry", 4, 8),
    ("phoff", 4, 8),
    ("shoff", 4, 8),
    ("flags", 4, 4),
    ("ehsize", 2, 2),
    ("phentsize", 2, 2),
    ("phnum", 2, 2),
    ("shentsize", 2, 2),
    ("shnum", 2, 2),
    ("shstrndx", 2, 2),
]

hdr_elf = _make_struct(hdrdef_elf)

hdrdef_sect = [
    ("name", 4, 4),
    ("type", 4, 4),
    ("flags", 4, 8),
    ("addr", 4, 8),
    ("offset", 4, 8),
    ("size", 4, 8),
    ("link", 4, 4),
    ("info", 4, 4),
    ("addralign", 4, 8),
    ("entsize", 4, 8),
]

hdr_sect = _make_struct(hdrdef_sect)

# we make 32 and 64 separate here as the field order differs

hdr32def_prog = [
    ("type", 4),
    ("offset", 4),
    ("vaddr", 4),
    ("paddr", 4),
    ("filesz", 4),
    ("memsz", 4),
    ("flags", 4),
    ("align", 4),
]

hdr64def_prog = [
    ("type", 4),
    ("flags", 4),
    ("offset", 8),
    ("vaddr", 8),
    ("paddr", 8),
    ("filesz", 8),
    ("memsz", 8),
    ("align", 8),
]

hdrdef_prog = (hdr32def_prog, hdr64def_prog)
hdr_prog = _make_sepstruct(*hdrdef_prog)

dyndef = [("tag", 4, 8), ("val", 4, 8)]

dyn_entry = _make_struct(dyndef)


def _unpack(sdef, sstr, offset, endian, mm):
    endian = ("<>")[endian]
    sstr = endian + sstr
    bytes = mm[offset : offset + struct.calcsize(sstr)]
    return {sdef[i][0]: v for i, v in enumerate(struct.unpack(sstr, bytes))}


def _get_nullstr(offset, strtab, mm):
    sbeg = strtab + offset
    send = mm.find(b"\0", sbeg)
    if send < 0:
        return mm[sbeg:]
    else:
        return mm[sbeg:send]


def scan_one(fpath):
    inf = open(fpath, "rb")
    mm = mmap.mmap(inf.fileno(), 0, prot=mmap.PROT_READ)

    if mm[0:4] != b"\x7fELF":
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

    interp = None
    stack = False
    execstack = True
    for i in range(ehdr["phnum"]):
        phdr = _unpack(hdrdef_prog[wsi], hdr_prog[wsi], phoff, endian, mm)
        if phdr["type"] == 0x3:
            # PT_INTERP
            interp = True
            if stack:
                break
        elif phdr["type"] == 0x6474E551:
            # PT_GNU_STACK
            # checking flags against PF_X (1 << 0)
            execstack = (phdr["flags"] & 1) != 0
            stack = True
            if interp:
                break
        phoff += phents

    strtabs = []

    dynsect = None
    for i in range(ehdr["shnum"]):
        shdr = _unpack(hdrdef_sect, hdr_sect[wsi], shoff, endian, mm)
        # SHT_DYNAMIC
        if shdr["type"] == 0x6:
            dynsect = shdr
            break
        elif shdr["type"] == 0x3:
            strtabs.append(shdr)
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
            elif dyntag == 0x6FFFFFFB:
                # DT_FLAGS_1
                if (dynent["val"] & 0x8000000) != 0 and not interp:
                    # DF_1_PIE; guarantees that it's an executable
                    interp = False

            dynoff += dynsz

        if not strtab and (len(needed) > 0 or soname):
            mm.close()
            inf.close()
            return None

        for st in strtabs:
            if st["addr"] == strtab:
                strtab = st["offset"]
                break
        else:
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
    if soname is not None and len(soname) == 0:
        soname = None

    return (
        ehdr["machine"],
        elf_types[etype],
        not dynsect,
        interp,
        textrel,
        execstack,
        needed,
        soname,
    )


def is_static(path):
    einfo = scan_one(path)
    return einfo and einfo[2]


def scan(pkg, somap):
    scandir = pkg.destdir
    elf_usrshare = []
    elf_textrels = []
    elf_xstack = []
    elf_foreign = []

    # only test machine type against libc when not bootstrapping
    # as otherise we cannot provide guarantees about the host system
    if pkg.stage > 0:
        rsroot = pkg.rparent.profile().sysroot.relative_to("/")
        libcp = paths.bldroot() / rsroot / "usr/lib/libc.so"
        libc = scan_one(libcp)

    for fpath in scandir.rglob("*"):
        st = fpath.lstat()
        # skip empty files, non-regular files
        if st.st_size == 0 or not stat.S_ISREG(st.st_mode):
            continue
        # try scan
        scanned = scan_one(fpath)
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
        foreign = False
        if pkg.stage > 0:
            foreign = scanned[0] != libc[0]
            if foreign and not pkg.options["foreignelf"]:
                elf_foreign.append(fpath)
        # deny /usr/share files
        if fpath.is_relative_to("usr/share"):
            elf_usrshare.append(fpath)
        # expand
        mtype, etype, is_static, interp, textrel, xstk, needed, soname = scanned
        # has textrels
        if textrel and not pkg.options["textrels"]:
            elf_textrels.append(fpath)
        # has executable stack
        if xstk and not pkg.options["execstack"]:
            elf_xstack.append(fpath)
        # store
        somap[str(fpath)] = (
            soname,
            needed,
            pkg.pkgname,
            is_static,
            etype,
            interp,
            foreign,
        )

    # some linting

    if len(elf_usrshare) > 0:
        pkg.log_red("ELF files in /usr/share:")
        for f in elf_usrshare:
            print(f"  {f}")
        pkg.error(None)

    if len(elf_textrels) > 0:
        pkg.log_red("found textrels:")
        for f in elf_textrels:
            print(f"  {f}")
        pkg.error(None)

    if len(elf_xstack) > 0:
        pkg.log_red("found executable stack:")
        for f in elf_xstack:
            print(f"  {f}")
        pkg.error(None)

    if len(elf_foreign) > 0:
        pkg.log_red("found foreign-machine ELF files:")
        for f in elf_foreign:
            print(f"  {f}")
        pkg.error(None)

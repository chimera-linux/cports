import subprocess
import pathlib

def scan(pkg, somap):
    scandir = pkg.destdir

    # %o: type, %t: textrels status, %n: needed, %S: soname
    scanout = subprocess.run(
        [
            "scanelf", "--nobanner", "--nocolor", "--recursive", "--symlink",
            "--format", "%a|%b|%o|%t|%n|%S|", str(pkg.destdir)
        ],
        capture_output = True
    )

    if scanout.returncode != 0:
        pkg.error("failed to scan shlibs")

    elf_usrshare = []
    elf_textrels = []

    for ln in scanout.stdout.splitlines():
        mtype, bind, stp, textrel, needed, soname, fpath = ln.split(b"|")
        # elf used as container files
        if mtype.strip() == b"EM_NONE":
            continue
        # object files
        if stp.strip() == b"ET_REL":
            continue
        # get file
        fpath = pathlib.Path(fpath.strip().decode()).relative_to(pkg.destdir)
        # deny /usr/share files
        if fpath.is_relative_to("usr/share"):
            elf_usrshare.append(fpath)
        # check textrels
        if textrel.strip() != b"-" and not pkg.rparent.options["textrels"]:
            elf_textrels.append(fpath)
        # get a list
        needed = needed.strip().decode()
        if len(needed) == 0:
            needed = []
        else:
            needed = needed.split(",")
        # sanitize
        if len(soname) == 0:
            soname = None
        else:
            soname = soname.decode()
        # write
        somap[str(fpath)] = (
            soname, needed, pkg.pkgname, bind.strip() == b"STATIC"
        )

    # some linting

    if len(elf_usrshare) > 0:
        try:
            pkg.error("ELF files in /usr/share:")
        except:
            for f in elf_usrshare:
                print(f"   {str(f)}")
            raise

    if len(elf_textrels) > 0:
        try:
            pkg.error("found textrels:")
        except:
            for f in elf_textrels:
                print(f"   {str(f)}")
            raise

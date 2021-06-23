import subprocess
import pathlib

def scan(pkg, somap):
    scandir = pkg.destdir

    # %o: type, %t: textrels status, %n: needed, %S: soname
    scanout = subprocess.run(
        [
            "scanelf", "--nobanner", "--nocolor", "--recursive", "--symlink",
            "--format", "%o|%t|%n|%S|", str(pkg.destdir)
        ],
        capture_output = True
    )

    if scanout.returncode != 0:
        pkg.error("failed to scan shlibs")

    for ln in scanout.stdout.splitlines():
        stp, textrel, needed, soname, fpath = ln.split(b"|")
        # object files
        if stp == "ET_REL":
            continue
        # check textrels
        if textrel.strip() != b"-" and not pkg.allow_textrels:
            pkg.error(f"{fpath} contains textrels!")
        # get file
        fpath = pathlib.Path(fpath.strip().decode()).relative_to(pkg.destdir)
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
        somap[str(fpath)] = (soname, needed, pkg.pkgname)

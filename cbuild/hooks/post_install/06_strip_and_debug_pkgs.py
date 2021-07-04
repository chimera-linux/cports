import shutil
import subprocess

def make_debug(pkg, f, relf):
    if pkg.rparent.nodebug or not pkg.rparent.build_dbg:
        return

    dfile = pkg.destdir / "usr/lib/debug" / relf
    cfile = pkg.chroot_destdir / "usr/lib/debug" / relf

    dfile.parent.mkdir(parents = True, exist_ok = True)
    try:
        pkg.rparent.do(pkg.rparent.tools["OBJCOPY"], [
            "--only-keep-debug",
            str(pkg.chroot_destdir / relf), str(cfile)
        ])
    except:
        pkg.error(f"failed to create dbg file for {str(relf)}")

    dfile.chmod(0o644)

def attach_debug(pkg, f, relf):
    if pkg.rparent.nodebug or not pkg.rparent.build_dbg:
        return

    cfile = pkg.chroot_destdir / "usr/lib/debug" / relf
    try:
        pkg.rparent.do(pkg.rparent.tools["OBJCOPY"], [
            "--add-gnu-debuglink=" + str(cfile),
            str(pkg.chroot_destdir / relf)
        ])
    except:
        pkg.error(f"failed to attach debug link to {str(relf)}")

def invoke(pkg):
    if pkg.nostrip:
        return

    strip_path = "/usr/bin/" + pkg.rparent.tools["STRIP"]
    dbgdir = pkg.destdir / "usr/lib/debug"

    elfs = pkg.rparent.current_elfs

    for v in pkg.destdir.rglob("*"):
        # already stripped debug symbols
        if v.is_relative_to(dbgdir):
            continue

        # must be a regular file
        if not v.is_file() or v.is_symlink():
            continue

        vr = v.relative_to(pkg.destdir)

        # must be either found in elfs, or be a static lib
        vt = elfs.get(str(vr), None)
        if not vt:
            with open(v, "rb") as ef:
                if ef.read(8) != b"!<arch>\n":
                    continue
                # empty archive
                if ef.read(1) == b"":
                    continue

        found_nostrip = True

        # match against patterns in nostrip_files, if found, skip
        for f in pkg.nostrip_files:
            if vr.match(f):
                break
        else:
            found_nostrip = False

        # explicitly not to be stripped
        if found_nostrip:
            continue

        # now we've got a file we definitely can strip
        cfile = str(pkg.chroot_destdir / vr)

        # strip static library
        if not vt:
            v.chmod(0o644)
            try:
                pkg.rparent.do(strip_path, ["--strip-debug", cfile])
            except:
                pkg.error(f"failed to strip {str(vr)}")

            print(f"   Stripped static library: {str(vr)}")
            continue

        soname, needed, pname, static = vt

        # strip static executable
        if static:
            v.chmod(0o755)
            try:
                pkg.rparent.do(strip_path, [cfile])
            except:
                pkg.error(f"failed to strip {str(vr)}")

            print(f"   Stripped static executable: {str(vr)}")
            continue

        # guess what it is
        scanout = subprocess.run([
            "scanelf", "--nobanner", "--nocolor",
            "--format", "%a|%o|%i", str(v)
        ], capture_output = True)

        if scanout.returncode != 0:
            pkg.error(f"failed to scan {str(vr)}")

        # strip the filename
        scanout = scanout.stdout.strip()[:-len(str(v)) - 1]

        # get the type and interpreter
        splitv = scanout.split(b"|")
        if len(splitv) != 3:
            pkg.error(
                f"invalid scanelf output for {str(vr)}: {scanout.encode()}"
            )
        mtype, etype, interp = splitv

        # may just be using ELF as a container format
        if mtype.strip() == b"EM_NONE":
            print(f"   Ignoring ELF file with no machine: {str(vr)}")

        # pie or nopie?
        if etype == b"ET_DYN":
            pie = True
        elif etype == b"ET_EXEC":
            pie = False
        else:
            pkg.error(f"unknown type for {str(vr)}: {etype.encode()}")

        # executable or library?
        dynlib = (len(interp.strip()) == 0)

        # sanity check
        if not pie and dynlib:
            pkg.error(f"dynamic executable without an interpreter: {str(vr)}")

        # regardless, sanitize mode
        v.chmod(0o755)

        # strip nopie executable
        if not pie:
            make_debug(pkg, v, vr)
            try:
                pkg.rparent.do(strip_path, [cfile])
            except:
                pkg.error(f"failed to strip {str(vr)}")

            print(f"   Stripped executable: {str(vr)}")

            allow_nopie = False
            if pkg.hardening["pie"]:
                for f in pkg.nopie_files:
                    if vr.match(f):
                        allow_nopie = True
                        break
            else:
                allow_nopie = True

            if not allow_nopie:
                pkg.error(f"non-PIE executable found in PIE build: {str(vr)}")

            attach_debug(pkg, v, vr)
            continue

        # strip pie executable or shared library
        make_debug(pkg, v, vr)
        try:
            pkg.rparent.do(strip_path, ["--strip-unneeded", cfile])
        except:
            pkg.error(f"failed to strip {str(vr)}")

        if not dynlib:
            print(f"   Stripped position-independent executable: {str(vr)}")
        else:
            print(f"   Stripped library: {str(vr)}")

        attach_debug(pkg, v, vr)

        # strip shared library

    # prepare debug package
    if pkg.rparent.nodebug or not pkg.rparent.build_dbg:
        return

    # no debug symbols found
    if not (pkg.destdir / "usr/lib/debug").is_dir():
        return

    ddest = pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg-{pkg.version}"
    (ddest / "usr/lib").mkdir(parents = True, exist_ok = True)

    # move debug symbols
    try:
        shutil.move(pkg.destdir / "usr/lib/debug", ddest / "usr/lib")
    except:
        pkg.error("failed to cerate debug package")

    # try removing the libdir
    for f in (pkg.destdir / "usr/lib").iterdir():
        break
    else:
        (pkg.destdir / "usr/lib").rmdir()

    # done!
    return

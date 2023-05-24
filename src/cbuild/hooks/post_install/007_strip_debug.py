import shutil
import subprocess
import stat


def make_debug(pkg, f, relf):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    dfile = pkg.destdir / "usr/lib/debug" / relf
    cfile = pkg.chroot_destdir / "usr/lib/debug" / relf

    dfile.parent.mkdir(parents=True, exist_ok=True)
    try:
        pkg.rparent.do(
            pkg.rparent.get_tool("OBJCOPY"),
            "--only-keep-debug",
            pkg.chroot_destdir / relf,
            cfile,
        )
    except:
        pkg.error(f"failed to create dbg file for {relf}")

    dfile.chmod(0o644)


def attach_debug(pkg, f, relf):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    cfile = pkg.chroot_destdir / "usr/lib/debug" / relf
    try:
        pkg.rparent.do(
            pkg.rparent.get_tool("OBJCOPY"),
            f"--add-gnu-debuglink={cfile}",
            pkg.chroot_destdir / relf,
        )
    except:
        pkg.error(f"failed to attach debug link to {relf}")


def _sanitize_exemode(f):
    st = f.lstat()
    mode = 0o755
    if st.st_mode & stat.S_ISUID:
        mode |= 0o4000
    if st.st_mode & stat.S_ISGID:
        mode |= 0o2000
    f.chmod(mode)


def invoke(pkg):
    if not pkg.options["strip"]:
        return

    strip_path = "/usr/bin/" + pkg.rparent.get_tool("STRIP")
    dbgdir = pkg.destdir / "usr/lib/debug"

    elfs = pkg.rparent.current_elfs

    have_pie = pkg.rparent.has_hardening("pie")

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

        # strip static library, only if not LTO or when forced
        if not vt:
            v.chmod(0o644)
            if not pkg.rparent.has_lto() or pkg.options["ltostrip"]:
                try:
                    pkg.rparent.do(strip_path, "--strip-debug", cfile)
                except:
                    pkg.error(f"failed to strip {vr}")

                print(f"   Stripped static library: {vr}")
            # in any case continue
            continue

        soname, needed, pname, static, etype, interp, foreign = vt

        # strip static executable
        if static:
            _sanitize_exemode(v)
            try:
                pkg.rparent.do(strip_path, cfile)
            except:
                pkg.error(f"failed to strip {vr}")

            print(f"   Stripped static executable: {vr}")
            continue

        # pie or nopie?
        if etype == "ET_DYN":
            pie = True
        elif etype == "ET_EXEC":
            pie = False
        else:
            pkg.error(f"unknown type for {vr}: {etype}")

        # sanity check
        if not pie and not interp:
            pkg.error(f"dynamic executable without an interpreter: {vr}")

        # regardless, sanitize mode
        _sanitize_exemode(v)

        # strip nopie executable
        if not pie:
            make_debug(pkg, v, vr)
            try:
                pkg.rparent.do(strip_path, cfile)
            except:
                pkg.error(f"failed to strip {vr}")

            print(f"   Stripped executable: {vr}")

            allow_nopie = False
            if have_pie:
                for f in pkg.nopie_files:
                    if vr.match(f):
                        allow_nopie = True
                        break
            else:
                allow_nopie = True

            if not allow_nopie:
                pkg.error(f"non-PIE executable found in PIE build: {vr}")

            attach_debug(pkg, v, vr)
            continue

        # strip pie executable or shared library
        make_debug(pkg, v, vr)
        try:
            pkg.rparent.do(strip_path, "--strip-unneeded", cfile)
        except:
            pkg.error(f"failed to strip {vr}")

        if interp:
            print(f"   Stripped position-independent executable: {vr}")
        else:
            print(f"   Stripped library: {vr}")

        attach_debug(pkg, v, vr)

        # strip shared library

    # prepare debug package
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    # no debug symbols found
    if not (pkg.destdir / "usr/lib/debug").is_dir():
        return

    ddest = pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg-{pkg.pkgver}"
    (ddest / "usr/lib").mkdir(parents=True, exist_ok=True)

    # move debug symbols
    try:
        shutil.move(pkg.destdir / "usr/lib/debug", ddest / "usr/lib")
    except:
        pkg.error("failed to create debug package")

    # try removing the libdir
    for f in (pkg.destdir / "usr/lib").iterdir():
        break
    else:
        (pkg.destdir / "usr/lib").rmdir()

    # done!
    return

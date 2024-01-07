from cbuild.util import strip

import shutil
import stat


def _sanitize_exemode(f):
    st = f.lstat()
    # suid/sgid binaries don't get normalized (unsafe)
    # though it mostly does not matter as all suid binaries
    # are detected by cbuild and the template always sets
    # their actual final mode explicitly... but just in case
    if (st.st_mode & stat.S_ISUID) or (st.st_mode & stat.S_ISGID):
        return
    f.chmod(0o755)


def invoke(pkg):
    if not pkg.options["strip"]:
        return

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

        # strip static library, only if not LTO or when forced
        if not vt:
            v.chmod(0o644)
            if not pkg.rparent.has_lto() or pkg.options["ltostrip"]:
                sp = strip.strip(pkg, v)
                print(f"   Stripped static library: {sp}")
            # in any case continue
            continue

        soname, needed, pname, static, etype, interp, foreign = vt

        # strip static executable
        if static:
            _sanitize_exemode(v)
            sp = strip.strip(pkg, v)
            print(f"   Stripped static executable: {sp}")
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

            sp = strip.strip_attach(pkg, v)
            print(f"   Stripped executable: {sp}")
            continue

        # strip pie executable or shared library
        sp = strip.strip_attach(pkg, v)
        if interp:
            print(f"   Stripped position-independent executable: {sp}")
        else:
            print(f"   Stripped library: {sp}")

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
    except Exception:
        pkg.error("failed to create debug package")

    # try removing the libdir
    for f in (pkg.destdir / "usr/lib").iterdir():
        break
    else:
        (pkg.destdir / "usr/lib").rmdir()

    # done!
    return

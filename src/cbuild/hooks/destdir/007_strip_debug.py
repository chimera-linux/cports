from cbuild.util import strip

import shutil
import stat


def _sanitize_exemode(pkg, f, vr):
    # don't normalize if file_modes specifies this, as that would
    # revert what the packager actually wanted to set
    if vr in pkg.file_modes:
        return
    st = f.lstat()
    # don't normalize suid files; it would render the suid detector
    # useless, and we require all suid files as well as files with
    # security xattrs to have an explicitly specified mode in the
    # template (for tighter control)
    if (st.st_mode & stat.S_ISUID) or (st.st_mode & stat.S_ISGID):
        return
    f.chmod(0o755)


def invoke(pkg):
    if not pkg.options["strip"]:
        return

    dbgdir = pkg.destdir / "usr/lib/debug"
    elfs = pkg.rparent.current_elfs
    have_pie = pkg.rparent.has_hardening("pie")

    strip_list = []
    strip_noslist = []

    log = pkg.logger

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
                log.out_plain(f"  \f[purple]static library:\f[] {vr}")
                strip_list.append(vr)
                strip_noslist.append(vr)
            # in any case continue
            continue

        soname, needed, pname, static, etype, interp, foreign = vt

        # strip static executable
        if static:
            _sanitize_exemode(pkg, v, str(vr))
            log.out_plain(f"  \f[green]static executable:\f[] {vr}")
            strip_list.append(vr)
            strip_noslist.append(vr)
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
        _sanitize_exemode(pkg, v, str(vr))

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

            strip_list.append(vr)
            log.out_plain(f"  \f[green]executable:\f[] {vr}")
            continue

        # strip pie executable or shared library
        strip_list.append(vr)
        # technically there may be libraries with an interpreter set,
        # so this is not completely robust, but there is no other way
        # to differentiate it (DF_1_PIE may not always be set) and it
        # is harmless, so do it anyway...
        #
        # the "interp is False" case means we explicitly detected DF_1_PIE
        # without having an interpreter, which is a guaranteed static-pie
        # executable, every other case is a guaranteed library
        if interp:
            log.out_plain(f"  \f[green]pie executable:\f[] {vr}")
        elif interp is False:
            log.out_plain(f"  \f[green]static-pie executable:\f[] {vr}")
        else:
            log.out_plain(f"  \f[cyan]library:\f[] {vr}")

    strip.strip_attach(pkg, strip_list, strip_noslist)

    # prepare debug package
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    # no debug symbols found
    if not (pkg.destdir / "usr/lib/debug").is_dir():
        return

    ddest = pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg"
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

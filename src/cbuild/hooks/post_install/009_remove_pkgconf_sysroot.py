# this hook replaces all occurences of the cross sysroot in .pc files so that
# cross builds do not differ from native ones (e.g. /usr/ARCH/usr -> /usr)


def invoke(pkg):
    sr = str(pkg.rparent.profile().sysroot / "usr")

    for f in pkg.destdir.glob("usr/*/pkgconfig/*.pc"):
        if not f.is_file() or f.is_symlink():
            continue
        ofp = f.with_suffix(".new")

        with open(f) as inf:
            with open(ofp, "w") as outf:
                for ln in inf:
                    outf.write(ln.replace(sr, "/usr"))

        ofp.chmod(0o644)
        ofp.rename(f)

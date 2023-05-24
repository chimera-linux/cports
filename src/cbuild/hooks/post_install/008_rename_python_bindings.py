import stat


def invoke(pkg):
    for v in (pkg.destdir / "usr/lib").glob(
        "python*/site-packages/**/*.cpython*.so"
    ):
        st = v.lstat()
        if not (st.st_mode & stat.S_IXUSR):
            continue
        oldname = v.name
        newname = oldname[: -len("".join(v.suffixes))]
        pkg.log_warn(f"renamed '{oldname}' to '{newname}.so'")
        v.rename(v.parent / (newname + ".so"))

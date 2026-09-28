# this removes arch suffix from native python modules; while for normal
# builds this makes no difference, this hook exists mainly to deal with
# crossbuilds as any native modules that are crossbuilt are built with
# the crosscompiler but sitll get a host arch suffix, which will then
# fail to load in the target environment

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
        v.rename(v.parent / (newname + ".so"))

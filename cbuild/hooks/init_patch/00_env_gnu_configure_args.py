from cbuild.core import paths

from os.path import join

def invoke(pkg):
    if pkg.build_style and pkg.build_style != "gnu_configure":
        return

    cargs = [
        "--prefix=/usr", "--sysconfdir=/etc", "--sbindir=/usr/bin",
        "--bindir=/usr/bin", "--mandir=/usr/share/man",
        "--infodir=/usr/share/info", "--localstatedir=/var"
    ]

    if pkg.triplet:
        cargs.append("--build=" + pkg.triplet)
        cargs.append("--host=" + pkg.triplet)

    # prepend
    pkg.configure_args = cargs + pkg.configure_args

    # autoconf cache
    cachedir = join(paths.cbuild(), "misc", "autoconf_cache")
    with open(join(cachedir, "musl-linux")) as f:
        for ln in f.readlines():
            ln = ln.strip()
            if len(ln) == 0 or ln[0] == "#":
                continue
            pos = ln.find("=")
            if pos >= 0:
                pkg.env[ln[0:pos]] = ln[pos + 1:]
            else:
                pkg.env[ln] = "yes"

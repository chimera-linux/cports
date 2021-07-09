from cbuild.core import paths

def configure(pkg, meson_dir = None, build_dir = "build", extra_args = []):
    if not meson_dir:
        meson_dir = "."

    pkg.do(
        "meson", [
            "--prefix=/usr",
            "--libdir=/usr/lib",
            "--libexecdir=/usr/libexec",
            "--bindir=/usr/bin",
            "--sbindir=/usr/bin",
            "--includedir=/usr/include",
            "--datadir=/usr/share",
            "--mandir=/usr/share/man",
            "--infodir=/usr/share/info",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--sharedstatedir=/var/lib",
            "--buildtype=plain",
            "--auto-features=auto",
            "--wrap-mode=nodownload",
            "-Ddefault_library=both",
            "-Db_ndebug=true",
            "-Db_staticpic=true"
        ] + pkg.configure_args + extra_args + [meson_dir, build_dir],
        build = True
    )

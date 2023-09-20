pkgname = "gettext"
pkgver = "0.22.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-java",
    "--disable-csharp",
    "--disable-libasprintf",
    "--enable-threads=posix",
]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "automake", "libtool", "xz"]
makedepends = ["libunistring-devel", "libxml2-devel", "ncurses-devel"]
checkdepends = ["perl", "bash"]
pkgdesc = "GNU internationalization utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gettext"
source = f"$(GNU_SITE)/gettext/gettext-{pkgver}.tar.gz"
sha256 = "a99662bafc1cc683ec7740844b465c7f30ccb044967f157f74697df9a9306b0e"
# most tests fail to find an adequate shell ???
options = ["!check"]
# broken ass autotools
exec_wrappers = [("/usr/bin/gmake", "make")]


def post_extract(self):
    self.cp(self.files_path / "libintl.c", ".")


def post_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(["libintl.c"], "libintl.o", obj_file=True, flags=["-fno-lto"])


def post_install(self):
    self.do(
        self.get_tool("AR"),
        "rcs",
        self.chroot_destdir / "usr/lib/libintl.a",
        "libintl.o",
    )


@subpackage("gettext-libs")
def _libs(self):
    return self.default_libs(
        extra=[
            f"usr/lib/libgettextlib-{pkgver}.so",
            f"usr/lib/libgettextsrc-{pkgver}.so",
        ]
    )


@subpackage("gettext-libintl")
def _libintl(self):
    self.pkgdesc = f"{pkgdesc} (libintl stub)"
    self.options = ["!splitstatic", "ltostrip"]

    return ["usr/lib/libintl.a"]


@subpackage("gettext-devel")
def _devel(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        f"{pkgname}-libintl={pkgver}-r{pkgrel}",
        "cmd:tar!bsdtar",
        "cmd:xz!xz",
    ]

    return self.default_devel(
        extra=[
            "usr/bin/autopoint",
            "usr/bin/gettextize",
            "usr/share/man/man1/autopoint.1",
            "usr/share/man/man1/gettextize.1",
        ]
    )

pkgname = "gettext"
pkgver = "0.23.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-java",
    "--disable-csharp",
    "--disable-libasprintf",
    "--enable-threads=posix",
]
make_check_args = ["-j1"]
hostmakedepends = ["automake", "libtool", "xz"]
makedepends = ["libunistring-devel", "libxml2-devel", "ncurses-devel"]
checkdepends = ["perl", "bash"]
pkgdesc = "GNU internationalization utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gettext"
source = f"$(GNU_SITE)/gettext/gettext-{pkgver}.tar.gz"
sha256 = "52a578960fe308742367d75cd1dff8552c5797bd0beba7639e12bdcda28c0e49"
# most tests fail to find an adequate shell ???
options = ["!check"]


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
def _(self):
    return self.default_libs(
        extra=[
            f"usr/lib/libgettextlib-{pkgver}.so",
            f"usr/lib/libgettextsrc-{pkgver}.so",
        ]
    )


@subpackage("gettext-libintl")
def _(self):
    self.subdesc = "libintl stub"
    self.options = ["!splitstatic", "ltostrip"]

    return ["usr/lib/libintl.a"]


@subpackage("gettext-devel")
def _(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-libintl"),
        "cmd:tar!libarchive-progs",
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

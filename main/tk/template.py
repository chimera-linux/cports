pkgname = "tk"
pkgver = "9.0.0"
pkgrel = 0
build_wrksrc = "unix"
build_style = "gnu_configure"
configure_args = [
    "--enable-threads",
    "--enable-man-symlinks",
    "--disable-rpath",
    "--without-tzdata",
    "tk_cv_strtod_unbroken=ok",
    "LIBS=-ltcl9.0",
]
make_dir = "."
hostmakedepends = ["automake", "pkgconf", "zip"]
makedepends = [
    "zlib-ng-compat-devel",
    "tcl-devel",
    "libxext-devel",
    "libxscrnsaver-devel",
    "libxft-devel",
]
provides = ["so:libtk9.0.so=0"]
pkgdesc = "TK graphical user interface toolkit for TCL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/tk{pkgver}-src.tar.gz"
sha256 = "f166e3c20773c82243f753cef4b091d05267cb7f87da64be88cb2ca5a2ba027e"
# no check target
options = ["!check", "!cross", "!lto"]


def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]


def post_install(self):
    self.install_link("usr/bin/wish", "wish9.0")
    self.install_license("../license.terms")


@subpackage("tk-devel")
def _(self):
    self.options = ["!splitstatic"]
    return self.default_devel(
        extra=[
            "usr/lib/tkConfig.sh",
            "usr/share/man/mann",
        ]
    )

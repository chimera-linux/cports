pkgname = "tk"
pkgver = "8.6.14"
pkgrel = 0
build_wrksrc = "unix"
build_style = "gnu_configure"
configure_args = [
    "--enable-threads",
    "--enable-man-symlinks",
    "--disable-rpath",
    "--without-tzdata",
    "tk_cv_strtod_unbroken=ok",
    "LIBS=-ltcl8.6",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "tcl-devel",
    "libxext-devel",
    "libxscrnsaver-devel",
    "libxft-devel",
]
provides = ["so:libtk8.6.so=0"]
pkgdesc = "TK graphical user interface toolkit for TCL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/{pkgname}{pkgver}-src.tar.gz"
sha256 = "8ffdb720f47a6ca6107eac2dd877e30b0ef7fac14f3a84ebbd0b3612cee41a94"
# no check target
options = ["!check", "!cross", "!lto"]


def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]


def post_install(self):
    self.install_link("usr/bin/wish", "wish8.6")
    self.install_license("../license.terms")


@subpackage("tk-devel")
def _devel(self):
    self.options = ["!splitstatic"]
    return self.default_devel(
        extra=[
            "usr/lib/tkConfig.sh",
            "usr/share/man/mann",
        ]
    )

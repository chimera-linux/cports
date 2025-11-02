pkgname = "tk"
pkgver = "8.6.17"
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
    "libxext-devel",
    "libxft-devel",
    "libxscrnsaver-devel",
    "tcl-devel",
    "zlib-ng-compat-devel",
]
provides = ["so:libtk8.6.so=0"]
pkgdesc = "TK graphical user interface toolkit for TCL"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/tk{pkgver}-src.tar.gz"
sha256 = "e4982df6f969c08bf9dd858a6891059b4a3f50dc6c87c10abadbbe2fc4838946"
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
def _(self):
    self.options = ["!splitstatic"]
    return self.default_devel(
        extra=[
            "usr/lib/tkConfig.sh",
            "usr/share/man/mann",
        ]
    )

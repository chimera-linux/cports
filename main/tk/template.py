pkgname = "tk"
pkgver = "8.6.12"
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
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "tcl-devel", "libxext-devel", "libxscrnsaver-devel",
    "libxft-devel"
]
provides = ["so:libtk8.6.so=0"]
pkgdesc = "TK graphical user interface toolkit for TCL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/{pkgname}{pkgver}-src.tar.gz"
sha256 = "12395c1f3fcb6bed2938689f797ea3cdf41ed5cb6c4766eec8ac949560310630"
# no check target
options = ["!check", "!cross", "!lto"]

def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]

def post_install(self):
    self.install_link("wish8.6", "usr/bin/wish")
    self.install_license("../license.terms")

@subpackage("tk-devel")
def _devel(self):
    self.options = ["!splitstatic"]

    return [
        "usr/lib/tkConfig.sh",
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
        "usr/share/man/mann",
        "usr/lib/*.a",
    ]

# FIXME visibility
hardening = ["!vis"]

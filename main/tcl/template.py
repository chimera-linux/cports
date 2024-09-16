pkgname = "tcl"
pkgver = "8.6.15"
pkgrel = 0
build_wrksrc = "unix"
build_style = "gnu_configure"
configure_args = [
    "--enable-threads",
    "--enable-man-symlinks",
    "--disable-rpath",
    "--with-system-sqlite",
    "--without-tzdata",
    "tcl_cv_strstr_unbroken=ok",
    "tcl_cv_strtoul_unbroken=ok",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "sqlite-devel"]
provides = ["so:libtcl8.6.so=0"]
pkgdesc = "TCL scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/tcl{pkgver}-src.tar.gz"
sha256 = "861e159753f2e2fbd6ec1484103715b0be56be3357522b858d3cbb5f893ffef1"
# no check target
options = ["!check", "!lto", "!splitstatic"]


def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]


def post_install(self):
    self.install_link("usr/bin/tclsh", "tclsh8.6")
    self.install_license("../license.terms")


@subpackage("tcl-devel")
def _(self):
    self.depends += [self.parent]
    self.options = ["!splitstatic"]
    return self.default_devel(extra=["usr/lib/*.sh"])

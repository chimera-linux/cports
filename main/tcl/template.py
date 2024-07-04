pkgname = "tcl"
pkgver = "8.6.14"
pkgrel = 1
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
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}{pkgver}-src.tar.gz"
sha256 = "5880225babf7954c58d4fb0f5cf6279104ce1cd6aa9b71e9a6322540e1c4de66"
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
def _devel(self):
    self.depends += [f"tcl={pkgver}-r{pkgrel}"]
    self.options = ["!splitstatic"]
    return self.default_devel(extra=["usr/lib/*.sh"])

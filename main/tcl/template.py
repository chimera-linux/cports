pkgname = "tcl"
pkgver = "9.0.0"
pkgrel = 0
build_wrksrc = "unix"
build_style = "gnu_configure"
configure_args = [
    "--enable-threads",
    "--enable-man-symlinks",
    "--disable-rpath",
    "--disable-zipfs",
    "--with-system-sqlite",
    "--without-tzdata",
    "tcl_cv_strstr_unbroken=ok",
    "tcl_cv_strtoul_unbroken=ok",
]
make_dir = "."
hostmakedepends = ["automake", "pkgconf", "zip"]
makedepends = ["musl-bsd-headers", "zlib-ng-compat-devel", "sqlite-devel"]
provides = ["so:libtcl9.0.so=0"]
pkgdesc = "TCL scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/tcl{pkgver}-src.tar.gz"
sha256 = "3bfda6dbaee8e9b1eeacc1511b4e18a07a91dff82d9954cdb9c729d8bca4bbb7"
# no check target
options = ["!check", "!lto", "!splitstatic"]


def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]


def post_install(self):
    self.install_link("usr/bin/tclsh", "tclsh9.0")
    self.install_license("../license.terms")


@subpackage("tcl-devel")
def _(self):
    self.depends += [self.parent]
    self.options = ["!splitstatic"]
    return self.default_devel(extra=["usr/lib/*.sh"])

pkgname = "tcl"
pkgver = "8.6.12"
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
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel", "sqlite-devel"]
provides = ["so:libtcl8.6.so=0"]
pkgdesc = "TCL scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}{pkgver}-src.tar.gz"
sha256 = "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6"
# no check target
options = ["!check", "!lto"]

def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]

def post_install(self):
    self.install_link("tclsh8.6", "usr/bin/tclsh")
    self.install_license("../license.terms")

@subpackage("tcl-devel")
def _devel(self):
    self.depends += [f"tcl={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/tclConfig.sh",
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
        "usr/lib/*.a",
    ]

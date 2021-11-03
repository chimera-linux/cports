pkgname = "tcl"
pkgver = "8.6.11"
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
sha256 = "8c0486668586672c5693d7d95817cb05a18c5ecca2f40e2836b9578064088258"
# no check target
options = ["!check"]

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
    return [
        "usr/lib/tclConfig.sh",
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
        "usr/lib/*.a",
    ]

pkgname = "pcre"
pkgver = "8.45"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-pic",
    "--enable-utf8",
    "--enable-unicode-properties",
    "--enable-pcretest-libedit",
    "--enable-pcregrep-libz",
    "--enable-pcregrep-libbz2",
    "--enable-newline-is-anycrlf",
    "--enable-jit",
    "--enable-static",
    "--disable-stack-for-recursion",
]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel", "libbz2-devel", "libedit-devel"]
pkgdesc = "Perl Compatible Regular Expressions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.pcre.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "4dae6fdcd2bb0bb6c37b5f97c33c2be954da743985369cddac3546e3218bffb8"
options = ["!cross"]

match self.profile().arch:
    case "riscv64":
        configure_args += ["--disable-jit"]

def post_install(self):
    self.install_license("LICENCE")

@subpackage("libpcrecpp")
def _libpcrecpp(self):
    self.pkgdesc = f"{pkgdesc} (C++ shared libraries)"
    return ["usr/lib/libpcrecpp.so.*"]

@subpackage("libpcre")
def _libpcre(self):
    self.pkgdesc = f"{pkgdesc} (shared libraries)"
    return self.default_libs()

@subpackage("pcre-devel")
def _devel(self):
    self.depends += ["zlib-devel", "libbz2-devel"]
    return self.default_devel(extra = ["usr/share/doc"])

configure_gen = []

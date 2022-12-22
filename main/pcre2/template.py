pkgname = "pcre2"
pkgver = "10.40"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-pic",
    "--enable-pcre2-16",
    "--enable-pcre2-32",
    "--enable-pcre2test-libedit",
    "--enable-pcre2grep-libz",
    "--enable-pcre2grep-libbz2",
    "--enable-newline-is-anycrlf",
    "--enable-jit",
    "--enable-static",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["zlib-devel", "libbz2-devel", "libedit-devel"]
pkgdesc = "Perl Compatible Regular Expressions v2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.pcre.org"
source = f"https://github.com/PhilipHazel/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ded42661cab30ada2e72ebff9e725e745b4b16ce831993635136f2ef86177724"

match self.profile().arch:
    case "riscv64":
        configure_args += ["--disable-jit"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("LICENCE")

@subpackage("libpcre2")
def _libpcre2(self):
    self.pkgdesc = f"{pkgdesc} (shared libraries)"
    return self.default_libs()

@subpackage("pcre2-devel")
def _devel(self):
    self.depends += ["zlib-devel", "libbz2-devel"]
    return self.default_devel(extra = ["usr/share/doc"])

# FIXME visibility
hardening = ["!vis"]

pkgname = "pcre2"
pkgver = "10.44"
pkgrel = 2
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
makedepends = ["zlib-ng-compat-devel", "bzip2-devel", "libedit-devel"]
pkgdesc = "Perl Compatible Regular Expressions v2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.pcre.org"
source = f"https://github.com/PCRE2Project/pcre2/releases/download/pcre2-{pkgver}/pcre2-{pkgver}.tar.gz"
sha256 = "86b9cb0aa3bcb7994faa88018292bc704cdbb708e785f7c74352ff6ea7d3175b"

match self.profile().arch:
    # aarch64 FIXME: segfault in pcre2_jit_neon_inc.h during testing
    case "riscv64" | "aarch64":
        configure_args += ["--disable-jit"]


def post_install(self):
    self.install_license("LICENCE")


@subpackage("pcre2-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libpcre2")]

    return self.default_libs()


@subpackage("pcre2-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel", "bzip2-devel"]
    return self.default_devel(extra=["usr/share/doc"])

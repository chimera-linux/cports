pkgname = "pcre2"
pkgver = "10.46"
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
makedepends = ["zlib-ng-compat-devel", "bzip2-devel", "libedit-devel"]
pkgdesc = "Perl Compatible Regular Expressions v2"
license = "BSD-3-Clause"
url = "https://www.pcre.org"
source = f"https://github.com/PCRE2Project/pcre2/releases/download/pcre2-{pkgver}/pcre2-{pkgver}.tar.gz"
sha256 = "8d28d7f2c3b970c3a4bf3776bcbb5adfc923183ce74bc8df1ebaad8c1985bd07"

match self.profile().arch:
    # aarch64 FIXME: segfault in pcre2_jit_neon_inc.h during testing
    case "riscv64" | "loongarch64" | "aarch64":
        configure_args += ["--disable-jit"]


def post_install(self):
    self.install_license("LICENCE.md")


@subpackage("pcre2-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libpcre2")]

    return self.default_libs()


@subpackage("pcre2-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel", "bzip2-devel"]
    return self.default_devel(extra=["usr/share/doc"])

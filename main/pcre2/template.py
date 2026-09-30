pkgname = "pcre2"
pkgver = "10.49"
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
    "--disable-symvers",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["zlib-ng-compat-devel", "bzip2-devel", "libedit-devel"]
pkgdesc = "Perl Compatible Regular Expressions v2"
license = "BSD-3-Clause"
url = "https://www.pcre.org"
source = f"https://github.com/PCRE2Project/pcre2/releases/download/pcre2-{pkgver}/pcre2-{pkgver}.tar.gz"
sha256 = "929f0b20e62879252a15886b06c89f1edef61a363cbd5826fb041080a5e557ae"

match self.profile.arch:
    # aarch64 FIXME: segfault in pcre2_jit_neon_inc.h during testing
    case "riscv64" | "loongarch64" | "aarch64":
        configure_args += ["--disable-jit"]


def post_install(self):
    self.install_license("LICENCE.md")


@subpackage("pcre2-libs")
def _(self):
    self.renames = ["libpcre2"]

    return self.default_libs()


@subpackage("pcre2-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel", "bzip2-devel"]
    return self.default_devel(extra=["usr/share/doc"])

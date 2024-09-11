pkgname = "pcre"
pkgver = "8.45"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-jit",
    "--enable-pcre16",
    "--enable-pcre32",
    "--enable-pcre8",
    "--enable-unicode-properties",
    "--enable-utf8",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Perl Compatible Regular Expressions"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://www.pcre.org"
source = f"https://downloads.sourceforge.net/project/pcre/pcre/{pkgver}/pcre-{pkgver}.tar.bz2"
sha256 = "4dae6fdcd2bb0bb6c37b5f97c33c2be954da743985369cddac3546e3218bffb8"

match self.profile().arch:
    case "riscv64" | "aarch64":
        configure_args += ["--disable-jit"]


def post_install(self):
    self.install_license("LICENCE")


@subpackage("libpcre")
def _(self):
    self.subdesc = "shared libraries"
    return self.default_libs()


@subpackage("pcre-devel")
def _(self):
    return self.default_devel()

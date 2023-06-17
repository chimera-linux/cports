pkgname = "utf8proc"
pkgver = "2.8.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Clean C library for processing UTF-8 Unicode data"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/JuliaStrings/utf8proc"
source = f"{url}/archive/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a0a60a79fe6f6d54e7d411facbfcc867a6e198608f2cd992490e46f04b1bcecc"
hardening = ["vis", "cfi"]
# cannot run check because Julia isn't packaged
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("utf8proc-devel")
def _devel(self):
    return self.default_devel()

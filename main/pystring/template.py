pkgname = "pystring"
pkgver = "1.1.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "C++ functions matching the interface of Python string methods"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://github.com/imageworks/pystring"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "49da0fe2a049340d3c45cce530df63a2278af936003642330287b68cefd788fb"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("pystring-devel")
def _(self):
    return self.default_devel()

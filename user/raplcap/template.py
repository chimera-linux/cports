pkgname = "raplcap"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["powercap-devel"]
pkgdesc = "RAPL power capping with multiple implementations"
license = "BSD-3-Clause"
url = "https://github.com/powercap/raplcap"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0402ab70ba031b40b567f93f4668a0ce7aa70eb72851947b0764d7757409974d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("raplcap-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("raplcap-devel")
def _(self):
    self.depends += [self.with_pkgver("raplcap-devel-static")]
    return self.default_devel()

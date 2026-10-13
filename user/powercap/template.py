pkgname = "powercap"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Glue to the Linux Power Capping Framework in sysfs"
license = "BSD-3-Clause"
url = "https://github.com/powercap/powercap"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4acd5ac85f297592b7006ed867ae5c73b3c5d7a3d6e773899609616fb9dd9b6c"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("powercap-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("powercap-devel")
def _(self):
    self.depends += [self.with_pkgver("powercap-devel-static")]
    return self.default_devel()

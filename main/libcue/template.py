pkgname = "libcue"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "bison", "flex"]
pkgdesc = "CUE sheet parser library"
license = "GPL-2.0-or-later AND BSD-2-Clause"
url = "https://github.com/lipnitsk/libcue"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "cc1b3a65c60bd88b77a1ddd1574042d83cf7cc32b85fe9481c99613359eb7cfe"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libcue-devel")
def _(self):
    return self.default_devel()

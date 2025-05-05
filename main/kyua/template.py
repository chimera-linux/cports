pkgname = "kyua"
pkgver = "0.14.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["atf-devel", "automake", "libtool", "pkgconf"]
makedepends = ["atf-devel", "lutok-devel", "sqlite-devel"]
pkgdesc = "Test framework for infrastructure software"
license = "BSD-3-Clause"
url = "https://github.com/freebsd/kyua"
source = f"{url}/releases/download/kyua-{pkgver}/kyua-{pkgver}.tar.gz"
sha256 = "3caf30a7e316f4f21c32e1c419ec80371fe113e3eed10ba1db9e6efc7ee15ecb"
tool_flags = {"CXXFLAGS": ["-std=gnu++11"]}


def post_install(self):
    self.install_license("LICENSE")

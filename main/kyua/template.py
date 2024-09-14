pkgname = "kyua"
pkgver = "0.13"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["atf-devel", "automake", "libtool", "pkgconf"]
makedepends = ["atf-devel", "lutok-devel", "sqlite-devel"]
pkgdesc = "Test framework for infrastructure software"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://github.com/freebsd/kyua"
source = f"{url}/releases/download/kyua-{pkgver}/kyua-{pkgver}.tar.gz"
sha256 = "db6e5d341d5cf7e49e50aa361243e19087a00ba33742b0855d2685c0b8e721d6"
tool_flags = {"CXXFLAGS": ["-std=gnu++11"]}


def post_install(self):
    self.uninstall("usr/tests")
    self.install_license("LICENSE")

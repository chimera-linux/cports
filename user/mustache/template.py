pkgname = "mustache"
pkgver = "4.1"
pkgrel = 0
pkgdesc = "Mustache text templates for modern C++"
license = "BSL-1.0"
url = "https://github.com/kainjow/Mustache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acd66359feb4318b421f9574cfc5a511133a77d916d0b13c7caa3783c0bfe167"
# header-only library
options = ["!check"]


def install(self):
    self.install_file("mustache.hpp", "usr/include/kainjow")
    self.install_license("LICENSE")

pkgname = "mustache"
pkgver = "4.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Mustache text templates for modern C++"
license = "BSL-1.0"
url = "https://github.com/kainjow/Mustache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acd66359feb4318b421f9574cfc5a511133a77d916d0b13c7caa3783c0bfe167"


def check(self):
    self.do(f"{self.make_dir}/mustache")


def install(self):
    self.install_file("mustache.hpp", "usr/include")
    self.install_license("LICENSE")

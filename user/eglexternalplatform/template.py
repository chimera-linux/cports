pkgname = "eglexternalplatform"
pkgver = "1.1"
pkgrel = 0
hostmakedepends = ["pkgconf"]
pkgdesc = "EGL external platform interface"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = "https://github.com/NVIDIA/eglexternalplatform"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "72725c4c9dd06b4d44bceb8794e1e78f75ed8702be23201282f8f937252a6b32"


def do_install(self):
    for path in self.cwd.glob("interface/*.h"):
        self.install_file(path, "usr/include/EGL")

    self.install_file("eglexternalplatform.pc", "usr/lib/pkgconfig")


def post_install(self):
    self.install_license("COPYING")

pkgname = "libsysstat"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "pkgconf"]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Library used to query system info and statistics"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libsysstat"
source = f"{url}/releases/download/{pkgver}/libsysstat-{pkgver}.tar.xz"
sha256 = "dc552c39aeeba772cd4a5fa2902a368f70420e4408eb834d834ec5125d6c931e"


@split("devel")
def _(self):
    return self.default_devel()

pkgname = "libqtxdg"
pkgver = "4.2.0"
pkgrel = 5
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qicon_p.h
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt implementation of freedesktop.org xdg specs"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libqtxdg"
source = f"{url}/releases/download/{pkgver}/libqtxdg-{pkgver}.tar.xz"
sha256 = "a5d430218550d66fa806debce7c418db41268286b17bdab46b8ce3a58f0fe82a"


@subpackage("libqtxdg-devel")
def _(self):
    return self.default_devel()

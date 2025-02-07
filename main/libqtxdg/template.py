pkgname = "libqtxdg"
pkgver = "4.1.0"
pkgrel = 2
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
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libqtxdg"
source = f"{url}/releases/download/{pkgver}/libqtxdg-{pkgver}.tar.xz"
sha256 = "0604d397d9561a6a6148930a2b131f2bdee86cec6cca304f7513a8ec7b8e8809"


@subpackage("libqtxdg-devel")
def _(self):
    return self.default_devel()

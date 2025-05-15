pkgname = "kglobalaccel"
pkgver = "6.14.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Global desktop keyboard shortcuts"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kglobalaccel/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kglobalaccel-{pkgver}.tar.xz"
sha256 = "e7aaca16bb4c5b5865af3ed4b48f2347c5163065d17c2b24be97752ff5e8c71d"
hardening = ["vis"]


@subpackage("kglobalaccel-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

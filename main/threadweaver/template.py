pkgname = "threadweaver"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "KDE Multithreading helper library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/threadweaver/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "1ac3fc8051f31ac4f76dfd5d157e5c375d183bc0762152a44e1831cf5816a956"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

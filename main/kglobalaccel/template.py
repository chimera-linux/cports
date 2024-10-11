pkgname = "kglobalaccel"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Global desktop keyboard shortcuts"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kglobalaccel/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kglobalaccel-{pkgver}.tar.xz"
sha256 = "2a35b9e06c6601d602b3a45e278c49e11e4627939cfacffb1fdee0826a6f6e0b"
hardening = ["vis"]


@subpackage("kglobalaccel-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

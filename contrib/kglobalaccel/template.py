pkgname = "kglobalaccel"
pkgver = "6.2.0"
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
sha256 = "c74727fef4a39680e36c5ed27cdb4c5b755043795fa52774ee3bc6a3b568e724"
hardening = ["vis", "cfi"]


@subpackage("kglobalaccel-devel")
def _devel(self):
    return self.default_devel()

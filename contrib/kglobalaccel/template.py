pkgname = "kglobalaccel"
pkgver = "6.3.0"
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
sha256 = "c08206ca39db1227a2a8a3c8c06922d5908830cb6d52ef212cb597b8c7029df1"
hardening = ["vis", "!cfi"]


@subpackage("kglobalaccel-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

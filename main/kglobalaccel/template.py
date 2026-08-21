pkgname = "kglobalaccel"
pkgver = "6.29.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kglobalaccel-{pkgver}.tar.xz"
sha256 = "71f4b08dfa993a1cfaccee004401234ba21754d48955733fc9be13ccc940b444"
hardening = ["vis"]


@subpackage("kglobalaccel-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

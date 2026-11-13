pkgname = "ktexttemplate"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE library for text templates"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "074a1616a41600b358e20c40cab16113906c2394600a4fdc62a22696cc3d4156"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

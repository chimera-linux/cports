pkgname = "ktexttemplate"
pkgver = "6.30.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE library for text templates"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "c3c229944d25294102e4e8a5b49fa0c0f481da9d33f8bec3782e8a53afd47493"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

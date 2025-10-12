pkgname = "ktexttemplate"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE library for text templates"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktexttemplate/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "4087353ac20e376a3dce2ef49bc62f8856eb3b7933707faf62bb31b179c11c83"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

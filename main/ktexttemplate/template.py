pkgname = "ktexttemplate"
pkgver = "6.22.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE library for text templates"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktexttemplate/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "53038e8eedb91e0672bd52bd75b89d196821db3b9d30a0a802f4c964e68f1f7d"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

pkgname = "ktexttemplate"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["qt6-qtdeclarative-devel"]
pkgdesc = "KDE library for text templates"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktexttemplate/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "295a3f87ff08af17f83496fd66b3f634917bcac6466c79be1f4cb6786ecb04c6"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

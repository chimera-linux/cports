pkgname = "ktexttemplate"
pkgver = "6.2.0"
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
sha256 = "a59b0e6e3acb94737b82eafac47d14725255c6c6f21c2371ccf9ecc1062cf2ca"
hardening = ["vis", "!cfi"]


@subpackage("ktexttemplate-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

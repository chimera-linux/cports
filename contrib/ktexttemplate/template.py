pkgname = "ktexttemplate"
pkgver = "6.3.0"
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
sha256 = "9351889c589fb2fa7f33fa6f0d748edbef44863fe79eb49b12d1fa5ab349ae9d"
hardening = ["vis", "!cfi"]


@subpackage("ktexttemplate-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

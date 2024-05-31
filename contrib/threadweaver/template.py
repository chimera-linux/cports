pkgname = "threadweaver"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "KDE Multithreading helper library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/threadweaver/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "e74de2df0bb50148acc8a6161f9809991ae4b2334b58a9ee092ba1d827044337"
# CFI: fails most tests
hardening = ["vis", "!cfi"]


@subpackage("threadweaver-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

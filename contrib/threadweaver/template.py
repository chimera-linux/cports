pkgname = "threadweaver"
pkgver = "6.3.0"
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
sha256 = "81201f8f9918d6967b76a5c8c468481289e5bf56351b3e140cce532821f7d913"
# CFI: fails most tests
hardening = ["vis", "!cfi"]


@subpackage("threadweaver-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

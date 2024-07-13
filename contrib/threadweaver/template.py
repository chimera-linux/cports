pkgname = "threadweaver"
pkgver = "6.4.0"
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
sha256 = "a317ad5b4e0ae8dee7fd95026a3df3f5fc1c2e53aec6d5ccbadddfc753c29598"
# CFI: fails most tests
hardening = ["vis", "!cfi"]


@subpackage("threadweaver-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

pkgname = "threadweaver"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "KDE Multithreading helper library"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "4a65944dcca12672ace6d54a48b3a993d4b46b6095106316c3a95ecae6af9906"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

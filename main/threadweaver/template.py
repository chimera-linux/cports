pkgname = "threadweaver"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "KDE Multithreading helper library"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/threadweaver/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "1ae0e593182c25ec8a9ee85777ab767b6c37b0f7e7a6851d4b6d49bfe03da1d0"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

pkgname = "threadweaver"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "KDE Multithreading helper library"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "b3ee9e6cdfdb3dec7c7df8e7f66ace6a94e73a531ba4f1d8f7b74360e7201e05"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

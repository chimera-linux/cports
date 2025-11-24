pkgname = "threadweaver"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "KDE Multithreading helper library"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/threadweaver/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "9313f25a2ea6e2431d34e0b00f68dad6881849c34f1e40515a539a70dd6fbb19"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

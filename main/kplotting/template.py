pkgname = "kplotting"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE plotting library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kplotting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kplotting-{pkgver}.tar.xz"
sha256 = "c9fdb99fd1c75f588e2f15ef84333feadf327a878c24324e44493d03e593ebc9"


@subpackage("kplotting-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

pkgname = "kplotting"
pkgver = "6.10.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kplotting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kplotting-{pkgver}.tar.xz"
sha256 = "6941d93019bfb1e9977cfa592ba110fbf9c3b7f247af40f336e040071f922d3f"


@subpackage("kplotting-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

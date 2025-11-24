pkgname = "kplotting"
pkgver = "6.20.0"
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
sha256 = "50cd8986acf47e9a8c0df2b11f068a79d241a13f6e426771703a9e188e6aa43f"


@subpackage("kplotting-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

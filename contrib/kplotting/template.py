pkgname = "kplotting"
pkgver = "6.4.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kplotting-{pkgver}.tar.xz"
sha256 = "4f9c770c814748f97a1d14e0ec9c452f2e406574fb51a85e71824ee81a71fc77"


@subpackage("kplotting-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])

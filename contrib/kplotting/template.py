pkgname = "kplotting"
pkgver = "6.3.0"
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
sha256 = "f8e7fa347d0e6bab924f3347716eb5cc468b96b296b52974d392df030dba9521"


@subpackage("kplotting-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])

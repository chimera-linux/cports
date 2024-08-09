pkgname = "kcalendarcore"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libical-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = [
    "perl",
    "xwayland-run",
]
pkgdesc = "KDE calendar access library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcalendarcore/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "6da599f5ed15f6ce54c2f928026ee2f64edd2fe0d5203b4f50bbf89a8b21f522"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _devel(self):
    return self.default_devel()

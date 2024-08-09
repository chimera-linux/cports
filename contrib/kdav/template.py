pkgname = "kdav"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE DAV library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdav/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "900fbb8b632d946cd35e826e64f50507346151f1b5fb40137890abc2896eefcf"


@subpackage("kdav-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()

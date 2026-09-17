pkgname = "kcalendarcore"
pkgver = "6.30.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = ["libical-devel", "qt6-qtdeclarative-devel", "qt6-qttools-devel"]
checkdepends = ["perl", "xwayland-run"]
pkgdesc = "KDE calendar access library"
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "e8bf60e398e2f8098a4db7db44c5475d70540ad8f8948a123c8bc109dc4db776"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()

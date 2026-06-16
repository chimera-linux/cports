pkgname = "kcalendarcore"
pkgver = "6.27.0"
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
url = "https://api.kde.org/frameworks/kcalendarcore/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "4228869722c5bb5325b7c5b10555e6b747bde0e36cbd43519d8681fe3b383173"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()

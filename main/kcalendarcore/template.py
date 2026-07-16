pkgname = "kcalendarcore"
pkgver = "6.28.0"
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
sha256 = "c0c8272729cc9cc7006f87b64f80feb03750acb6bbd208ae94c2bad77fc444be"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()

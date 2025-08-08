pkgname = "kuserfeedback"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
# fails without gl
make_check_args = ["-E", "openglinfosourcetest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE user feedback integration"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kuserfeedback/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "0f1b5361ffa6fff12ec3dfd7a3e4b1b2aa6ebadc4afcc03a9d31c2d49bec7caf"
hardening = ["vis"]


@subpackage("kuserfeedback-devel")
def _(self):
    return self.default_devel()

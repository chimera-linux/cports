pkgname = "kuserfeedback"
pkgver = "6.9.0"
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
    "qt6-qtcharts-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE user feedback integration"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kuserfeedback/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "d12bec0c0396f589423a77a8a8e3c8e7fdc8e9cb88ec6eb35ad978a3127ae5e8"
hardening = ["vis"]


@subpackage("kuserfeedback-devel")
def _(self):
    return self.default_devel()

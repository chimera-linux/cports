pkgname = "libkdepim"
pkgver = "25.12.2"
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
    "kcompletion-devel",
    "ki18n-devel",
    "kldap-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM common library"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libkdepim/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdepim-{pkgver}.tar.xz"
sha256 = "7ae5f42570914f217e2e073a865b8395dd88818fce8e0e6cd01b75b71454db8f"


@subpackage("libkdepim-devel")
def _(self):
    return self.default_devel()

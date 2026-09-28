pkgname = "libkdepim"
pkgver = "26.08.1"
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
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdepim-{pkgver}.tar.xz"
sha256 = "f4de990ab9a8e38b9f73870c1f9523d51c69ede75b8ccf2d62e51be48a861682"


@subpackage("libkdepim-devel")
def _(self):
    return self.default_devel()

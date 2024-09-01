pkgname = "libkdepim"
pkgver = "24.08.0"
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
    "kldap-devel",
    "kcompletion-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM common library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libkdepim/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdepim-{pkgver}.tar.xz"
sha256 = "36b77351b98bdd12cb2a703eb3f4c87b56a47f81bce12418c4d67412465ecbca"


@subpackage("libkdepim-devel")
def _(self):
    return self.default_devel()

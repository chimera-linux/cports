pkgname = "libkdepim"
pkgver = "24.12.2"
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
sha256 = "fe2986ab9a4ccf2af56d6b91a27e391202c4629877b94caa0c8d8efe0a16af74"


@subpackage("libkdepim-devel")
def _(self):
    return self.default_devel()

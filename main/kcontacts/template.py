pkgname = "kcontacts"
pkgver = "6.14.0"
pkgrel = 0
build_style = "cmake"
# germania/germany difference
make_check_args = ["-E", "kcontacts-addresstest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE address book API"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcontacts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcontacts-{pkgver}.tar.xz"
sha256 = "64fd6f2692dc5bea9bc720f52bfdb2880771d82db27e1c9c0f61ac846e503729"
hardening = ["vis"]


@subpackage("kcontacts-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
        "ki18n-devel",
    ]

    return self.default_devel()

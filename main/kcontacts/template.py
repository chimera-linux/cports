pkgname = "kcontacts"
pkgver = "6.16.0"
pkgrel = 0
build_style = "cmake"
# germania/germany difference
make_check_args = ["-E", "kcontacts-addresstest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE address book API"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcontacts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcontacts-{pkgver}.tar.xz"
sha256 = "ff57a9ab119b95895335d427481009cff72ae9cf6d0fc2fa9a504f96cfac6a5e"
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

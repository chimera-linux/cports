pkgname = "kcontacts"
pkgver = "6.31.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcontacts-{pkgver}.tar.xz"
sha256 = "987bc7a1cb0d642ed2ef30a639621535ab18e825e45d526e18f1ca1e29a666d4"
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

pkgname = "kcontacts"
pkgver = "6.3.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcontacts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcontacts-{pkgver}.tar.xz"
sha256 = "229b5b1797cdc7faeb227f715c86edee8e8464f40b247432af909e3b3d30b107"
hardening = ["vis", "!cfi"]


@subpackage("kcontacts-devel")
def _devel(self):
    self.depends += [
        "kcodecs-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
        "ki18n-devel",
    ]

    return self.default_devel()

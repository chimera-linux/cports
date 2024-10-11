pkgname = "kcontacts"
pkgver = "6.7.0"
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
sha256 = "292f8104f9f31d62c59289a3a821766d1ec540f4fc513ffc3b6f7197602d42c5"
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

pkgname = "kidentitymanagement"
pkgver = "25.04.0"
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
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kpimtextedit-devel",
    "ktextaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE library for managing user identities"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/kidentitymanagement/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kidentitymanagement-{pkgver}.tar.xz"
sha256 = "e6bd02635cf475fdf3dfea40bc0f5ce1109cc3bc31d64e0d5844177510688b09"


@subpackage("kidentitymanagement-devel")
def _(self):
    self.depends += [
        "kcoreaddons-devel",
        "kpimtextedit-devel",
    ]
    return self.default_devel()

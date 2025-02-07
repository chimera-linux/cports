pkgname = "kidentitymanagement"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/kidentitymanagement/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kidentitymanagement-{pkgver}.tar.xz"
sha256 = "b6a10f2c650db4ba99c5a2a786fb4213701250126aa853dc909c81cf37c0f21e"


@subpackage("kidentitymanagement-devel")
def _(self):
    self.depends += [
        "kcoreaddons-devel",
        "kpimtextedit-devel",
    ]
    return self.default_devel()

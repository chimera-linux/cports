pkgname = "kidentitymanagement"
pkgver = "24.05.0"
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
sha256 = "78dcecb9f938ccaccff2572b951bf03321ce6b29a05aa9d97120f1c0df3b0212"


@subpackage("kidentitymanagement-devel")
def _devel(self):
    self.depends += [
        "kcoreaddons-devel",
        "kpimtextedit-devel",
    ]
    return self.default_devel()

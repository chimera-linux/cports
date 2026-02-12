pkgname = "kidentitymanagement"
pkgver = "25.12.2"
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
sha256 = "305cd01a360ce60386cae5c00d64368aaf3159a4fda54856df072c2d6c03cdb0"


@subpackage("kidentitymanagement-devel")
def _(self):
    self.depends += [
        "kcoreaddons-devel",
        "kpimtextedit-devel",
    ]
    return self.default_devel()

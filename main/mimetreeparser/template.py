pkgname = "mimetreeparser"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgme-devel",
    "kcalendarcore-devel",
    "kcodecs-devel",
    "kcolorscheme-devel",
    "ki18n-devel",
    "kmbox-devel",
    "kmime-devel",
    "kwidgetsaddons-devel",
    "libkleo-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE parser for MIME trees"
license = "LGPL-3.0-only AND GPL-3.0-only"
url = "https://invent.kde.org/pim/mimetreeparser"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/mimetreeparser-{pkgver}.tar.xz"
)
sha256 = "63662367842e25b8e13c7523d0542847a1cffb36c72072bfe3b2942eccdd7841"


@subpackage("mimetreeparser-devel")
def _(self):
    self.depends += [
        "ki18n-devel",
        "ki18n-devel",
        "kmbox-devel",
        "kmime-devel",
        "mailimporter-devel",
    ]
    return self.default_devel()

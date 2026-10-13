pkgname = "mimetreeparser"
pkgver = "26.08.2"
pkgrel = 0
build_style = "cmake"
# unable to detect a launcher
make_check_args = ["-j1", "-E", "core-attachmentmodeltest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgmepp-devel",
    "kcalendarcore-devel",
    "kcodecs-devel",
    "kcolorscheme-devel",
    "ki18n-devel",
    "kio-devel",
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
sha256 = "82b4e37cb59b7264ef13b6e8c18be7d59666f4cbfb51b5ae0f1d7ab6ea35cd09"


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

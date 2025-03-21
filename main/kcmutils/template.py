pkgname = "kcmutils"
pkgver = "6.12.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Utilities for KDE System Settings modules"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcmutils/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "7aacd2f06f0f393631fc058188b92ad55929871e93aa2ea3de2a9d0b35a36ac7"
hardening = ["vis"]


@subpackage("kcmutils-devel")
def _(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()

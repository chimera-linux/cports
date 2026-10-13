pkgname = "kcmutils"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Utilities for KDE System Settings modules"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "e7c96296f2cc31b68c323559890df1e197dcb9c663822682dc97737c1b811610"
hardening = ["vis"]


@subpackage("kcmutils-devel")
def _(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()

pkgname = "kcmutils"
pkgver = "6.4.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcmutils/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "59b1293ffe67134ceba30fb7ce741889c54f85ad0c90d155688bdd0dfc8f31be"
hardening = ["vis"]


@subpackage("kcmutils-devel")
def _devel(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()

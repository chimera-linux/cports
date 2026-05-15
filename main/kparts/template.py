pkgname = "kparts"
pkgver = "6.26.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Plugin framework for UI components"
license = (
    "LGPL-2.1-only AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
)
url = "https://api.kde.org/frameworks/kparts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kparts-{pkgver}.tar.xz"
sha256 = "049c2cf048b4cbbffe0bea9357bd9ab53b8be672ba509b2bb058f764d21b3f5b"
hardening = ["vis"]


@subpackage("kparts-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "kservice-devel",
        "kxmlgui-devel",
    ]

    return self.default_devel()

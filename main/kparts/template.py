pkgname = "kparts"
pkgver = "6.17.0"
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
sha256 = "1e64d426ce47501a8ff1bac8c2366f0cd153e6cd4d440e827eb0015d9e38c3e9"
hardening = ["vis"]


@subpackage("kparts-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "kservice-devel",
        "kxmlgui-devel",
    ]

    return self.default_devel()

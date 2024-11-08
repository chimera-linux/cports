pkgname = "kparts"
pkgver = "6.8.0"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Plugin framework for UI components"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
)
url = "https://api.kde.org/frameworks/kparts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kparts-{pkgver}.tar.xz"
sha256 = "0a21d2abf4c4406015f7d5abebefec0493575847ea4ec34ea23d53db5255b327"
hardening = ["vis"]


@subpackage("kparts-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "kservice-devel",
        "kxmlgui-devel",
    ]

    return self.default_devel()

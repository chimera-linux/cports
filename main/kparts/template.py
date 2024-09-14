pkgname = "kparts"
pkgver = "6.6.0"
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
sha256 = "d494def76a3a4c2e28bc9d4f889d6d4d9b644515fffb61169f429ce7b9bb22c7"
hardening = ["vis"]


@subpackage("kparts-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "kservice-devel",
        "kxmlgui-devel",
    ]

    return self.default_devel()

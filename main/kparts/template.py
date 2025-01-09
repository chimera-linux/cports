pkgname = "kparts"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kparts-{pkgver}.tar.xz"
sha256 = "afc9c4e897b371a51589342ed0573889bf4fab79b81b9a6950a45cd9faedd788"
hardening = ["vis"]


@subpackage("kparts-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "kservice-devel",
        "kxmlgui-devel",
    ]

    return self.default_devel()

pkgname = "oxygen"
pkgver = "6.2.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "frameworkintegration-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    self.with_pkgver("oxygen-cursors"),
    "oxygen-icons",
    "frameworkintegration",
]
pkgdesc = "Oxygen visual style for the KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"  # FIXME
url = "https://invent.kde.org/plasma/oxygen"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-{pkgver}.tar.xz"
sha256 = "a8838f2363ab8fc2ff6e8d5735c1f034a6965c31f1515a164e1424cbb58aa7b8"
hardening = ["vis"]


@subpackage("oxygen-cursors")
def _(self):
    self.subdesc = "cursor themes"
    return [
        "usr/share/icons/Oxygen*",
        "usr/share/icons/KDE_Classic",
    ]

pkgname = "oxygen"
pkgver = "6.4.1"
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
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
]
depends = [
    self.with_pkgver("oxygen-cursors"),
    "oxygen-icons",
    "frameworkintegration",
]
pkgdesc = "Oxygen visual style for the KDE Plasma Desktop"
license = "GPL-2.0-or-later"  # FIXME
url = "https://invent.kde.org/plasma/oxygen"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-{pkgver}.tar.xz"
sha256 = "6f9b223791f1511e6feec4b68ba6034e1245e03ea21d131fe18c4a84975546a5"
hardening = ["vis"]


@subpackage("oxygen-cursors")
def _(self):
    self.subdesc = "cursor themes"
    return [
        "usr/share/icons/Oxygen*",
        "usr/share/icons/KDE_Classic",
    ]

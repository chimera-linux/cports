pkgname = "oxygen"
pkgver = "6.4.4"
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
    "frameworkintegration",
    "oxygen-icons",
    self.with_pkgver("oxygen-cursors"),
]
pkgdesc = "Oxygen visual style for the KDE Plasma Desktop"
license = "GPL-2.0-or-later"  # FIXME
url = "https://invent.kde.org/plasma/oxygen"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-{pkgver}.tar.xz"
sha256 = "7f045afa9d321e86fcda814037bbf991fe4cffe34b3cd48c70678db7406f28fb"
hardening = ["vis"]


@subpackage("oxygen-cursors")
def _(self):
    self.subdesc = "cursor themes"
    return [
        "usr/share/icons/Oxygen*",
        "usr/share/icons/KDE_Classic",
    ]

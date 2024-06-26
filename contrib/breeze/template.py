pkgname = "breeze"
pkgver = "6.1.1"
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
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    f"breeze-cursors={pkgver}-r{pkgrel}",
    "breeze-icons",
    "frameworkintegration",
]
pkgdesc = "Breeze visual style for the KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/breeze"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-{pkgver}.tar.xz"
sha256 = "8943ff74c4cb16b1b3c03eea0cca39821d444bea60dc163ff18e2bd313609725"
# FIXME: cfi kills plasma-apply-lookandfeel in breeze6.so
hardening = ["vis", "!cfi"]
# TODO: split qt6 theme?


@subpackage("breeze-cursors")
def _cursors(self):
    self.pkgdesc = f"{pkgdesc} (cursor themes)"
    return [
        "usr/share/icons/breeze_cursors",
        "usr/share/icons/Breeze_Light",
    ]


@subpackage("breeze-devel")
def _devel(self):
    return self.default_devel()

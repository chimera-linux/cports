pkgname = "breeze"
pkgver = "6.1.0"
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
sha256 = "f71b8f4e7677e5685676ac72f961015853de959b1e08ba73539147cec7bd1d0e"
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

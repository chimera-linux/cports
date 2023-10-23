pkgname = "breeze"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
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
# depends = ["breeze-icons", "frameworkintegration"] # "breeze-snow-cursor-theme"
pkgdesc = "Breeze visual style for the KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/breeze"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-{pkgver}.tar.xz"
sha256 = "f249dd4464f4da6b681af5c4fd0e81178127294b2d441134f3b10e2703f57374"
# FIXME: cfi kills plasma-apply-lookandfeel in breeze6.so
hardening = ["vis", "!cfi"]


# TODO: any subpackaging for cursors etc?


@subpackage("breeze-devel")
def _devel(self):
    return self.default_devel()

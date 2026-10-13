pkgname = "dolphin-plugins"
pkgver = "26.08.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dolphin-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
pkgdesc = "Plugins for the KDE Dolphin file manager"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/dolphin_plugins"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/dolphin-plugins-{pkgver}.tar.xz"
)
sha256 = "e9a921523cb17df79db27c81d6c31d08be1f78bd937dc9394d9aafd2ca3a1143"
hardening = ["vis"]

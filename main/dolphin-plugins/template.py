pkgname = "dolphin-plugins"
pkgver = "25.12.2"
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
sha256 = "3ac44ee9ad6495b2e56612ccd2a1940b05584685ed33cba490c484f5e5f9a6a6"
hardening = ["vis"]

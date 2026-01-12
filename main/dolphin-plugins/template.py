pkgname = "dolphin-plugins"
pkgver = "25.12.1"
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
sha256 = "c36d7756afdd3286bf61f4184122203c20eda3bcefc4b203b27b05395c459ce7"
hardening = ["vis"]

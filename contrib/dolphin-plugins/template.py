pkgname = "dolphin-plugins"
pkgver = "24.05.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/dolphin_plugins"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/dolphin-plugins-{pkgver}.tar.xz"
)
sha256 = "715329f75eb22d6f59baabc5defa1aa37c73ea16d62141c0eae695325c01ac2e"
# CFI: check
hardening = ["vis", "!cfi"]

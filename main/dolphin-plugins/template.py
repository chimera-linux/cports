pkgname = "dolphin-plugins"
pkgver = "26.08.1"
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
sha256 = "f9edc41bb0fc75dba1ac32a8c15ef33fb8152740f10b90265dbc6f1724eb929b"
hardening = ["vis"]

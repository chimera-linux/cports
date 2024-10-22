pkgname = "plasma5support"
pkgver = "6.2.2"
pkgrel = 0
build_style = "cmake"
# needs plasma-workspace plugin and is circular with it
make_check_args = ["-E", "pluginloadertest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "kservice-devel",
    "libksysguard-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
# some qt5 compat modules were moved here ~6.1.0
# also locale file conflicts ~6.2.2
replaces = ["plasma-workspace<6.2.2"]
pkgdesc = "KDE Support components for porting from Qt5/KF5 to Qt6/KF6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma5support"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma5support-{pkgver}.tar.xz"
sha256 = "8e26657768b5533bb1c7aeccd51658b47a61a66750438bf4b25ab96d63a8c730"
hardening = ["vis"]


@subpackage("plasma5support-devel")
def _(self):
    self.depends += ["kcoreaddons-devel", "kservice-devel"]

    return self.default_devel()

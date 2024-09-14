pkgname = "plasma5support"
pkgver = "6.1.5"
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
    "knotifications-devel",
    "libksysguard-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
# some qt5 compat modules were moved here
replaces = ["plasma-workspace<6.1.5"]
pkgdesc = "KDE Support components for porting from Qt5/KF5 to Qt6/KF6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma5support"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma5support-{pkgver}.tar.xz"
sha256 = "0563585222c5333e2279efda829c36a139741c9e0cf3ad36e3e8096840c017d1"
hardening = ["vis"]


@subpackage("plasma5support-devel")
def _(self):
    self.depends += ["kcoreaddons-devel", "kservice-devel"]

    return self.default_devel()

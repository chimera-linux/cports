pkgname = "plasma5support"
pkgver = "6.1.2"
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
replaces = ["plasma-workspace<6.1.2"]
pkgdesc = "KDE Support components for porting from Qt5/KF5 to Qt6/KF6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma5support"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma5support-{pkgver}.tar.xz"
sha256 = "f2cf732fef4d1f03df87eef5aa556c0de4630fdff50cd64d59effdec23689c9d"
hardening = ["vis", "cfi"]


@subpackage("plasma5support-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel", "kservice-devel"]

    return self.default_devel()

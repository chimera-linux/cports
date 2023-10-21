pkgname = "plasma5support"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Support components for porting from Qt5/KF5 to Qt6/KF6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma5support"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma5support-{pkgver}.tar.xz"
sha256 = "8a811e7dba1c30ae2628934c4da91d2dfa42dc932286e97dac8970646287b87a"
hardening = ["vis", "cfi"]


@subpackage("plasma5support-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel", "kservice-devel"]

    return self.default_devel()

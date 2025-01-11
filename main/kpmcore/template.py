pkgname = "kpmcore"
pkgver = "24.12.1"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "fdisk",
    "smartmontools",
]
pkgdesc = "KDE library for partition management"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpmcore-{pkgver}.tar.xz"
sha256 = "8e13b75bfd2e86e3897cb338509440bbc2f03dd4a6de8a0118b95de19bc0e3a2"
hardening = ["vis"]


@subpackage("kpmcore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

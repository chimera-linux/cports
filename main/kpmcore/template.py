pkgname = "kpmcore"
pkgver = "25.08.2"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
depends = ["smartmontools", "util-linux-fdisk"]
pkgdesc = "KDE library for partition management"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpmcore-{pkgver}.tar.xz"
sha256 = "39024369e01001119a5feca5c230f7f72ea4b625f4f2767c48f6e33c07a95555"
hardening = ["vis"]


@subpackage("kpmcore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

pkgname = "kpmcore"
pkgver = "24.08.2"
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
sha256 = "81d30f3322acb2eb8751e980af6c8b13fc3994683f4f902e588226b70a456795"
hardening = ["vis"]


@subpackage("kpmcore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()

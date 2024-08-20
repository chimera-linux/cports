pkgname = "polkit-qt-1"
pkgver = "0.200.0"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "polkit-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Qt wrapper around polkit-1 client libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/polkit-qt-1"
source = f"$(KDE_SITE)/polkit-qt-1/polkit-qt-1-{pkgver}.tar.xz"
sha256 = "5d3b611c062d2b76a93750bb10c907bfd21d1ff08d0a15dc2cf63e278e1677fb"
hardening = ["vis"]


@subpackage("polkit-qt-1-devel")
def _(self):
    return self.default_devel()

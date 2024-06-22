pkgname = "libktorrent"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "gmp-devel",
    "karchive-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kio-devel",
    "libgcrypt-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "solid-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE torrent library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/libktorrent"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libktorrent-{pkgver}.tar.xz"
sha256 = "6bfff0f4f1b269d82dfe28bb29e0d81322e131d3ad29423207a8957db73249e5"


@subpackage("libktorrent-devel")
def _devel(self):
    self.depends += [
        "boost-devel",
        "gmp-devel",
        "karchive-devel",
        "kconfig-devel",
        "kio-devel",
        "libgcrypt-devel",
        "qt6-qt5compat-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

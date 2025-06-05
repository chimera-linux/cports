pkgname = "libktorrent"
pkgver = "25.04.2"
pkgrel = 0
build_style = "cmake"
# flakes sometimes
make_check_args = ["-E", "superseedtest"]
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
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/libktorrent"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libktorrent-{pkgver}.tar.xz"
sha256 = "e6ccf6d0503a0b71d594b75e67aa0ad505d57316d20d5380ccc590c4f0604e98"


@subpackage("libktorrent-devel")
def _(self):
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

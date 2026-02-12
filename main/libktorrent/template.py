pkgname = "libktorrent"
pkgver = "25.12.2"
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
sha256 = "31ade6b88d30bbdf7062d76dcec1ea41fb2887de9a93f0175248199e13329c37"


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

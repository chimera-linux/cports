pkgname = "libktorrent"
pkgver = "24.08.3"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/libktorrent"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libktorrent-{pkgver}.tar.xz"
sha256 = "58243287e78a86a212af400cc3cfc4ded1a0837a2ebbf6898eeb67b5bb02d4fc"


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

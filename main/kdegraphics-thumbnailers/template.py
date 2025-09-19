pkgname = "kdegraphics-thumbnailers"
pkgver = "25.08.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kdegraphics-mobipocket-devel",
    "kio-devel",
    "libkdcraw-devel",
    "libkexiv2-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE thumbnailers for PostScript/RAW/MobiPocket/Blender"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdegraphics_thumbnailers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-thumbnailers-{pkgver}.tar.xz"
sha256 = "0c048e4dc190a30aa2b4c6316b186d9462418adad22a6e3535b40d4085b6649d"

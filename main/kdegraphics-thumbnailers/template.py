pkgname = "kdegraphics-thumbnailers"
pkgver = "26.04.3"
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
sha256 = "bd44c4c13e22dc69366e76d05b3d65629d07507a38e5ba42d60267756d73edcf"

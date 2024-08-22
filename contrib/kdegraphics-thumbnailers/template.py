pkgname = "kdegraphics-thumbnailers"
pkgver = "24.08.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdegraphics_thumbnailers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-thumbnailers-{pkgver}.tar.xz"
sha256 = "0e8326861dc9d8afc3780ef2b4848e9bb2a8194f2144b95928e5bc39989d70b2"

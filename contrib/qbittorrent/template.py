pkgname = "qbittorrent"
pkgver = "4.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT6=ON",
    "-DSTACKTRACE=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "boost-devel",
    "libtorrent-rasterbar-devel",
    "openssl-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "qt6-qtsvg-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "QT-based torrent client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.qbittorrent.org"
source = f"https://github.com/qbittorrent/qBittorrent/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "f1cb8a677d2c882d3aa7f6fdebd9671950d7d6578480ace7529b498b13480804"
# FIXME: BitTorrent::SessionImpl::SessionImpl cfi crash
hardening = ["vis"]
# don't build
options = ["!check"]

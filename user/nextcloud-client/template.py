pkgname = "nextcloud-client"
pkgver = "3.15.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "inkscape",
    "ninja",
    "openssl-devel",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "karchive-devel",
    "kguiaddons-devel",
    "kio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebengine-devel",
    "qt6-qtwebsockets-devel",
    "qtkeychain-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Desktop sync client for Nextcloud"
maintainer = "doskel <doskel@doskel.net>"
license = "GPL-2.0-only"
url = "https://github.com/nextcloud/desktop"
source = f"{url}/archive/refs/tags/v{pkgver.replace('_', '-')}.tar.gz"
sha256 = "25eb5248049c4961a27cf996dbebf9202c720dd36049cd2799e2e80f7bd51756"

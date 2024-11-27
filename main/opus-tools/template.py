pkgname = "opus-tools"
pkgver = "0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
]
makedepends = [
    "flac-devel",
    "libogg-devel",
    "libopusenc-devel",
    "linux-headers",
    "opus-devel",
    "opusfile-devel",
]
pkgdesc = "Collection of tools for the Opus audio codec"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause AND GPL-2.0-only"
url = "https://wiki.xiph.org/Opus-tools"
source = f"https://downloads.xiph.org/releases/opus/opus-tools-{pkgver}.tar.gz"
sha256 = "b4e56cb00d3e509acfba9a9b627ffd8273b876b4e2408642259f6da28fa0ff86"


def post_install(self):
    self.install_license("COPYING")

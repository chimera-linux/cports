pkgname = "libbluray-bdj"
pkgver = "1.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-optimizations"]
configure_gen = []
hostmakedepends = [
    "apache-ant",
    "openjdk17-default",
    "openjdk17-jdk",
    "pkgconf",
]
makedepends = ["libxml2-devel", "fontconfig-devel"]
pkgdesc = "Library for Blu-Ray disk playback (BD-J support)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.videolan.org/developers/libbluray.html"
source = f"https://download.videolan.org/pub/videolan/libbluray/{pkgver}/libbluray-{pkgver}.tar.bz2"
sha256 = "478ffd68a0f5dde8ef6ca989b7f035b5a0a22c599142e5cd3ff7b03bbebe5f2b"


def post_install(self):
    # make it not conflict
    self.uninstall("usr/bin")
    self.uninstall("usr/include")
    self.uninstall("usr/lib")

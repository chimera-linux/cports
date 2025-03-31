pkgname = "libbluray"
pkgver = "1.3.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-optimizations", "--disable-bdjava-jar"]
# slibtool breaks dlfcn.h check
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libxml2-devel", "fontconfig-devel"]
pkgdesc = "Library for Blu-Ray disk playback"
license = "LGPL-2.1-or-later"
url = "https://www.videolan.org/developers/libbluray.html"
source = f"https://download.videolan.org/pub/videolan/libbluray/{pkgver}/libbluray-{pkgver}.tar.bz2"
sha256 = "478ffd68a0f5dde8ef6ca989b7f035b5a0a22c599142e5cd3ff7b03bbebe5f2b"


@subpackage("libbluray-devel")
def _(self):
    return self.default_devel()


@subpackage("libbluray-progs")
def _(self):
    return self.default_progs()

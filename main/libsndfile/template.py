pkgname = "libsndfile"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "python"]
# FIXME: mpg123 is cyclic (pipewire->sbc->sndfile)
makedepends = [
    "libvorbis-devel", "flac-devel", "opus-devel", "sqlite-devel",
    "lame-devel", "linux-headers",
]
pkgdesc = "C library for reading and writing files containing sampled sound"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libsndfile.github.io/libsndfile"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0f98e101c0f7c850a71225fb5feaf33b106227b3d331333ddc9bacee190bcf41"

@subpackage("libsndfile-progs")
def _progs(self):
    return self.default_progs()

@subpackage("libsndfile-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/doc"])

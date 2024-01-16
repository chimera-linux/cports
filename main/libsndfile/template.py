pkgname = "libsndfile"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "python"]
# FIXME: mpg123 is cyclic (pipewire->sbc->sndfile)
makedepends = [
    "libvorbis-devel",
    "flac-devel",
    "opus-devel",
    "sqlite-devel",
    "lame-devel",
    "linux-headers",
]
pkgdesc = "C library for reading and writing files containing sampled sound"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libsndfile.github.io/libsndfile"
source = f"https://github.com/libsndfile/libsndfile/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3799ca9924d3125038880367bf1468e53a1b7e3686a934f098b7e1d286cdb80e"


@subpackage("libsndfile-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libsndfile-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []

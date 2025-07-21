pkgname = "libsndfile"
pkgver = "1.2.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "python", "slibtool"]
# FIXME: mpg123 is cyclic (pipewire->sbc->sndfile)
makedepends = [
    "flac-devel",
    "lame-devel",
    "libvorbis-devel",
    "linux-headers",
    "opus-devel",
    "sqlite-devel",
]
pkgdesc = "C library for reading and writing files containing sampled sound"
license = "LGPL-2.1-or-later"
url = "https://libsndfile.github.io/libsndfile"
source = f"https://github.com/libsndfile/libsndfile/releases/download/{pkgver}/libsndfile-{pkgver}.tar.xz"
sha256 = "3799ca9924d3125038880367bf1468e53a1b7e3686a934f098b7e1d286cdb80e"


@subpackage("libsndfile-progs")
def _(self):
    return self.default_progs()


@subpackage("libsndfile-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])

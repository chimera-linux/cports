pkgname = "libsndfile"
pkgver = "1.0.31"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "python"]
makedepends = [
    "libvorbis-devel", "flac-devel", "opus-devel", "sqlite-devel",
    "linux-headers",
]
pkgdesc = "C library for reading and writing files containing sampled sound"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libsndfile.github.io/libsndfile"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a8cfb1c09ea6e90eff4ca87322d4168cdbe5035cb48717b40bf77e751cc02163"

@subpackage("libsndfile-progs")
def _progs(self):
    return self.default_progs()

@subpackage("libsndfile-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/doc"])

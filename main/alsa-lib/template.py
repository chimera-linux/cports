pkgname = "alsa-lib"
pkgver = "1.2.6.1"
pkgrel = 0
build_style = "gnu_configure"
# build a stripped down alsa lib; things should never use it directly other
# than soundservers, and this should be just enough functionality for them
configure_args = [
    "--disable-rawmidi",
    "--disable-hwdep",
    "--disable-topology",
    "--disable-alisp",
    "--disable-old-symbols",
    "--disable-python",
    "--with-versioned=no",
    "--with-pcm-plugins=extplug ioplug",
]
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Advanced Linux Sound Architecture library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ad582993d52cdb5fb159a0beab60a6ac57eab0cc1bdf85dc4db6d6197f02333f"
# tests require stuff we disable
options = ["!check"]

def post_install(self):
    # disabled
    self.rm(self.destdir / "usr/lib/pkgconfig/alsa-topology.pc")

@subpackage("alsa-lib-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()

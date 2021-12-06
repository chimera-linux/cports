pkgname = "alsa-lib"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
# build a stripped down alsa lib; things should never use it directly other
# than soundservers, and this should be just enough functionality for them
configure_args = [
    "--disable-mixer",
    "--disable-rawmidi",
    "--disable-hwdep",
    "--disable-ucm",
    "--disable-topology",
    "--disable-alisp",
    "--disable-old-symbols",
    "--disable-python",
    "--with-versioned=no",
    "--with-pcm-plugins=",
]
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Advanced Linux Sound Architecture library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7fe3057894ec319118abfd042ef84632a1dcd911806ec9fff6daaa68d15a8c52"
# tests require stuff we disable
options = ["!check"]

def post_install(self):
    # disabled
    self.rm(self.destdir / "usr/lib/pkgconfig/alsa-topology.pc")

@subpackage("alsa-lib-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()

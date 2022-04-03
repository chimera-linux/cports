pkgname = "openal-soft"
pkgver = "1.21.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "zlib-devel", "libpulse-devel", "pipewire-jack-devel", "sdl-devel",
    "ffmpeg-devel",
]
pkgdesc = "Cross-platform 3D audio API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
source = f"{url}/openal-releases/{pkgname}-{pkgver}.tar.bz2"
sha256 = "c8ad767e9a3230df66756a21cc8ebf218a9d47288f2514014832204e666af5d8"
# no test target
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")

@subpackage("openal-soft-devel")
def _devel(self):
    return self.default_devel()

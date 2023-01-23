pkgname = "openal-soft"
pkgver = "1.22.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "zlib-devel", "libpulse-devel", "pipewire-devel", "pipewire-jack-devel",
    "sdl-devel", "ffmpeg-devel",
]
pkgdesc = "Cross-platform 3D audio API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
source = f"{url}/openal-releases/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ae94cc95cda76b7cc6e92e38c2531af82148e76d3d88ce996e2928a1ea7c3d20"
# no test target
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")

@subpackage("openal-soft-devel")
def _devel(self):
    return self.default_devel()

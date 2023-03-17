pkgname = "openal-soft"
pkgver = "1.23.0"
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
sha256 = "057dcf96c3cdfcf40159800a93f57740fe79c2956f76247bee10e436b6657183"
# no test target
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")

@subpackage("openal-soft-devel")
def _devel(self):
    return self.default_devel()

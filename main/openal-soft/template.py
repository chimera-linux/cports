pkgname = "openal-soft"
pkgver = "1.23.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "libpulse-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl-devel",
    "ffmpeg-devel",
]
pkgdesc = "Cross-platform 3D audio API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
source = f"{url}/openal-releases/{pkgname}-{pkgver}.tar.bz2"
sha256 = "796f4b89134c4e57270b7f0d755f0fa3435b90da437b745160a49bd41c845b21"
# no test target
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _devel(self):
    return self.default_devel()

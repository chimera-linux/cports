pkgname = "openal-soft"
pkgver = "1.24.2"
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
source = f"{url}/openal-releases/openal-soft-{pkgver}.tar.bz2"
sha256 = "cd4c88c9b7311cb6785db71c0ed64f5430c9d5b3454e0158314b2ef25ace3e61"
# no test target
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _(self):
    return self.default_devel()

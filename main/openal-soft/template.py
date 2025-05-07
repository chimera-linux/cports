pkgname = "openal-soft"
pkgver = "1.24.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "libpulse-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl3-devel",
    "ffmpeg-devel",
]
pkgdesc = "Cross-platform 3D audio API"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
source = f"{url}/openal-releases/openal-soft-{pkgver}.tar.bz2"
sha256 = "cb5e6197a1c0da0edcf2a81024953cc8fa8545c3b9474e48c852af709d587892"
# no test target
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _(self):
    return self.default_devel()

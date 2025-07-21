pkgname = "openal-soft"
pkgver = "1.24.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "libpulse-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cross-platform 3D audio API"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
# expired certificate
# source = f"{url}/openal-releases/openal-soft-{pkgver}.tar.bz2"
source = f"https://github.com/kcat/openal-soft/archive/{pkgver}.tar.gz"
sha256 = "7e1fecdeb45e7f78722b776c5cf30bd33934b961d7fd2a11e0494e064cc631ce"
# no test target
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _(self):
    return self.default_devel()

pkgname = "rtaudio"
pkgver = "6.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DRTAUDIO_API_ALSA=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pipewire-jack-devel", "libpulse-devel"]
pkgdesc = "Common API for realtime audio input/output"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://www.music.mcgill.ca/~gary/rtaudio"
source = f"https://github.com/thestk/rtaudio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7206c8b6cee43b474f43d64988fefaadfdcfc4264ed38d8de5f5d0e6ddb0a123"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rtaudio-devel")
def _(self):
    return self.default_devel()

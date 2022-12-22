pkgname = "sdl_mixer"
pkgver = "2.6.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # use external libraries, disable bundled crap
    "--enable-music-flac-libflac",
    "--enable-music-mp3-mpg123",
    "--enable-music-ogg-vorbis",
    "--disable-music-flac-drflac",
    "--disable-music-mp3-drmp3",
    "--disable-music-ogg-stb",
    "--disable-music-mod-modplug-shared",
    "--disable-music-midi-fluidsynth-shared",
    "--disable-music-mp3-mpg123-shared",
    "--disable-music-ogg-vorbis-shared",
    "--disable-music-flac-libflac-shared",
    "--disable-music-opus-shared",
    "--disable-music-midi-timidity",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "sdl-devel",
    "flac-devel",
    "libvorbis-devel",
    "opusfile-devel",
    "libmodplug-devel",
    "fluidsynth-devel",
    "smpeg-devel",
    "mpg123-devel",
]
pkgdesc = "SDL audio mixer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_mixer"
source = f"{url}/release/SDL2_mixer-{pkgver}.tar.gz"
sha256 = "8cdea810366decba3c33d32b8071bccd1c309b2499a54946d92b48e6922aa371"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl_mixer-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]

pkgname = "sdl_mixer"
pkgver = "2.6.3"
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
sha256 = "7a6ba86a478648ce617e3a5e9277181bc67f7ce9876605eea6affd4a0d6eea8f"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl_mixer-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

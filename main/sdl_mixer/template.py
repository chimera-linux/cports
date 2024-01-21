pkgname = "sdl_mixer"
pkgver = "2.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # use external libraries, disable bundled crap
    "--enable-music-flac-libflac",
    "--enable-music-mp3-mpg123",
    "--enable-music-ogg-vorbis",
    "--enable-music-wavpack",
    "--disable-music-flac-drflac",
    "--disable-music-flac-libflac-shared",
    "--disable-music-gme",
    "--disable-music-midi-fluidsynth-shared",
    "--disable-music-midi-timidity",
    "--disable-music-mod-modplug-shared",
    "--disable-music-mod-xmp",
    "--disable-music-mp3-minimp3",
    "--disable-music-mp3-mpg123-shared",
    "--disable-music-ogg-stb",
    "--disable-music-ogg-vorbis-shared",
    "--disable-music-opus-shared",
    "--disable-music-wavpack-shared",
]
make_cmd = "gmake"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "flac-devel",
    "fluidsynth-devel",
    "libmodplug-devel",
    "libvorbis-devel",
    "mpg123-devel",
    "opusfile-devel",
    "sdl-devel",
    "smpeg-devel",
    "wavpack-devel",
]
pkgdesc = "SDL audio mixer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_mixer"
source = f"{url}/release/SDL2_mixer-{pkgver}.tar.gz"
sha256 = "1cfb34c87b26dbdbc7afd68c4f545c0116ab5f90bbfecc5aebe2a9cb4bb31549"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl_mixer-devel")
def _devel(self):
    return self.default_devel()

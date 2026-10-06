pkgname = "sdl2_mixer"
pkgver = "2.8.2"
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
hostmakedepends = [
    "autoconf-archive",
    "automake",
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
    "sdl2-compat-devel",
    "smpeg-devel",
    "wavpack-devel",
]
provides = [self.with_pkgver("sdl_mixer")]
pkgdesc = "SDL audio mixer library"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_mixer"
source = f"{url}/release/SDL2_mixer-{pkgver}.tar.gz"
sha256 = "938dff531d00ace2296557a6599abe6f34599e2f34f0a4a08a397e2ccac8b8f7"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2_mixer-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_mixer-devel")]

    return self.default_devel()

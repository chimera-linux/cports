pkgname = "sdl_mixer"
pkgver = "2.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-music-mod-modplug-shared",
    "--disable-music-mod-mikmod-shared",
    "--disable-music-midi-fluidsynth-shared",
    "--disable-music-mp3-mpg123-shared",
    "--disable-music-ogg-shared",
    "--disable-music-flac-shared",
    "--disable-music-opus-shared",
    "--disable-music-midi-fluidsynth", # FIXME
    "--disable-music-midi-timidity",   # FIXME
    "--disable-music-mp3-mpg123",      # FIXME
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "sdl-devel",
    "flac-devel",
    "libvorbis-devel",
    "opusfile-devel",
    "libmikmod-devel",
    "libmodplug-devel",
    #"fluidsynth-devel",
    "smpeg-devel",
    #"mpg123-devel",
]
pkgdesc = "SDL audio mixer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_mixer"
source = f"{url}/release/SDL2_mixer-{pkgver}.tar.gz"
sha256 = "b4cf5a382c061cd75081cf246c2aa2f9df8db04bdda8dcdc6b6cca55bede2419"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("COPYING.txt")

@subpackage("sdl_mixer-devel")
def _devel(self):
    return self.default_devel()

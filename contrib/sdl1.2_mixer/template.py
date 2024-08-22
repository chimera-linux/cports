pkgname = "sdl1.2_mixer"
pkgver = "1.2.12"
pkgrel = 1
build_style = "gnu_configure"
# make sure they're pulled as runtime deps
configure_args = [
    "--disable-music-flac-shared",
    "--disable-music-mod-shared",
    "--disable-music-mp3-shared",
    "--disable-music-ogg-shared",
]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "libmikmod-devel",
    "libvorbis-devel",
    "sdl12-compat-devel",
    "smpeg0-devel",
]
pkgdesc = "SDL 1.2 audio mixer library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://www.libsdl.org/projects/old/SDL_mixer/release-1.2.html"
source = f"https://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-{pkgver}.tar.gz"
sha256 = "1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a"
# no tests
options = ["!check"]


@subpackage("sdl1.2_mixer-devel")
def _(self):
    return self.default_devel()

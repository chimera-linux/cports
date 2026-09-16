pkgname = "sdl3_mixer"
pkgver = "3.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DSDLMIXER_VENDORED=OFF",
    "-DSDLMIXER_TESTS=OFF",
    "-DSDLMIXER_EXAMPLES=OFF",
    "-DSDLMIXER_FLAC_LIBFLAC=ON",
    "-DSDLMIXER_FLAC_DRFLAC=OFF",
    "-DSDLMIXER_FLAC_LIBFLAC_SHARED=OFF",
    "-DSDLMIXER_GME=OFF",
    "-DSDLMIXER_MOD=OFF",
    "-DSDLMIXER_MP3_MPG123=ON",
    "-DSDLMIXER_MP3_DRMP3=OFF",
    "-DSDLMIXER_MP3_MPG123_SHARED=OFF",
    "-DSDLMIXER_MIDI_FLUIDSYNTH_SHARED=OFF",
    "-DSDLMIXER_MIDI_TIMIDITY=OFF",
    "-DSDLMIXER_OPUS=ON",
    "-DSDLMIXER_OPUS_SHARED=OFF",
    "-DSDLMIXER_VORBIS_STB=OFF",
    "-DSDLMIXER_VORBIS_VORBISFILE=ON",
    "-DSDLMIXER_VORBIS_VORBISFILE_SHARED=OFF",
    "-DSDLMIXER_WAVPACK=ON",
    "-DSDLMIXER_WAVPACK_SHARED=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "flac-devel",
    "fluidsynth-devel",
    "libvorbis-devel",
    "mpg123-devel",
    "opusfile-devel",
    "sdl3-devel",
    "wavpack-devel",
]
provides = [self.with_pkgver("sdl_mixer")]
pkgdesc = "SDL audio mixer library"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_mixer"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "f2ea848ccdf2f394cd4973ee0f6c482e04511044695cccfd46bab6dcd7f780aa"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3_mixer-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_mixer-devel")]
    return self.default_devel()

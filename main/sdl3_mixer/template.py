pkgname = "sdl3_mixer"
pkgver = "3.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DSDLMIXER_TESTS=OFF",
    "-DSDLMIXER_EXAMPLES=OFF",
    "-DSDLMIXER_FLAC_LIBFLAC=ON",
    "-DSDLMIXER_FLAC_DRFLAC=OFF",
    "-DSDLMIXER_FLAC_LIBFLAC_SHARED=OFF",
    "-DSDLMIXER_GME=OFF",
    "-DSDLMIXER_MP3_MPG123=ON",
    "-DSDLMIXER_MP3_DRMP3=OFF",
    "-DSDLMIXER_MP3_MPG123_SHARED=OFF",
    "-DSDLMIXER_MIDI_FLUIDSYNTH=ON",
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
pkgdesc = "SDL audio mixer library"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_mixer"
source = (
    f"https://libsdl.org/projects/SDL_mixer/release/SDL3_mixer-{pkgver}.tar.gz"
)
sha256 = "182a07c745375e113dc740d43964ff21b0be29f29f59876c4dbc4db3d32f6901"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3_mixer-devel")
def _(self):
    return self.default_devel()

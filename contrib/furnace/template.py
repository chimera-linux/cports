pkgname = "furnace"
pkgver = "0.6.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSYSTEM_FFTW=ON",
    "-DSYSTEM_FMT=ON",
    "-DSYSTEM_FREETYPE=ON",
    "-DSYSTEM_LIBSNDFILE=ON",
    "-DSYSTEM_PORTAUDIO=ON",
    "-DSYSTEM_RTMIDI=ON",
    "-DSYSTEM_SDL2=ON",
    "-DSYSTEM_ZLIB=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "fftw-devel",
    "fmt-devel",
    "freetype-devel",
    "libsndfile-devel",
    "pipewire-jack-devel",
    "portaudio-devel",
    "rtmidi-devel",
    "sdl-devel",
    "zlib-devel",
]
depends = ["zenity"]
pkgdesc = "Multi-system chiptune tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/tildearrow/furnace"
_adpcm_commit = "7736b178f4fb722d594c6ebdfc1ddf1af2ec81f7"
_adpcm_xq_commit = "6220fed7655e86a29702b45dbc641a028ed5a4bf"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/superctr/adpcm/archive/{_adpcm_commit}.tar.gz",
    f"https://github.com/dbry/adpcm-xq/archive/{_adpcm_xq_commit}.tar.gz",
]
source_paths = [".", "extern/adpcm", "extern/adpcm-xq"]
sha256 = [
    "e01df9ea9c5c625e7f3cbd59df34ab066be5b6d4e8675d445c62e4e1a5915476",
    "5e64cbd5414e7e64088c295446d90550cf5c2f80c12cb17737a16a31bbef7f1a",
    "601cf3905e7843f3d1477237a8ba358af08fa000ff8944651f40c986c7f57cff",
]

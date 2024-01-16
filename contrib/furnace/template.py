pkgname = "furnace"
pkgver = "0.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSYSTEM_FFTW=ON",
    "-DSYSTEM_FMT=ON",
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
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/superctr/adpcm/archive/{_adpcm_commit}.tar.gz",
]
source_paths = [".", "extern/adpcm"]
sha256 = [
    "d7d40da0234f379a689e8d5ad925e097e0ef487a72fe8d5c1b050cdc18f7fb44",
    "5e64cbd5414e7e64088c295446d90550cf5c2f80c12cb17737a16a31bbef7f1a",
]

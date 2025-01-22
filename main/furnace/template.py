pkgname = "furnace"
pkgver = "0.6.7"
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
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
depends = ["zenity"]
pkgdesc = "Multi-system chiptune tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://tildearrow.org/furnace"
_adpcm_commit = "ef7a217154badc3b99978ac481b268c8aab67bd8"
source = [
    f"https://github.com/tildearrow/furnace/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/superctr/adpcm/archive/{_adpcm_commit}.tar.gz",
]
source_paths = [".", "extern/adpcm"]
sha256 = [
    "94180a50ff9009c7d29f93c2ea64363ecea0f88e8eea3709221cb1a6e5e7b808",
    "46da29342d2968ff222ba00e07c646e038b76af2e6c86de037c653059a056251",
]

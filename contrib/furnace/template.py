pkgname = "furnace"
pkgver = "0.6.3"
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
_adpcm_commit = "ef7a217154badc3b99978ac481b268c8aab67bd8"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/superctr/adpcm/archive/{_adpcm_commit}.tar.gz",
]
source_paths = [".", "extern/adpcm"]
sha256 = [
    "bc28647c2175fc4e0c831d2d3f814c37828bb525af42897e5337f0e6c4168ffb",
    "46da29342d2968ff222ba00e07c646e038b76af2e6c86de037c653059a056251",
]

pkgname = "fluidsynth"
pkgver = "2.4.6"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=",
    "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2",
]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    "glib-devel",
    "libedit-readline-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "linux-headers",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl2-compat-devel",
]
pkgdesc = "Software synthesizer based on the SoundFont 2 specifications"
license = "LGPL-2.1-or-later"
url = "https://www.fluidsynth.org"
source = f"https://github.com/FluidSynth/fluidsynth/archive/v{pkgver}.tar.gz"
sha256 = "a6be90fd4842b9e7246500597180af5cf213c11bfa3998a3236dd8ff47961ea8"
# CFI: doesn't work (run drumstick-vpiano)
hardening = ["vis", "!cfi"]


@subpackage("fluidsynth-libs")
def _(self):
    self.renames = ["libfluidsynth"]
    return self.default_libs()


@subpackage("fluidsynth-devel")
def _(self):
    return self.default_devel()

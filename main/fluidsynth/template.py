pkgname = "fluidsynth"
pkgver = "2.6.2"
pkgrel = 0
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
    "gcem",
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
sha256 = "ca376b42a3c1b186a4c8c248931789a455ac94a89b777394969d678010c2f91f"
# CFI: doesn't work (run drumstick-vpiano)
hardening = ["vis", "!cfi"]


@split("libs")
def _(self):
    self.renames = ["libfluidsynth"]
    return self.default_libs()


@split("devel")
def _(self):
    return self.default_devel()

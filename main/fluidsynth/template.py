pkgname = "fluidsynth"
pkgver = "2.4.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=",
    "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2",
]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "libpulse-devel",
    "sdl2-compat-devel",
    "libsndfile-devel",
    "libedit-readline-devel",
    "linux-headers",
]
pkgdesc = "Software synthesizer based on the SoundFont 2 specifications"
license = "LGPL-2.1-or-later"
url = "https://www.fluidsynth.org"
source = f"https://github.com/FluidSynth/fluidsynth/archive/v{pkgver}.tar.gz"
sha256 = "2d2a5ca35bbb3f3fd241ef388a0cb3ae5755ebbb78121c7869f02b021d694810"
# CFI: doesn't work (run drumstick-vpiano)
hardening = ["vis", "!cfi"]


@subpackage("fluidsynth-libs")
def _(self):
    self.provides = [self.with_pkgver("libfluidsynth")]
    return self.default_libs()


@subpackage("fluidsynth-devel")
def _(self):
    return self.default_devel()

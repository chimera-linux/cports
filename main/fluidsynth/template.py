pkgname = "fluidsynth"
pkgver = "2.4.4"
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
sha256 = "fc492a255f453e65ac5b99a25e6ffbe0fbd64d6a4fe824bacd68de16fe8af7ba"
# CFI: doesn't work (run drumstick-vpiano)
hardening = ["vis", "!cfi"]


@subpackage("fluidsynth-libs")
def _(self):
    self.provides = [self.with_pkgver("libfluidsynth")]
    return self.default_libs()


@subpackage("fluidsynth-devel")
def _(self):
    return self.default_devel()

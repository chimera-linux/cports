pkgname = "fluidsynth"
pkgver = "2.3.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=",
    "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "glib-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "libpulse-devel",
    "sdl-devel",
    "libsndfile-devel",
    "libedit-readline-devel",
    "linux-headers",
]
pkgdesc = "Software synthesizer based on the SoundFont 2 specifications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.fluidsynth.org"
source = f"https://github.com/FluidSynth/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "1529ef5bc3b9ef3adc2a7964505912f7305103e269e50cc0316f500b22053ac9"
hardening = ["vis", "cfi"]


def do_check(self):
    # the tests only get built+ran on the check target and don't get built ahead
    # of time otherwise for ctest
    self.make.check()


@subpackage("libfluidsynth")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("fluidsynth-devel")
def _devel(self):
    return self.default_devel()

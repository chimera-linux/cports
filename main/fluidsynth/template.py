pkgname = "fluidsynth"
pkgver = "2.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=",
    "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2",
]
make_check_target = "check"
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
sha256 = "321f7d3f72206b2522f30a1cb8ad1936fd4533ffc4d29dd335b1953c9fb371e6"
hardening = ["vis", "cfi"]


@subpackage("libfluidsynth")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("fluidsynth-devel")
def _devel(self):
    return self.default_devel()

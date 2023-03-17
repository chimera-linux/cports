pkgname = "fluidsynth"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=", "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2"
]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "glib-devel", "pipewire-devel", "pipewire-jack-devel", "libpulse-devel",
    "sdl-devel", "libsndfile-devel", "libedit-devel", "linux-headers",
]
pkgdesc = "Software synthesizer based on the SoundFont 2 specifications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.fluidsynth.org"
source = f"https://github.com/FluidSynth/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "d734e4cf488be763cf123e5976f3154f0094815093eecdf71e0e9ae148431883"
hardening = ["vis", "cfi"]

@subpackage("libfluidsynth")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("fluidsynth-devel")
def _devel(self):
    return self.default_devel()

pkgname = "fluidsynth"
pkgver = "2.2.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_SUFFIX=", "-DDEFAULT_SOUNDFONT=/usr/share/soundfonts/default.sf2"
]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "glib-devel", "pipewire-jack-devel", "libpulse-devel",
    "libsndfile-devel", "libedit-devel", "linux-headers",
]
pkgdesc = "Software synthesizer based on the SoundFont 2 specifications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.fluidsynth.org"
source = f"https://github.com/FluidSynth/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "7c29a5cb7a2755c8012d941d1335da7bda957bbb0a86b7c59215d26773bb51fe"

@subpackage("libfluidsynth")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("fluidsynth-devel")
def _devel(self):
    return self.default_devel()

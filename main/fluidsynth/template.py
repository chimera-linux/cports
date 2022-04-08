pkgname = "fluidsynth"
pkgver = "2.2.6"
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
sha256 = "ca90fe675cacd9a7b442662783c4e7fa0e1fd638b28d64105a4e3fe0f618d20f"

@subpackage("libfluidsynth")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("fluidsynth-devel")
def _devel(self):
    return self.default_devel()

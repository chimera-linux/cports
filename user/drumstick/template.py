pkgname = "drumstick"
pkgver = "2.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "doxygen",
    "graphviz",
    "ninja",
    "pkgconf",
    "shared-mime-info",
]
makedepends = [
    "alsa-lib-devel",
    "fluidsynth-devel",
    "libpulse-devel",
    "pipewire-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "sonivox-devel",
]
pkgdesc = "MIDI libraries for Qt"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://drumstick.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/drumstick/drumstick-{pkgver}.tar.gz"
sha256 = "92f5fc2a94b8c9067200897fd14027f707bf0103871ea942e388f9afe95e0f34"


@subpackage("drumstick-devel")
def _(self):
    return self.default_devel()

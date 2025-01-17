pkgname = "vmpk"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "drumstick-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Virtual MIDI piano keyboard"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://sourceforge.net/projects/vmpk"
source = f"$(SOURCEFORGE_SITE)/vmpk/vmpk-{pkgver}.tar.gz"
sha256 = "3ac9cca97fcdbffd25605c5de88984e15a8b2dbeee885f626b1c5c499af80b51"

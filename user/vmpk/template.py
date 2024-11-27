pkgname = "vmpk"
pkgver = "0.9.0"
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
sha256 = "3cfd900843b1e068fda9a4e075c204086447a2e233d4800d785d2124480ae2f5"

pkgname = "faad2"
pkgver = "2.11.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Free AAC decoder"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/faac"
source = f"https://github.com/knik0/faad2/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "72dbc0494de9ee38d240f670eccf2b10ef715fd0508c305532ca3def3225bb06"


@subpackage("faad2-devel")
def _(self):
    return self.default_devel()

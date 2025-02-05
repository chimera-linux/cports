pkgname = "libspectre"
pkgver = "0.2.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_dir = "."  # ftbfs
hostmakedepends = ["pkgconf"]
makedepends = ["ghostscript-devel"]
checkdepends = ["cairo-devel"]
pkgdesc = "Small library for rendering PostScript documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/libspectre"
source = (
    f"http://libspectre.freedesktop.org/releases/libspectre-{pkgver}.tar.gz"
)
sha256 = "55a7517cd3572bd2565df0cf450944a04d5273b279ebb369a895391957f0f960"
hardening = ["vis", "cfi"]


@subpackage("libspectre-devel")
def _(self):
    return self.default_devel()


configure_gen = []

pkgname = "libspectrum"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "perl", "automake", "libtool"]
makedepends = ["glib-devel", "libgcrypt-devel"]
pkgdesc = "ZX Spectrum emulator support library"
maintainer = "logout <logout128@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://fuse-emulator.sourceforge.net/libspectrum.php"
source = f"$(SOURCEFORGE_SITE)/fuse-emulator/libspectrum/{pkgver}/libspectrum-{pkgver}.tar.gz"
sha256 = "a353cb46e9b1a281061d816353ea010d0a6fe78e6a17aa0b7b74271ca5e4acfc"


@subpackage("libspectrum-devel")
def _devel(self):
    return self.default_devel()

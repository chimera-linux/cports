pkgname = "libass"
pkgver = "0.15.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "yasm"]
makedepends = ["fontconfig-devel", "fribidi-devel", "harfbuzz-devel"]
pkgdesc = "Portable library for SSA/ASS subtitle rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/libass/libass"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1b2a54dda819ef84fa2dee3069cf99748a886363d2adb630fde87fe046e2d1d5"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libass-devel")
def _devel(self):
    return self.default_devel()

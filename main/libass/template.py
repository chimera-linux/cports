pkgname = "libass"
pkgver = "0.16.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "yasm"]
makedepends = ["fontconfig-devel", "fribidi-devel", "harfbuzz-devel"]
pkgdesc = "Portable library for SSA/ASS subtitle rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/libass/libass"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fea8019b1887cab9ab00c1e58614b4ec2b1cee339b3f7e446f5fab01b032d430"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libass-devel")
def _devel(self):
    return self.default_devel()

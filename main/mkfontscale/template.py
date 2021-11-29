pkgname = "mkfontscale"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-bzip2"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "zlib-devel", "libbz2-devel", "freetype-devel",
    "libfontenc-devel"
]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "X11 scalable font index generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ca0495eb974a179dd742bfa6199d561bda1c8da4a0c5a667f21fd82aaab6bac7"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

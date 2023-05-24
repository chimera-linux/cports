pkgname = "fontconfig"
pkgver = "2.14.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--enable-docs",
    f"--with-cache-dir=/var/cache/{pkgname}",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gperf", "gmake", "python"]
makedepends = ["libexpat-devel", "freetype-bootstrap", "libuuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/release/{pkgname}-{pkgver}.tar.gz"
sha256 = "3ba2dd92158718acec5caaf1a716043b5aa055c27b081d914af3ccb40dce8a55"


def post_install(self):
    self.install_license("COPYING")
    # reject bitmap fonts by default, preventing them from being preferred
    self.install_link(
        "/usr/share/fontconfig/conf.avail/70-no-bitmaps.conf",
        "etc/fonts/conf.d/70-no-bitmaps.conf",
    )


@subpackage("fontconfig-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

pkgname = "fontconfig"
pkgver = "2.14.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static", "--enable-docs",
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
sha256 = "b8f607d556e8257da2f3616b4d704be30fd73bd71e367355ca78963f9a7f0434"

def post_install(self):
    self.install_license("COPYING")
    # reject bitmap fonts by default, preventing them from being preferred
    self.install_link(
        f"/usr/share/fontconfig/conf.avail/70-no-bitmaps.conf",
        "etc/fonts/conf.d/70-no-bitmaps.conf"
    )

@subpackage("fontconfig-devel")
def _devel(self):
    return self.default_devel()

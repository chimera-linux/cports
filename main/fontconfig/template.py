pkgname = "fontconfig"
pkgver = "2.14.1"
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
sha256 = "ae480e9ca34382790312ff062c625ec70df94d6d9a9366e2b2b3d525f7f90387"

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

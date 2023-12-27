pkgname = "fontconfig"
pkgver = "2.15.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--enable-docs",
    f"--with-cache-dir=/var/cache/{pkgname}",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gperf",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = ["libexpat-devel", "freetype-bootstrap", "libuuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/release/{pkgname}-{pkgver}.tar.gz"
sha256 = "f5f359d6332861bd497570848fcb42520964a9e83d5e3abe397b6b6db9bcaaf4"


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "70-no-nonscalable.conf",
        "usr/share/fontconfig/conf.avail",
    )
    # reject bitmap fonts by default, preventing them from being preferred
    self.install_link(
        "/usr/share/fontconfig/conf.avail/70-no-nonscalable.conf",
        "etc/fonts/conf.d/70-no-nonscalable.conf",
    )


@subpackage("fontconfig-devel")
def _devel(self):
    return self.default_devel()

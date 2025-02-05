pkgname = "fontconfig"
pkgver = "2.16.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--enable-docs",
    f"--with-cache-dir=/var/cache/{pkgname}",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gperf",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = ["libexpat-devel", "freetype-bootstrap", "util-linux-uuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"$(FREEDESKTOP_SITE)/fontconfig/release/fontconfig-{pkgver}.tar.xz"
sha256 = "6a33dc555cc9ba8b10caf7695878ef134eeb36d0af366041f639b1da9b6ed220"


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "70-no-nonscalable.conf",
        "usr/share/fontconfig/conf.avail",
    )
    # reject bitmap fonts by default, preventing them from being preferred
    self.install_link(
        "etc/fonts/conf.d/70-no-nonscalable.conf",
        "../../../usr/share/fontconfig/conf.avail/70-no-nonscalable.conf",
    )


@subpackage("fontconfig-devel")
def _(self):
    return self.default_devel()

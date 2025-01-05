pkgname = "fontconfig"
pkgver = "2.15.0"
pkgrel = 3
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
makedepends = ["libexpat-devel", "freetype-bootstrap", "libuuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"$(FREEDESKTOP_SITE)/fontconfig/release/fontconfig-{pkgver}.tar.gz"
sha256 = "f5f359d6332861bd497570848fcb42520964a9e83d5e3abe397b6b6db9bcaaf4"

if self.profile().arch == "ppc":
    # sigtrap on real hardware
    hardening = ["!int"]


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

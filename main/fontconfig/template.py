pkgname = "fontconfig"
pkgver = "2.17.1"
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
license = "MIT"
url = "https://www.fontconfig.org"
source = f"https://gitlab.freedesktop.org/api/v4/projects/890/packages/generic/fontconfig/{pkgver}/fontconfig-{pkgver}.tar.xz"
sha256 = "9f5cae93f4fffc1fbc05ae99cdfc708cd60dfd6612ffc0512827025c026fa541"


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

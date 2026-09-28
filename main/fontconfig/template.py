pkgname = "fontconfig"
pkgver = "2.18.3"
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
sha256 = "4f7b554a38cdf78c033f666c8871f3749e14a094f65a07f630c91ed0b43d35e3"
options = ["etcfiles"]


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

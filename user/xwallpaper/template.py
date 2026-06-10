pkgname = "xwallpaper"
pkgver = "0.7.6"
pkgrel = 0

build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]

hostmakedepends = [
    "automake",
    "pkgconf",
]

makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libseccomp-devel",
    "libxcb-devel",
    "libxpm-devel",
    "linux-headers",
    "pixman-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
]

pkgdesc = "Wallpaper setting utility for X"
license = "ISC"
url = "https://github.com/stoeckmann/xwallpaper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "380aae8762a296f5e0284eff87ac92babd9c68e3e7612a8208f86b0dea814750"


def post_install(self):
    self.install_license("LICENSE")

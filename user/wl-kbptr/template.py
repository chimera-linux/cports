pkgname = "wl-kbptr"
pkgver = "0.4.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dopencv=enabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "opencv-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["jq"]
pkgdesc = "Control the mouse pointer with the keyboard"
license = "GPL-3.0-or-later"
url = "https://github.com/moverest/wl-kbptr"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3655f5305987dbac389a25e64c2f5a028c1651db70ea757024c4efa55c24338"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("helpers/wl-kbptr-sway-active-win")

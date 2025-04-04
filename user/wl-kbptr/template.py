pkgname = "wl-kbptr"
pkgver = "0.3.0"
pkgrel = 0
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
sha256 = "69775029acb8ff7d814a2868afe22e72b8c9c99cbb35b0acf57eccd3609b089c"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("helpers/wl-kbptr-sway-active-win")

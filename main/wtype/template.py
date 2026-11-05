pkgname = "wtype"
pkgver = "0.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["libxkbcommon-devel", "wayland-devel"]
pkgdesc = "Xdotool type for wayland"
license = "MIT"
url = "https://github.com/atx/wtype"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "684308ac8b47c510dddf4abac3aef86b4f7b8c0e165389a40608679a7a5b77ed"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

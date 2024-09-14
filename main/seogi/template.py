pkgname = "seogi"
pkgver = "1.1.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "argp-standalone",
    "elogind-devel",
    "libhangul-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Hangul IME for Wayland"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://github.com/mswiger/seogi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "243d28d54e448e98d2c910dd868c86fe83924c67309136898760d81deceb59a3"
tool_flags = {"LDFLAGS": ["-largp"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

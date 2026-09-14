pkgname = "noctalia-greeter"
pkgver = "1.3.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "clang",
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "librsvg-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "mesa-devel",
    "nlohmann-json",
    "pango-devel",
    "stb",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["dbus", "greetd"]
pkgdesc = "Greetd greeter, tightly coupled with Noctalia"
license = "MIT"
url = "https://github.com/noctalia-dev/noctalia-greeter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c3a2fce1d15efcf9c87f22b149d03c7dd378f273290c1488190cf8445edbc14d"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        "examples/*", "usr/share/examples/noctalia-greeter", glob=True
    )

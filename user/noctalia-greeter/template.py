pkgname = "noctalia-greeter"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "clang",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "libjxl-devel",
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
depends = ["greetd"]
pkgdesc = "Greetd greeter"
license = "MIT"
url = "https://github.com/noctalia-dev/noctalia-greeter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5b092784c0147bb6739efc2e8146d2d07e3572a59d7a370e93092f9f56d4fcc8"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        "examples/*", "usr/share/examples/noctalia-greeter", glob=True
    )

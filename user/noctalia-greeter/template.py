pkgname = "noctalia-greeter"
pkgver = "1.6.0"
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
sha256 = "f23ebf07cbe4508971c08b0b81d2b5bfc4ec1ec45605d8f8fb01b799743a70b6"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        "examples/*", "usr/share/examples/noctalia-greeter", glob=True
    )

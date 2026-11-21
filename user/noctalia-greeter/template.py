pkgname = "noctalia-greeter"
pkgver = "1.7.1"
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
sha256 = "79344d9629393ab3f4d605068eec94d2bfe8e12402618e1521f46111e27ff6ed"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        "examples/*", "usr/share/examples/noctalia-greeter", glob=True
    )

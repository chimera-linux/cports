pkgname = "noctalia"
pkgver = "5.0.0_beta8"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cairo-devel",
    "curl-devel",
    "elogind-devel",
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "jemalloc-devel",
    "libepoxy-devel",
    "libical-devel",
    "libjxl-devel",
    "libqalculate-devel",
    "librsvg-devel",
    "libsecret-devel",
    "libsndfile-devel",
    "libsodium-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "linux-pam-devel",
    "md4c-devel",
    "mesa-devel",
    "nlohmann-json",
    "pango-devel",
    "pipewire-devel",
    "polkit-devel",
    "sdbus-cpp-devel",
    "stb",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
    "wireplumber-devel",
]
pkgdesc = "Desktop shell for Wayland"
license = "MIT"
url = "https://noctalia.dev"
_upver = pkgver.replace("_beta", "-beta.")
source = f"https://github.com/noctalia-dev/noctalia/archive/v{_upver}.tar.gz"
sha256 = "a60e4ab8723f428e11b9a2bac97811aaa6a494648730abc61025c35cb728539e"


def post_install(self):
    self.install_license("LICENSE")

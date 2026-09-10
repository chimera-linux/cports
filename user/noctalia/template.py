pkgname = "noctalia"
pkgver = "5.0.1"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
]
hostmakedepends = [
    "gsed",
    "meson",
    "ninja",
    "pkgconf",
    "wayland-protocols",
]
makedepends = [
    "cairo-devel",
    "curl-devel",
    "fontconfig-devel",
    "freetype-devel",
    "glib-devel",
    "jemalloc-devel",
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
    "wireplumber-devel",
]
pkgdesc = "Minimal native Wayland desktop shell built on Wayland and OpenGL ES"
license = "MIT"
url = "https://github.com/noctalia-dev/noctalia"
source = f"https://github.com/noctalia-dev/noctalia/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ed8334f294e9f94f4744e315b674511fc51203a6a56c561af8803a6eb6884698"
# No tests for the package - Need an active Wayland environmenet to be executed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

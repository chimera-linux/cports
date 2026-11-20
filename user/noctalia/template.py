pkgname = "noctalia"
pkgver = "5.6.0"
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
# used by plugin management
depends = ["git"]
pkgdesc = "Desktop shell for Wayland"
license = "MIT"
url = "https://noctalia.dev"
source = f"https://github.com/noctalia-dev/noctalia/archive/v{pkgver}.tar.gz"
sha256 = "c2f0fcc30bae289ecc39ab495ae68120c5882902371cde14f4f08b8bf14210a1"
# Generates completions by running the built executable
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"noctalia.{shell}", "w") as outf:
            self.do(
                "./build/noctalia",
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("example.toml", "usr/share/examples/noctalia")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"noctalia.{shell}", shell)

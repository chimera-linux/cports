pkgname = "noctalia"
pkgver = "5.2.0"
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
depends = ["git"]
pkgdesc = "Desktop shell for Wayland"
license = "MIT"
url = "https://noctalia.dev"
source = f"https://github.com/noctalia-dev/noctalia/archive/v{pkgver}.tar.gz"
sha256 = "b1080bcb19c9ee7836153464d99021f34d1e3564f4bf4a26331a2af21234ddf8"
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

pkgname = "spotify-player"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "sdl-backend,streaming,media-control,image,sixel,notify",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "cbindgen",
    "cmake",
    "pkgconf",
    "rust-bindgen",
]
makedepends = [
    "dbus-devel",
    "libpulse-devel",
    "libsixel-devel",
    "openssl3-devel",
    "rust-std",
    "sdl2-compat-devel",
]
pkgdesc = "Spotify player in the terminal with full feature parity"
license = "MIT"
url = "https://github.com/aome510/spotify-player"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a1bc03ff6b1788283a38808745098d551f0d86b87a2fffabc61ceaaa17cfa93d"

if self.profile().wordsize == 32:
    broken = "needs atomic64"
elif self.profile().arch == "loongarch64":
    broken = "busted rustix"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/spotify_player")
    self.install_license("LICENSE")

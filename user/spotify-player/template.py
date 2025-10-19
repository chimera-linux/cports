pkgname = "spotify-player"
pkgver = "0.21.1"
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
sha256 = "f4679325c06967ce28a697f05d7ca181dbbd832b0aa2a1ca1ec41512157347b1"

if self.profile().wordsize == 32:
    broken = "needs atomic64"
elif self.profile().arch == "loongarch64":
    broken = "busted rustix"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/spotify_player")
    self.install_license("LICENSE")

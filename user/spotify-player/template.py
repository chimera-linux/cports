pkgname = "spotify-player"
pkgver = "0.20.4"
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
    "cmake",
    "cbindgen",
    "pkgconf",
    "rust-bindgen",
]
makedepends = [
    "libpulse-devel",
    "dbus-devel",
    "sdl2-compat-devel",
    "openssl3-devel",
    "libsixel-devel",
    "rust-std",
]
pkgdesc = "Spotify player in the terminal with full feature parity"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://github.com/aome510/spotify-player"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1d13f47ef4df3415835736f32629d57e331707d781507007ea04217a7dc735d8"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/spotify_player")
    self.install_license("LICENSE")

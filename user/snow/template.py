pkgname = "snow"
pkgver = "1.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "sdl2-compat-devel",
    "zstd-devel",
]
pkgdesc = "Classic Macintosh emulator"
license = "MIT"
url = "https://snowemu.com"
source = f"https://github.com/twvd/snow/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "00ee7515a8ed5e977e46b5f87a02ce964049613a5b909203b77b2feb277193a0"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/snowemu")
    self.install_license("LICENSE")
    with self.pushd("assets"):
        self.install_file(
            "snow.desktop",
            "usr/share/applications",
        )
        self.install_file(
            "dev.thomasw.snow.metainfo.xml",
            "usr/share/metainfo",
        )
        self.install_file("snow_icon.png", "usr/share/icons")

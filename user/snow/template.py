pkgname = "snow"
pkgver = "1.3.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "sdl2-devel",
    "zstd-devel",
]
pkgdesc = "Classic Macintosh emulator"
license = "MIT"
url = "https://snowemu.com"
source = f"https://github.com/twvd/snow/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "db733fc8948e30c8b8b4d78ae60991d84c7df63003d6bb8d3630379338dae3a5"

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

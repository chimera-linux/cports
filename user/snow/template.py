pkgname = "snow"
pkgver = "1.4.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "sdl2-devel",
    "zstd-devel",
]
pkgdesc = "Classic Macintosh emulator"
license = "MIT"
url = "https://snowemu.com"
source = f"https://github.com/twvd/snow/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c980c9ac4d952ddc21da63fe28a411852ff49463a6e62c647502b541e3d0b229"

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

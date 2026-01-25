pkgname = "snow"
pkgver = "1.3.0"
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
sha256 = "0b6bd694d75e2ad9043be635b40e1c7b06e7e37665d64464405b6e83e0d5993b"


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/snow_frontend_egui",
        name="snowemu",
    )
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

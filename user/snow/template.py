pkgname = "snow"
pkgver = "1.6.0"
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
sha256 = "d18eb6894e5e19f7057c84724236aa1f26bdcb1f0850ba490dabaf3d2eb0a90a"

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "snowemu"))
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

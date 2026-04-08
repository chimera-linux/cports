pkgname = "cosmic-launcher"
pkgver = "1.0.8"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
]
pkgdesc = "Cosmic desktop's application launcher UI"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-launcher"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "5dcecd911dceb5b360f6cc9f4cc4401aff3f58710f9c6d96b277c58653b05ce3"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/cosmic-launcher",
        "usr/bin",
        mode=0o755,
    )
    self.install_file(
        "data/com.system76.CosmicLauncher.desktop",
        "usr/share/applications",
        mode=0o644,
        name="defaults",
    )
    self.install_file(
        "data/com.system76.CosmicLauncher.metainfo.xml",
        "usr/share/metainfo",
        mode=0o644,
        name="tiling_exception_defaults",
    )
    self.install_license("LICENSE.md")

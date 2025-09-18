pkgname = "lapce"
pkgver = "0.4.4"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "openssl3-devel",
    "rust-std",
    "vulkan-loader-devel",
    "wayland-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Lightning-fast and powerful code editor"
license = "Apache-2.0"
url = "https://lapce.dev"
source = f"https://github.com/lapce/lapce/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1acfc01a1d9ac22cde0e2e8105de048fa6940d3f68b23b8b26438028109987a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lapce")
    self.install_bin(f"target/{self.profile().triplet}/release/lapce-proxy")
    self.install_file(
        "extra/linux/dev.lapce.lapce.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "extra/linux/dev.lapce.lapce.metainfo.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "extra/images/logo.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="dev.lapce.lapce.svg",
    )
    self.install_file(
        "extra/images/logo.png", "usr/share/pixmaps", name="dev.lapce.lapce.png"
    )

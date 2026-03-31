pkgname = "cosmic-comp"
pkgver = "1.0.8"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libdisplay-info-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "pixman-devel",
    "rust-std",
    "udev-devel",
]
depends = ["xrdb"]
pkgdesc = "Compositor for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-comp"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "b8f473d5ccc25a3ff0756f4a62c0c7ba80ad574f00e40b278a97dc6fd8705fda"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/cosmic-comp",
        "usr/bin",
        mode=0o755,
    )
    self.install_file(
        "data/keybindings.ron",
        "usr/share/cosmic/com.system76.CosmicSettings.Shortcuts/v1",
        mode=0o644,
        name="defaults",
    )
    self.install_file(
        "data/tiling-exceptions.ron",
        "usr/share/cosmic/com.system76.CosmicSettings.WindowRules/v1",
        mode=0o644,
        name="tiling_exception_defaults",
    )
    self.install_license("LICENSE")

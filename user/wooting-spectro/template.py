pkgname = "wooting-spectro"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "gtk+3-devel",
    "hidapi-devel",
    "pipewire-devel",
    "rust-std",
    "xdotool-devel",
]
depends = [
    "libayatana-appindicator-devel",
    "udev",
    "zenity",
]

pkgdesc = "Spectrum analyzer for Wooting keyboards"
license = "GPL-3.0-only"
url = "https://tinkery.primmr.dev/PrimmR/wooting-spectro"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "874c6f591c9333b08e009d9f458e7388086add06bdc8b6abdcee6d26067e3ddb"


def install(self):
    self.cargo.install(args=["--locked"])

    self.install_file("wooting-spectro.desktop", "usr/share/applications")

    self.install_file(
        "icons/icon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="wooting-spectro.svg",
    )

    self.install_file(
        self.files_path / "udev.rules",
        "usr/lib/udev/rules.d/",
        name="70-wooting.rules",
    )

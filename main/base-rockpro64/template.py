pkgname = "base-rockpro64"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-ap6256",
    "firmware-linux-rockchip",
    "u-boot-menu",
    "u-boot-rockpro64-rk3399",
]
pkgdesc = "Chimera base package for RockPro64"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "device", "usr/lib/u-boot")
    self.install_file(self.files_path / "cmdline", "usr/lib/u-boot")

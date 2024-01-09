pkgname = "base-rockpro64"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-ap6256",
    "firmware-linux-rockchip",
    "u-boot-rockpro64-rk3399",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for RockPro64"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    # agetty service customization
    self.install_file(self.files_path / "agetty", "etc/default")
    self.install_file(self.files_path / "agetty-ttyS2", "etc/default")

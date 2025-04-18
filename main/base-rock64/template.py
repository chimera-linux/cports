pkgname = "base-rock64"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-linux-rockchip",
    "u-boot-rock64-rk3328",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for Rock64"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")

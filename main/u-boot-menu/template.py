pkgname = "u-boot-menu"
pkgver = "0.1"
pkgrel = 2
depends = ["base-kernel"]
pkgdesc = "Common U-Boot boot menu generator for device targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


def install(self):
    # generator itself
    self.install_bin(self.files_path / "update-u-boot.sh", name="update-u-boot")
    # installer
    self.install_bin(
        self.files_path / "install-u-boot.sh", name="install-u-boot"
    )
    # config file
    self.install_file(self.files_path / "u-boot", "etc/default")
    # kernel hook
    self.install_file(
        self.files_path / "99-gen-uboot.sh", "usr/lib/kernel.d", mode=0o755
    )

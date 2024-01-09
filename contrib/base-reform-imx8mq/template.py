pkgname = "base-reform-imx8mq"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = ["u-boot-imx8mq_reform2", "u-boot-menu"]
pkgdesc = "Chimera base package for MNT Reform 2 with i.MX8MQ"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(self.files_path / "agetty", "etc/default")
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    self.install_file(self.files_path / "u-boot-fdt", "etc/default")

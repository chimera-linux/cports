pkgname = "base-reform-imx8mq"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = ["linux", "u-boot-imx8mq_reform2"]
pkgdesc = "Chimera base package for MNT Reform 2 with i.MX8MQ"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"

def do_install(self):
    # kernel hook
    self.install_file(
        self.files_path / "99-reform-kernel.sh", "etc/kernel.d", mode = 0o755
    )
    # cmdline
    self.install_file(self.files_path / "reform-cmdline", "etc/default")
    # agetty service
    self.install_service(self.files_path / "agetty-ttymxc0")

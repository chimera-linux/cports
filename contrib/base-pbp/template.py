pkgname = "base-pbp"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = [
    "firmware-ap6256", "linux-pbp", "u-boot-pbp",
    "u-boot-tools", "util-linux", "base-kernel"
]
pkgdesc = "Chimera base package for Pinebook Pro"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"

def do_install(self):
    self.install_file(
        self.files_path / "60-pinebookpro.rules", "usr/lib/udev/rules.d"
    )
    self.install_file(
        self.files_path / "10-pinebookpro.hwdb", "usr/lib/udev/hwdb.d"
    )
    self.install_file(self.files_path / "asound.state", "var/lib/alsa")
    # kernel hook
    self.install_file(
        self.files_path / "99-pbp-kernel.sh", "etc/kernel.d", mode = 0o755
    )
    # agetty service
    self.install_service(self.files_path / "agetty-ttyS2")

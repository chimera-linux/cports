pkgname = "initramfs-tools-growrootfs"
pkgver = "0.1"
pkgrel = 0
makedepends = ["dinit-chimera"]
depends = ["initramfs-tools", "util-linux-mount"]
pkgdesc = "Resize your root filesystem on first boot"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check", "!autosplit"]


def install(self):
    self.install_service(self.files_path / "early-growrootfs", enable=True)
    self.install_initramfs(
        self.files_path / "growrootfs.local-bottom",
        stype="local-bottom",
        name="growrootfs",
    )
    self.install_initramfs(
        self.files_path / "growrootfs.hook", name="growrootfs"
    )

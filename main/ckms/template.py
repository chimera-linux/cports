pkgname = "ckms"
pkgver = "0.1.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = ["python"]
pkgdesc = "Chimera Kernel Module System"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/ckms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b18de2c60927191725b91bda5f297bff7ed1f2a9da7239435c66a9012ad16dc9"
# no tests
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # kernel hook
    self.install_file(
        self.files_path / "10-ckms.sh", "usr/lib/kernel.d", mode=0o755
    )
    # initramfs refresh hook
    self.install_file(
        self.files_path / "refresh-initramfs.sh", "etc/ckms", mode=0o755
    )
    # depmod hook
    self.install_file(self.files_path / "depmod.sh", "etc/ckms", mode=0o755)

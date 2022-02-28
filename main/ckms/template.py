pkgname = "ckms"
pkgver = "0.0.1_git2022028"
_commit = "b9de0bd47a6e35cdb01c0c5ff50d7d5c34f4c938"
pkgrel = 0
depends = ["python"]
triggers = ["/usr/src"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/ckms"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "45d908885e07f415425e475e486ae1fc4ddd20879c429801e77e70533eebbcea"
# no tests
options = ["!check"]
system_users = ["_ckms"]

def do_install(self):
    self.install_dir("etc/ckms")
    self.install_file("config.ini", "etc/ckms")
    self.install_bin("ckms")
    # kernel hook
    self.install_file(
        self.files_path / "10-ckms.sh", "etc/kernel.d", mode = 0o755
    )
    # initramfs refresh hook
    self.install_file(
        self.files_path / "refresh-initramfs.sh", "etc/ckms", mode = 0o755
    )

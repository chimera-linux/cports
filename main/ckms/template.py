pkgname = "ckms"
pkgver = "0.0.1_git2022027"
_commit = "226327332ffd86c307cc3b92e09eb6e48ddc6cb8"
pkgrel = 0
depends = ["python"]
triggers = ["/usr/src"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/ckms"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "0713db942cac2bef669e8e69310444a54b7cefaaacf5d46a4ab7a9446a25e145"
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

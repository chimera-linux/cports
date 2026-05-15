pkgname = "emptty"
pkgver = "0.16.1"
pkgrel = 1
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "linux-pam-devel"]
pkgdesc = "TTY display manager"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e85d0658fd793ad97be90af241451a9374b299d9525d2aeb57a6f83f10ad4931"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

pkgname = "emptty"
pkgver = "0.16.0"
pkgrel = 0
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "linux-pam-devel"]
pkgdesc = "TTY display manager"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "35a5d60d21b4496a7df1b14ce7f7b7be0be9dc1e54c1e86e17e49f6dd83732a8"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

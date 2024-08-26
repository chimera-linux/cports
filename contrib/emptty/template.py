pkgname = "emptty"
pkgver = "0.13.0"
pkgrel = 0
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["libx11-devel", "linux-pam-devel"]
pkgdesc = "TTY display manager"
maintainer = "Michal Tvrznik <emporeor@gmail.com>"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "87e9e1ea10177043605912c4ff8019a4c0072c8cb704f6a0e5a38d5d3bf01053"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

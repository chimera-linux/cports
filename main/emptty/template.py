pkgname = "emptty"
pkgver = "0.13.0"
pkgrel = 3
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["libx11-devel", "linux-pam-devel"]
pkgdesc = "TTY display manager"
maintainer = "Michal Tvrznik <emporeor@gmail.com>"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3bed150f359fa46664ff28bff9d15306b899e147e60d486eb3a415afd7e2f3ba"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

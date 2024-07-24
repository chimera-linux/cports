pkgname = "emptty"
pkgver = "0.12.1"
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
sha256 = "0220230cdee3dedd7ccd6f2d81c57b29e2169159c8e28263d58abaf20093ce23"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

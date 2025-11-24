pkgname = "emptty"
pkgver = "0.14.0"
pkgrel = 5
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "libx11-devel", "linux-pam-devel"]
pkgdesc = "TTY display manager"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4b95a8b6d7d09bd4c80fb16e33ac8295344d81186f6f5c2601f237795e93859"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

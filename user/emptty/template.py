pkgname = "emptty"
pkgver = "0.15.0"
pkgrel = 0
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "libx11-devel", "linux-pam-devel"]
pkgdesc = "TTY display manager"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fae7c04afeeb9ef3dcbb9bca67e9a2fa940e99a91872ebc0775e10253972c7f3"


def post_install(self):
    self.install_file("res/pam", "usr/lib/pam.d", name="emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_service(self.files_path / "dinit-service", "emptty")
    self.install_license("LICENSE")
    self.install_man("res/emptty.1")

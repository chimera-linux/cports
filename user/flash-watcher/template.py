pkgname = "flash-watcher"
pkgver = "0.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "File watcher that executes commands when files change"
license = "MIT"
url = "https://github.com/sage-scm/Flash"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dd9604dabbf0c864e59ad41ce24b91293a436b76ecb9a1c18a8cc53878c7753c"


def post_install(self):
    self.install_license("LICENSE")

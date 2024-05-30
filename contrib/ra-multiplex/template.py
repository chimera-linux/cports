pkgname = "ra-multiplex"
pkgver = "0.2.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Share a language server instance between multiple clients"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/pr2502/ra-multiplex"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a6e52a26d2e707341b8b2440190b94d9f6b57040496fb7c859da0bb5f34ccbb2"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "ra-multiplex.user")

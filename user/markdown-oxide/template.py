pkgname = "markdown-oxide"
pkgver = "0.25.11"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "PKM Markdown Language Server"
license = "Apache-2.0"
url = "https://github.com/Feel-ix-343/markdown-oxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "274446b861ebbf3098dcb7e0a5d3135df88df34b16a2c128288f900391dfbf75"


def post_install(self):
    self.install_license("LICENSE")

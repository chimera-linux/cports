pkgname = "markdown-oxide"
pkgver = "0.25.12"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "PKM Markdown language server"
license = "Apache-2.0"
url = "https://oxide.md"
source = (
    f"https://github.com/Feel-ix-343/markdown-oxide/archive/v{pkgver}.tar.gz"
)
sha256 = "fc7c472c2bd93a9b8f58848d71f054ed02442310f5328081f3036a7ce79040cb"

pkgname = "numbat"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "High precision scientific calculator"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/numbat"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a0435bf938d6166c5089106cfb39049b0b207dec69a96552ccc3f114d515fd9"


def do_install(self):
    self.cargo.install(wrksrc="numbat-cli")
    self.install_license("LICENSE-MIT")
    self.install_files("numbat/modules", "usr/share/numbat")

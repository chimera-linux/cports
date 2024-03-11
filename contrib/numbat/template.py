pkgname = "numbat"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "High precision scientific calculator"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/numbat"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9543f449e758b2db6d1299b4eee88dbeac1ba57a427580c7f45d3ee613b089a0"


def do_install(self):
    self.cargo.install(wrksrc="numbat-cli")
    self.install_license("LICENSE-MIT")
    self.install_files("numbat/modules", "usr/share/numbat")

    self.install_file("assets/numbat.desktop", "usr/share/applications")
    self.install_file(
        "assets/numbat.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    for f in [16, 22, 24, 32, 48, 64, 128, 256, 512]:
        self.install_file(
            f"assets/numbat-{f}x{f}.png",
            f"usr/share/icons/hicolor/{f}x{f}/apps",
            name="numbat.png",
        )

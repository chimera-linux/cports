pkgname = "numbat"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cargo"
# Tries to access network
make_check_args = ["--", "--skip=examples_can_be_parsed_and_interpreted"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["tzdata"]
pkgdesc = "High-precision scientific calculator"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/numbat"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3c152ec83dd0615cc62d7f92164fabad361d853f3796db22c79c20fa060e26b4"


def install(self):
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

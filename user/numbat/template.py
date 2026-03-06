pkgname = "numbat"
pkgver = "1.23.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
# Tries to access network
make_check_args = ["--", "--skip=examples_can_be_parsed_and_interpreted"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
depends = ["tzdb"]
pkgdesc = "High-precision scientific calculator"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/numbat"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "578c0ff6cb80098baca84042a104644758907002e4fc7ba839a1266be7f4af28"


def install(self):
    self.cargo.install(wrksrc="numbat-cli")
    self.install_license("LICENSE-MIT")
    self.install_files("numbat/modules", "usr/share/numbat")

    self.install_file("assets/numbat.desktop", "usr/share/applications")
    self.install_file(
        "assets/numbat.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    self.install_file("assets/numbat.vim", "usr/share/vim/vimfiles/syntax")
    for f in [16, 22, 24, 32, 48, 64, 128, 256, 512]:
        self.install_file(
            f"assets/numbat-{f}x{f}.png",
            f"usr/share/icons/hicolor/{f}x{f}/apps",
            name="numbat.png",
        )

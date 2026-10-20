pkgname = "eza"
pkgver = "0.23.5"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Directory listing utility"
license = "EUPL-1.2"
url = "https://eza.rocks"
source = [
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/eza-community/eza/releases/download/v{pkgver}/man-{pkgver}.tar.gz",
]
source_paths = [".", "manpage"]
sha256 = [
    "bbf179f2611c904014431740b559e8055276c12fcf978a7e31c271663548337f",
    "cbdae2ad79ae0ef1fd6a06f4644c90cef79a56353bc3bb7cf4663bb2831420f9",
]


def post_install(self):
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
    self.install_completion("completions/nush/eza.nu", "nushell")
    self.install_man(f"manpage/man-{pkgver}/eza.1")
    self.install_man(f"manpage/man-{pkgver}/eza_colors.5")
    self.install_man(f"manpage/man-{pkgver}/eza_colors-explanation.5")

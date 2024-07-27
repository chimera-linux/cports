pkgname = "bottom"
pkgver = "0.9.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Process and system monitor"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/ClementTsang/bottom"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/completion.tar.gz",
    f"{url}/releases/download/{pkgver}/manpage.tar.gz",
]
source_paths = [
    ".",
    "completions",
    "man",
]
sha256 = [
    "29c3f75323ae0245576ea23268bb0956757352bf3b16d05f511357655b9cc71e",
    "721b3921157cbc3f31f20f0aaaea468a235b3d0fa8f876cbf9d3867578db8203",
    "e828123c48bfaec804db06dd211c7e4bb2c9899100c9a68522607832789a3ddb",
]


def post_install(self):
    self.install_license("LICENSE")
    self.do("gunzip", self.chroot_cwd / "man/btm.1.gz")
    self.install_man("man/btm.1")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")

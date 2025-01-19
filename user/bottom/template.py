pkgname = "bottom"
pkgver = "0.10.2"
pkgrel = 1
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
    "1db45fe9bc1fabb62d67bf8a1ea50c96e78ff4d2a5e25bf8ae8880e3ad5af80a",
    "899be2ef2d1cd8406f11536d1828b568161fdabafbf0a7172a58bd3b636fcda0",
    "d9f99261e51f29f81b4e3bcf439f43c41e3a7ccf07ba55754c8aeda0fa6edf5f",
]


def post_install(self):
    self.install_license("LICENSE")
    self.do("gunzip", self.chroot_cwd / "man/btm.1.gz")
    self.install_man("man/btm.1")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")

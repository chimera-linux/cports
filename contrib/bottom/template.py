pkgname = "bottom"
pkgver = "0.9.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
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
    "202130e0d7c362d0d0cf211f6a13e31be3a02f13f998f88571e59a7735d60667",
    "74a525a17f56e3553bc179ab803d2568a9fe4b5599586f017edcf1d43913daa5",
    "a22799302ae15ac0b6ed037f35b6f857e264d78e06446b638bc5464846dd5046",
]


def post_install(self):
    self.install_license("LICENSE")
    self.do("gunzip", self.chroot_cwd / "man/btm.1.gz")
    self.install_man("man/btm.1")
    self.install_completion("completions/btm.bash", "bash")
    self.install_completion("completions/btm.fish", "fish")
    self.install_completion("completions/_btm", "zsh")

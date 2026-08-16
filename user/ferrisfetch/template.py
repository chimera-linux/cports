pkgname = "ferrisfetch"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fast, lightweight Linux system information fetch tool"
license = "MIT"
url = "https://github.com/kk376/ferrisfetch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6e2fbf052988cb945c436087f42dcf9ebd8885d3cd19638b58221e7d41eca9df"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/ferrisfetch.bash", "bash")
    self.install_completion("completions/ferrisfetch.fish", "fish")
    self.install_completion("completions/_ferrisfetch", "zsh")

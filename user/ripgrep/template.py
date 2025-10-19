pkgname = "ripgrep"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cargo"
# we patch lockfile
prepare_after_patch = True
make_build_args = ["--features", "pcre2"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcre2-devel"]
pkgdesc = "Recursive grep-like tool"
license = "MIT OR Unlicense"
url = "https://github.com/BurntSushi/ripgrep"
source = [
    f"{url}/archive/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/ripgrep-{pkgver}-x86_64-unknown-linux-musl.tar.gz",
]
source_paths = [".", "docs-prebuilt"]
sha256 = [
    "e6b2d35ff79c3327edc0c92a29dc4bb74e82d8ee4b8156fb98e767678716be7a",
    "253ad0fd5fef0d64cba56c70dccdacc1916d4ed70ad057cc525fcdb0c3bbd2a7",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rg")
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

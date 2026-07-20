pkgname = "ripgrep"
pkgver = "15.2.0"
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
    "7605249d3eb0d5f170e3414498e3344e26b1e7a147aec518b57090b80036a562",
    "33e15bcf1624b25cdd2a55813a47a2f95dbe126268203e76aa6a585d1e7b149c",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rg")
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

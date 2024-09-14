pkgname = "ripgrep"
pkgver = "14.1.1"
pkgrel = 0
build_style = "cargo"
# we patch lockfile
prepare_after_patch = True
make_build_args = ["--features", "pcre2"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcre2-devel"]
pkgdesc = "Recursive grep-like tool"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/BurntSushi/ripgrep"
source = [
    f"{url}/archive/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/ripgrep-{pkgver}-x86_64-unknown-linux-musl.tar.gz",
]
source_paths = [".", "docs-prebuilt"]
sha256 = [
    "4dad02a2f9c8c3c8d89434e47337aa654cb0e2aa50e806589132f186bf5c2b66",
    "4cf9f2741e6c465ffdb7c26f38056a59e2a2544b51f7cc128ef28337eeae4d8e",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rg")
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

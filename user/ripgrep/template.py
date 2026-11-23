pkgname = "ripgrep"
pkgver = "16.0.0"
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
    "17e7a1a0db80ed9618a0963c7ae4aecb8fce25c70cf7ebed514daf2b38a0d153",
    "54268ab4643c00a290a29b0086066d64b3f56236dd805ec64629a86f9bd29fd0",
]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "rg"))
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

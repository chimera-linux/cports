pkgname = "ripgrep"
pkgver = "14.1.0"
pkgrel = 1
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
    "33c6169596a6bbfdc81415910008f26e0809422fda2d849562637996553b2ab6",
    "f84757b07f425fe5cf11d87df6644691c644a5cd2348a2c670894272999d3ba7",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rg")
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

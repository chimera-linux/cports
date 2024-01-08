pkgname = "ripgrep"
pkgver = "14.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = (
    "Tool that recursively searches the current directory for a regex pattern"
)
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


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("docs-prebuilt/doc/rg.1")
    self.install_completion("docs-prebuilt/complete/rg.bash", "bash", "rg")
    self.install_completion("docs-prebuilt/complete/rg.fish", "fish", "rg")
    self.install_completion("docs-prebuilt/complete/_rg", "zsh", "rg")

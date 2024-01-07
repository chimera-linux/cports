pkgname = "ripgrep"
pkgver = "14.0.3"
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
    "f5794364ddfda1e0411ab6cad6dd63abe3a6b421d658d9fee017540ea4c31a0e",
    "62cd0efc4d6f1817b9c852859987b4720cd52e0de008418266e8503028dc0c7a",
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

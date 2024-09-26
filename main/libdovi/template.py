pkgname = "libdovi"
pkgver = "3.3.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "pkgconf",
]
makedepends = ["rust-std"]
pkgdesc = "Library to read & write Dolby Vision metadata"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/quietvoid/dovi_tool"
source = f"{url}/archive/refs/tags/libdovi-{pkgver}.tar.gz"
sha256 = "4cd7a4c418fd8af1da13278ce7524c15b7fdf61e1fe53663aa291c68c5062777"
# literally one test lol
options = ["!check"]


def prepare(self):
    self.cargo.vendor(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def build(self):
    self.cargo.cbuild(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def check(self):
    self.cargo.check(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def install(self):
    self.cargo.cinstall(wrksrc="dolby_vision")
    self.install_license("LICENSE")


@subpackage("libdovi-devel")
def _(self):
    return self.default_devel()

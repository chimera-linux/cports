pkgname = "uv"
pkgver = "0.4.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Python package installer"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/astral-sh/uv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c0dab196cc4f8141a29f72ac9f02e6542812bf283a8af06db477d92cfedef308"
# too many of them need net
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def post_install(self):
    self.install_license("LICENSE-MIT")

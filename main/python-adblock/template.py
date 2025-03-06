pkgname = "python-adblock"
pkgver = "0.6.0"
pkgrel = 4
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
    "python-setuptools-rust",
    "python-wheel",
]
makedepends = ["rust-std"]
depends = ["python"]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Python wrapper for Brave's adblocking library"
license = "Apache-2.0 OR MIT"
url = "https://github.com/ArniDagur/python-adblock"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cdde5db640f1d9205785641665b79e6edb7c51092a68536bc4907560c71136b2"
# XXX: requires pre-installing the package
options = ["!check"]


def prepare(self):
    from cbuild.util import cargo

    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )
    self.do(
        "cargo",
        "update",
        "--package",
        "target-lexicon",
        "--precise",
        "0.12.16",
        allow_network=True,
    )

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE-MIT")

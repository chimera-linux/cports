pkgname = "uv"
pkgver = "0.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
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
sha256 = "d585904958c0fb12bdb65a975e27912f6fccbea0030ea9a196c74bee6b1227d2"
# too many of them need net
options = ["!check"]


if self.profile().arch == "riscv64":
    broken = "stuck forever"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()

    # TODO: our cargo vendor does not take into account custom source entries
    # (this is spat out by `cargo vendor`)

    with open(f"{self.cwd}/.cargo/config.toml", "a") as f:
        f.write(
            """
[source."git+https://github.com/astral-sh/pubgrub?rev=aaef464c1b0d8eea4ff9ffaee4f3458c236d10da"]
git = "https://github.com/astral-sh/pubgrub"
rev = "aaef464c1b0d8eea4ff9ffaee4f3458c236d10da"
replace-with = "vendored-sources"
[source."git+https://github.com/astral-sh/reqwest-middleware?rev=5e3eaf254b5bd481c75d2710eed055f95b756913"]
git = "https://github.com/astral-sh/reqwest-middleware"
rev = "5e3eaf254b5bd481c75d2710eed055f95b756913"
replace-with = "vendored-sources"
[source."git+https://github.com/charliermarsh/rs-async-zip?rev=011b24604fa7bc223daaad7712c0694bac8f0a87"]
git = "https://github.com/charliermarsh/rs-async-zip"
rev = "011b24604fa7bc223daaad7712c0694bac8f0a87"
replace-with = "vendored-sources"
"""
        )


def do_check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE-MIT")

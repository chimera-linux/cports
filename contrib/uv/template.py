pkgname = "uv"
pkgver = "0.2.34"
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
sha256 = "b111d5f6c4958bab14a6c4e3c4a77dc576a900aa3ce48caf0c2269901df64652"
# too many of them need net
options = ["!check"]


if self.profile().arch == "riscv64":
    broken = "stuck forever"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)

    # TODO: our cargo vendor does not take into account custom source entries
    # (this is spat out by `cargo vendor`)

    with open(f"{self.cwd}/.cargo/config.toml", "a") as f:
        f.write(
            """
[source."git+https://github.com/astral-sh/pubgrub?rev=2fac39371a47e7cb821e510aaa4de25405413d29"]
git = "https://github.com/astral-sh/pubgrub"
rev = "2fac39371a47e7cb821e510aaa4de25405413d29"
replace-with = "vendored-sources"
[source."git+https://github.com/astral-sh/reqwest-middleware?rev=21ceec9a5fd2e8d6f71c3ea2999078fecbd13cbe"]
git = "https://github.com/astral-sh/reqwest-middleware"
rev = "21ceec9a5fd2e8d6f71c3ea2999078fecbd13cbe"
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

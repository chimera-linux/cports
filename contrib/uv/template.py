pkgname = "uv"
pkgver = "0.2.28"
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
sha256 = "3a99515b8031c7622baa3c677a19b53a2459b0c5a32b5752751a7296b2e99f20"
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
[source."git+https://github.com/astral-sh/pubgrub?rev=3f0ba760951ab0deeac874b98bb18fc90103fcf7"]
git = "https://github.com/astral-sh/pubgrub"
rev = "3f0ba760951ab0deeac874b98bb18fc90103fcf7"
replace-with = "vendored-sources"
[source."git+https://github.com/astral-sh/reqwest-middleware?rev=21ceec9a5fd2e8d6f71c3ea2999078fecbd13cbe"]
git = "https://github.com/astral-sh/reqwest-middleware"
rev = "21ceec9a5fd2e8d6f71c3ea2999078fecbd13cbe"
replace-with = "vendored-sources"
[source."git+https://github.com/charliermarsh/rs-async-zip?rev=1dcb40cfe1bf5325a6fd4bfcf9894db40241f585"]
git = "https://github.com/charliermarsh/rs-async-zip"
rev = "1dcb40cfe1bf5325a6fd4bfcf9894db40241f585"
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

pkgname = "uv"
pkgver = "0.13.4"
pkgrel = 1
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
license = "Apache-2.0 OR MIT"
url = "https://github.com/astral-sh/uv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "182d66815490dbb497b456a6fde93c7e66ae7f27a50a2065b3b5a06fbb3a20bd"
# too many of them need net
# completions with host bin
options = ["!check", "!cross"]

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.44.0")
    cargo.clear_vendor_checksums(self, "linux-raw-sys-0.12.1")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    from cbuild.util import cargo

    for cmd in ["uv", "uvx"]:
        for shell in ["bash", "fish", "nushell", "zsh"]:
            with open(self.cwd / f"{cmd}.{shell}", "w") as cf:
                self.do(
                    cargo.target_path(self, cmd),
                    "--generate-shell-completion",
                    shell,
                    stdout=cf,
                )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def post_install(self):
    self.install_license("LICENSE-MIT")
    for cmd in ["uv", "uvx"]:
        for shell in ["bash", "fish", "nushell", "zsh"]:
            self.install_completion(f"{cmd}.{shell}", shell, cmd)

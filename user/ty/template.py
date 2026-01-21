pkgname = "ty"
pkgver = "0.0.12"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo-auditable",
    "git",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Python type checker and language server"
license = "MIT"
url = "https://github.com/astral-sh/ty"
source = f"https://github.com/astral-sh/ty/releases/download/{pkgver}/source.tar.gz>{pkgname}_{pkgver}.tar.gz"
sha256 = "4dfc2aa8058445556949f0bc798ede40a3f098971b61a0d4a973c69716393624"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="ruff")

    self.mv("ruff/.cargo", ".")
    self.do(
        "sed",
        "-i",
        "",
        "-e",
        's#directory = "vendor"#directory = "ruff/vendor"#',
        ".cargo/config.toml",
    )


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check(wrksrc="ruff")


def post_install(self):
    self.install_license("LICENSE")

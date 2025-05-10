pkgname = "ty"
pkgver = "0.0.1.19"
_ver = "0.0.1-alpha.19"
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
source = (
    f"https://github.com/astral-sh/ty/releases/download/{_ver}/source.tar.gz"
)
sha256 = "889f566a41e0f9b1c2eef106321cd047788f6bf4df0b3f67c70a8507863c78ab"
# can't be arsed for an early alpha where there's not even working tarballs
options = ["!check"]


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


def post_install(self):
    self.install_license("LICENSE")

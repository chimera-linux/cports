pkgname = "ty"
pkgver = "0.0.18"
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
sha256 = "041796166dbe3ac1079a8b5b7c676a35529944036ffa2355ab91542ccdb484c9"


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

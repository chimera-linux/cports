pkgname = "taskwarrior"
pkgver = "3.4.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSYSTEM_CORROSION=ON"]
make_dir = "."
hostmakedepends = [
    "cargo",
    "cmake",
    "corrosion",
    "cxxbridge",
    "ninja",
    "rust-bindgen",
]
makedepends = ["util-linux-uuid-devel", "rust-std", "sqlite-devel"]
pkgdesc = "TODO list manager for the command line"
license = "MIT"
url = "https://taskwarrior.org"
source = f"https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v{pkgver}/task-{pkgver}.tar.gz"
sha256 = "d302761fcd1268e4a5a545613a2b68c61abd50c0bcaade3b3e68d728dd02e716"

if self.profile().wordsize == 32:
    broken = "atomic64 assumptions"


def post_patch(self):
    from cbuild.util import cargo

    # match packaged cxxbridge
    self.do(
        "cargo",
        "update",
        "--package",
        "cxx",
        "--precise",
        "1.0.150",
        allow_network=True,
    )

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE")

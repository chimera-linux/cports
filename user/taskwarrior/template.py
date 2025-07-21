pkgname = "taskwarrior"
pkgver = "3.4.1"
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
sha256 = "23eb60f73e42f16111cc3912b44ee12be6768860a2db2a9c6a47f8ac4786bac3"

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
    self.install_license("COPYING")

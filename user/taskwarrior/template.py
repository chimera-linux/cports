pkgname = "taskwarrior"
pkgver = "3.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSYSTEM_CORROSION=ON"]
make_dir = "."
hostmakedepends = ["cmake", "ninja", "cargo", "corrosion", "cxxbridge"]
makedepends = ["util-linux-uuid-devel", "rust-std", "sqlite-devel"]
pkgdesc = "TODO list manager for the command line"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://taskwarrior.org"
source = f"https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v{pkgver}/task-{pkgver}.tar.gz"
sha256 = "7fd1e3571f673679758f001b5f44963eee59fd0d2cac887a5807cf2fd90856a1"

if self.profile().wordsize == 32:
    broken = "atomic64 assumptions"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("COPYING")

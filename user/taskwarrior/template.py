pkgname = "taskwarrior"
pkgver = "3.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSYSTEM_CORROSION=ON"]
make_dir = "."
hostmakedepends = ["cmake", "ninja", "cargo", "corrosion"]
makedepends = ["libuuid-devel", "rust-std", "sqlite-devel"]
pkgdesc = "TODO list manager for the command line"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://taskwarrior.org"
source = f"https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v{pkgver}/task-{pkgver}.tar.gz"
sha256 = "1ae67c74b84067573a53095cf3cb6718245dd7dd808f19f9b3d85da445838b4f"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("COPYING")

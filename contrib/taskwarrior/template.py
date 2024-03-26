pkgname = "taskwarrior"
pkgver = "3.0.0"
pkgrel = 0
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja", "cargo", "corrosion"]
makedepends = ["libuuid-devel"]
pkgdesc = "TODO list manager for the command line"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://taskwarrior.org"
source = f"https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v{pkgver}/task-{pkgver}.tar.gz"
sha256 = "30f397081044f5dc2e5a0ba51609223011a23281cd9947ea718df98d149fcc83"


def post_extract(self):
    (self.cwd / ".cargo" / "config").unlink()


def post_patch(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("COPYING")

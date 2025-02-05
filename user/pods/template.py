pkgname = "pods"
pkgver = "2.1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
    "rust-clippy",
]
makedepends = [
    "appstream-glib-devel",
    "glib-devel",
    "gtksourceview-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "rust-std",
    "vte-gtk4-devel",
]
pkgdesc = "GTK frontend for podman"
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-3.0-only"
url = "https://github.com/marhkb/pods"
source = f"https://github.com/marhkb/pods/releases/download/v{pkgver}/pods-v{pkgver}.tar.xz"
sha256 = "259fe1830e1efcde5bea5afabd234907361ef6727c0b29c4f289427b1f1e5360"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_extract(self):
    self.rm(".cargo/config")


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/pods")

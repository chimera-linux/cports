pkgname = "pods"
pkgver = "2.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "appstream-glib-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "rust-std",
    "vte-gtk4-devel",
]
pkgdesc = "GTK frontend for podman"
license = "GPL-3.0-only"
url = "https://github.com/marhkb/pods"
source = f"https://github.com/marhkb/pods/releases/download/v{pkgver}/pods-v{pkgver}.tar.xz"
sha256 = "8afd0df06fafa1c96a0144d864ce74c330b3bb90a3074f66a7d6e1c78538e823"

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

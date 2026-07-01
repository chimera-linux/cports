pkgname = "pods"
pkgver = "3.0.0"
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
sha256 = "473e6675d8389e92acd0d61283c52de8f61de67a8cb728514b780161126485d3"

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

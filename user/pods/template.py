pkgname = "pods"
pkgver = "3.1.1"
pkgrel = 0
build_style = "meson"
make_build_env = {}
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
sha256 = "e13a8a36f8beac8f5194b297abdef2ac4424f4c49117f83a2afb735e15c6e48b"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    # loongarch64-chimera-linux-musl-ld: error: address assignment did not converge
    make_build_env["RUSTFLAGS"] = "-C link-arg=-mno-relax"


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

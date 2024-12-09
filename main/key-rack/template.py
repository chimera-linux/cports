pkgname = "key-rack"
pkgver = "0.4.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "libadwaita-devel",
    "rust-std",
]
pkgdesc = "View and edit keyring secrets"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://gitlab.gnome.org/World/key-rack"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "0ea5b243cefaf0acda3222691eec0ba6af0dc0e33528299eca98632d9f5cf245"
# target deleted below
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]

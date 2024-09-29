pkgname = "pipeline"
pkgver = "2.0.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = ["clapper-devel", "libadwaita-devel", "openssl-devel", "rust-std"]
pkgdesc = "GTK-based Youtube video player"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://mobile.schmidhuberj.de/pipeline"
source = (
    f"https://gitlab.com/schmiddi-on-mobile/pipeline/-/archive/v{pkgver}.tar.gz"
)
sha256 = "8408e670777cb72d59bf2a08057254432b178cf65353dc8dbd6110eb06e2f30a"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"./build/target/{self.profile().triplet}/release/tubefeeder"
    )

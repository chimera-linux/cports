pkgname = "glycin-loaders"
pkgver = "1.0.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=false"]
hostmakedepends = [
    "cargo",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "libheif-devel",
    "libjxl-devel",
    "libseccomp-devel",
    "libxml2-devel",
    "pango-devel",
    "rust-std",
]
depends = ["bubblewrap"]
pkgdesc = "Sandboxed and extendable image decoding"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/sophie-h/glycin"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d0f022462ff555856e85ea940474470bb36b37c9ffcbcba63a03fe5e954370cf"
# Needs loaders to be system-installed
options = ["!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    for loader in (self.cwd / "loaders").glob("glycin-*"):
        self.install_file(
            f"./build/cargo_target/loaders/{self.profile().triplet}/release/{loader.name}",
            "usr/libexec/glycin-loaders/1+",
            mode=0o755,
        )

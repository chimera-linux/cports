pkgname = "papers"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcomics=enabled",
    "-Ddocumentation=false",
    "-Dtiff=enabled",
    "-Ddjvu=enabled",
    "-Dtests=false",
]
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "itstool",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "djvulibre-devel",
    "exempi-devel",
    "gdk-pixbuf-devel",
    "gobject-introspection",
    "libadwaita-devel",
    "libarchive-devel",
    "libgxps-devel",
    "libsecret-devel",
    "libspelling-devel",
    "nautilus-devel",
    "poppler-devel",
    "rust-std",
]
pkgdesc = "GNOME document viewer"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/papers"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "13c60125f8d58ac0e4f0a7bd391fd41193ab6bcd1055b0f6827fc8eb21b1753e"
# needs thumbnailer copied etc, whatever don't care
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="shell").vendor()
    cargo.Cargo(self, wrksrc="thumbnailer").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"./build/shell/src/{self.profile().triplet}/release/papers"
    )
    self.install_bin(
        f"./build/thumbnailer/{self.profile().triplet}/release/papers-thumbnailer"
    )


@subpackage("papers-devel")
def _(self):
    return self.default_devel()


@subpackage("papers-nautilus")
def _(self):
    self.subdesc = "nautilus integration"
    self.install_if = [self.parent, "nautilus"]
    return ["usr/lib/nautilus"]

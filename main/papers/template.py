pkgname = "papers"
pkgver = "51.0"
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
    "appstream",
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
sha256 = "bfa9b800a5225eba48c060a14710f9f393a9447d587494870e86e82a388a0a9d"
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
    from cbuild.util import cargo

    self.install_bin(
        cargo.target_path(self, "papers", f"{self.make_dir}/shell/src")
    )
    self.install_bin(
        cargo.target_path(
            self, "papers-thumbnailer", f"{self.make_dir}/thumbnailer"
        )
    )


@subpackage("papers-devel")
def _(self):
    return self.default_devel()


@subpackage("papers-nautilus")
def _(self):
    self.subdesc = "nautilus integration"
    self.install_if = [self.parent, "nautilus"]
    return ["usr/lib/nautilus"]

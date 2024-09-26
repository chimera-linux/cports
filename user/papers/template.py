pkgname = "papers"
pkgver = "46.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcomics=enabled",
    "-Dps=enabled",
    "-Dtiff=enabled",
    "-Dxps=enabled",
    "-Ddjvu=enabled",
    "-Dgtk_doc=false",
]
hostmakedepends = [
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
    "nautilus-devel",
    "poppler-devel",
    "rust-std",
]
pkgdesc = "GNOME document viewer"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Incubator/papers"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "675fc379c3758bfd95438131497c23320df90c7f7e86ba8648927fe586cdbafe"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="shell-rs").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"./build/shell-rs/src/{self.profile().triplet}/release/papers"
    )


@subpackage("papers-devel")
def _(self):
    return self.default_devel()


@subpackage("papers-nautilus")
def _(self):
    self.subdesc = "nautilus integration"
    self.install_if = [self.parent, "nautilus"]
    return ["usr/lib/nautilus"]

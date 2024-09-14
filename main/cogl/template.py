pkgname = "cogl"
pkgver = "1.22.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-kms-egl-platform", "--enable-gles2"]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libdrm-devel",
    "libgbm-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxrandr-devel",
    "mesa-devel",
    "pango-devel",
]
checkdepends = ["bash"]
pkgdesc = "Deprecated GL/GLES abstraction/utility layer"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT AND SGI-B-2.0 AND BSD-3-Clause AND custom:none"
url = "https://gitlab.gnome.org/Archive/cogl"
source = f"$(GNOME_SITE)/cogl/{pkgver[:-2]}/cogl-{pkgver}.tar.xz"
sha256 = "a805b2b019184710ff53d0496f9f0ce6dcca420c141a0f4f6fcc02131581d759"
# TODO: All tests fail
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("cogl-devel")
def _(self):
    return self.default_devel()

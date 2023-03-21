pkgname = "graphene"
pkgver = "1.10.8"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dinstalled_tests=false",
    "-Dgcc_vector=true",
    "-Dintrospection=enabled"
]
hostmakedepends = ["meson", "pkgconf", "gobject-introspection"]
makedepends = [
    "glib-devel"
]
pkgdesc = "Thin layer of graphic data types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ebassi/graphene"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a37bb0e78a419dcbeaa9c7027bcff52f5ec2367c25ec859da31dfde2928f279a"

match self.profile().arch:
    case "x86_64":
        configure_args += ["-Dsse2=true"]
    case "aarch64":
        configure_args += ["-Darm_neon=true"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("graphene-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/lib/graphene-1.0"])

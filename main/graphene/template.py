pkgname = "graphene"
pkgver = "1.10.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dinstalled_tests=false",
    "-Dgcc_vector=true",
    "-Dintrospection=enabled"
]
hostmakedepends = ["meson", "pkgconf", "gobject-introspection"]
makedepends = [
    "libglib-devel"
]
pkgdesc = "Thin layer of graphic data types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ebassi/graphene"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "80ae57723e4608e6875626a88aaa6f56dd25df75024bd16e9d77e718c3560b25"

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

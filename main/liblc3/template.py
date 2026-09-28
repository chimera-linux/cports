pkgname = "liblc3"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtools=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Low complexity communicationcodec"
license = "Apache-2.0"
url = "https://github.com/google/liblc3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "276752ff54ce6a77d54ec133397b9d7e71f90caf3d9afa32d8b0e891b8ecb8af"


@subpackage("liblc3-devel")
def _(self):
    return self.default_devel()

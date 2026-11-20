pkgname = "venus-protocol"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["python-mako"]
pkgdesc = "Virtio-GPU protocol for Vulkan command serialization"
license = "MIT"
url = "https://docs.mesa3d.org/drivers/venus"
source = f"https://gitlab.freedesktop.org/virgl/venus-protocol/-/archive/v{pkgver}/venus-protocol-{pkgver}.tar.gz"
sha256 = "783be597c8442b40577aea9e17ecf144158bcf124b6e10ff65c94254fc51e067"
# no license in tarball
options = ["!distlicense", "empty"]


@subpackage("venus-protocol-devel")
def _(self):
    return self.default_devel()

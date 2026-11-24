pkgname = "venus-protocol"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["python-mako"]
pkgdesc = "Virtio-GPU protocol for Vulkan command serialization"
license = "MIT"
url = "https://gitlab.freedesktop.org/virgl/venus-protocol"
source = f"{url}/-/archive/v{pkgver}/venus-protocol-{pkgver}.tar.gz"
sha256 = "783be597c8442b40577aea9e17ecf144158bcf124b6e10ff65c94254fc51e067"
# FIXME: remove on next bump (02c03c815fd07f2237d7f1161bbafcf6a829373c)
options = ["!distlicense"]

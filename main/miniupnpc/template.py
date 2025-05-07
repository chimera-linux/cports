pkgname = "miniupnpc"
pkgver = "2.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUPNPC_BUILD_SAMPLE=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "UPnP client library"
license = "BSD-3-Clause"
url = "http://miniupnp.free.fr"
source = f"{url}/files/miniupnpc-{pkgver}.tar.gz"
sha256 = "985de16d2e5449c3ba0d3663a0c76cb2bff82472a0eb7a306107d93f44586ffe"


def post_install(self):
    # whoever actually needs this can resurrect it
    self.uninstall("usr/bin/external-ip.sh")
    self.install_license("LICENSE")


@subpackage("miniupnpc-devel")
def _(self):
    return self.default_devel()

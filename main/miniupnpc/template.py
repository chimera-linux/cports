pkgname = "miniupnpc"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUPNPC_BUILD_SAMPLE=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "UPnP client library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "http://miniupnp.free.fr"
source = f"{url}/files/miniupnpc-{pkgver}.tar.gz"
sha256 = "025c9ab95677f02a69bc64ac0a747f07e02ba99cf797bc679a5a552fed8d990c"


def post_install(self):
    # whoever actually needs this can resurrect it
    self.uninstall("usr/bin/external-ip.sh")
    self.install_license("LICENSE")


@subpackage("miniupnpc-devel")
def _(self):
    return self.default_devel()

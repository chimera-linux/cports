pkgname = "miniupnpc"
pkgver = "2.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUPNPC_BUILD_SAMPLE=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "UPnP client library"
license = "BSD-3-Clause"
url = "http://miniupnp.free.fr"
source = f"{url}/files/miniupnpc-{pkgver}.tar.gz"
sha256 = "d52a0afa614ad6c088cc9ddff1ae7d29c8c595ac5fdd321170a05f41e634bd1a"


def post_install(self):
    # whoever actually needs this can resurrect it
    self.uninstall("usr/bin/external-ip.sh")
    self.install_license("LICENSE")


@subpackage("miniupnpc-devel")
def _(self):
    return self.default_devel()

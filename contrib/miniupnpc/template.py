pkgname = "miniupnpc"
pkgver = "2.2.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUPNPC_BUILD_SAMPLE=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "UPnP client library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "http://miniupnp.free.fr"
source = f"{url}/files/miniupnpc-{pkgver}.tar.gz"
sha256 = "05b929679091b9921b6b6c1f25e39e4c8d1f4d46c8feb55a412aa697aee03a93"


def post_install(self):
    # whoever actually needs this can resurrect it
    self.uninstall("usr/bin/external-ip.sh")
    self.install_license("LICENSE")


@subpackage("miniupnpc-devel")
def _(self):
    return self.default_devel()

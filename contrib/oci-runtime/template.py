pkgname = "oci-runtime"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
depends = ["virtual:oci-runtime-provider!oci-runtime-runc"]
pkgdesc = "OCI runtime metapackage"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


@subpackage("oci-runtime-runc")
def _runc(self):
    self.pkgdesc = "OCI runtime (runc)"
    self.depends = ["runc"]
    self.provides = [f"oci-runtime-provider={pkgver}-r{pkgrel}"]
    # default
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return []


@subpackage("oci-runtime-crun")
def _crun(self):
    self.pkgdesc = "OCI runtime (crun)"
    self.depends = ["crun"]
    self.provides = [f"oci-runtime-provider={pkgver}-r{pkgrel}"]

    return []

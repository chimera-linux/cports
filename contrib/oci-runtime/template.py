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
def _(self):
    self.subdesc = "runc"
    self.depends = ["runc"]
    self.provides = [self.with_pkgver("oci-runtime-provider")]
    # default
    self.install_if = [self.parent]

    return []


@subpackage("oci-runtime-crun")
def _(self):
    self.subdesc = "crun"
    self.depends = ["crun"]
    self.provides = [self.with_pkgver("oci-runtime-provider")]

    return []

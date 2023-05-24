pkgname = "dnssec-anchors"
pkgver = "20181012"
pkgrel = 0
pkgdesc = "DNSSEC trust anchors for the root zone"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = f"http://data.iana.org/root-anchors"
# no tests
options = ["!check"]


def do_install(self):
    self.install_file(self.files_path / "root.key", "etc/dns")

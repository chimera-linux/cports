pkgname = "iana-etc"
pkgver = "20230405"
pkgrel = 0
pkgdesc = "Unix /etc/services and /etc/protocols files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = f"https://www.iana.org/protocols"
# no tests
options = ["!check", "bootstrap"]

def do_install(self):
    self.install_file(self.files_path / "protocols", "etc")
    self.install_file(self.files_path / "services", "etc")

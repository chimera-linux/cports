pkgname = "dns-root-data"
pkgver = "2024071800"
pkgrel = 0
pkgdesc = "DNS root hints and DNSSEC trust anchor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://data.iana.org/root-anchors"
# we could use a source package to generate the files the same as debian
# does, but then we create a depcycle as that needs programs that come
# with unbound as well as some others
source = f"$(DEBIAN_SITE)/main/d/dns-root-data/dns-root-data_{pkgver}_all.deb"
sha256 = "5172a3feea331ab5ab2169b4db4ba0b3d70b2590b54273cd48086434e5cb28cc"


def install(self):
    self.install_files("usr/share/dns", "usr/share")

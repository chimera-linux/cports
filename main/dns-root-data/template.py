pkgname = "dns-root-data"
pkgver = "2024071801"
pkgrel = 0
pkgdesc = "DNS root hints and DNSSEC trust anchor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://data.iana.org/root-anchors"
# we could use a source package to generate the files the same as debian
# does, but then we create a depcycle as that needs programs that come
# with unbound as well as some others
source = f"$(DEBIAN_SITE)/main/d/dns-root-data/dns-root-data_{pkgver}_all.deb"
sha256 = "8b5f5e2c742af9c10dbe2955e8d108d1432b737503a3f77c8e67c33928bba296"


def install(self):
    self.install_files("usr/share/dns", "usr/share")

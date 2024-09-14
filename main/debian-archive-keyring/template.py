pkgname = "debian-archive-keyring"
pkgver = "2023.4"
pkgrel = 0
pkgdesc = "Debian archive keyring"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:none"
url = "https://salsa.debian.org/release-team/debian-archive-keyring"
source = f"$(DEBIAN_SITE)/main/d/debian-archive-keyring/debian-archive-keyring_{pkgver}_all.deb"
sha256 = "6e93a87b9e50bd81518880ec07a62f95d7d8452f4aa703f5b0a3076439f1022c"


def install(self):
    self.install_file(
        "etc/apt/trusted.gpg.d/*.asc", "etc/apt/trusted.gpg.d", glob=True
    )
    self.install_file(
        "usr/share/keyrings/*.gpg", "usr/share/keyrings", glob=True
    )

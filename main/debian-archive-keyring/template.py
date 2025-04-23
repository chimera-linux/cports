pkgname = "debian-archive-keyring"
pkgver = "2025.1"
pkgrel = 0
pkgdesc = "Debian archive keyring"
license = "custom:none"
url = "https://salsa.debian.org/release-team/debian-archive-keyring"
source = f"$(DEBIAN_SITE)/main/d/debian-archive-keyring/debian-archive-keyring_{pkgver}_all.deb"
sha256 = "9ea7778e443144ca490668737a8ab22dd3e748bb99e805e22ec055abeb3c7fac"


def install(self):
    self.install_file(
        "etc/apt/trusted.gpg.d/*.asc", "etc/apt/trusted.gpg.d", glob=True
    )
    self.install_file(
        "usr/share/keyrings/*.gpg", "usr/share/keyrings", glob=True
    )

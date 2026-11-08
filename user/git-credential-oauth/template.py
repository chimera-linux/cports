pkgname = "git-credential-oauth"
pkgver = "0.18.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Oauth credential manager for git"
license = "Apache-2.0"
url = "https://github.com/hickford/git-credential-oauth"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2acf2c1c9197e179e3068e318da67ec1af26feae63d8661c930963e3a7704ba2"


def post_install(self):
    self.install_man("git-credential-oauth.1")

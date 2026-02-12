pkgname = "tea"
pkgver = "0.11.1"
pkgrel = 2
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X code.gitea.io/tea/cmd.Version={pkgver}",
]
hostmakedepends = ["go"]
pkgdesc = "CLI tool to interact with Gitea servers"
license = "MIT"
url = "https://gitea.com/gitea/tea"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1da6b6d2534bd6ffb0931400014bbdef26242cf4d35d4ba44c24928811825805"


def post_install(self):
    self.install_license("LICENSE")

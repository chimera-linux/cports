pkgname = "tea"
pkgver = "0.10.1"
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
sha256 = "791b7f90eff9ade0d5ee5e3f0dfba128e35eaf83b5f8b8d5f5d6cc9a94ae9b03"


def post_install(self):
    self.install_license("LICENSE")

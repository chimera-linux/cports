pkgname = "tea"
pkgver = "0.14.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X code.gitea.io/tea/cmd.Version={pkgver}",
]
hostmakedepends = ["go"]
checkdepends = ["git"]
pkgdesc = "CLI tool to interact with Gitea servers"
license = "MIT"
url = "https://gitea.com/gitea/tea"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f509de217ac0e57491ffdab2750516e8c505780881529ee703b9d0c86cc652a3"


def post_install(self):
    self.install_license("LICENSE")

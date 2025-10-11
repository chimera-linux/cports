pkgname = "tea"
pkgver = "0.11.0"
pkgrel = 0
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
sha256 = "278bbdf2e197f6f80a838e09574e8a950de535f0ba0f53154d26930a3adfaaa6"


def post_install(self):
    self.install_license("LICENSE")

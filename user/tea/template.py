pkgname = "tea"
pkgver = "0.14.0"
pkgrel = 2
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X code.gitea.io/tea/modules/version.Version={pkgver}",
]
hostmakedepends = ["go"]
checkdepends = ["git"]
pkgdesc = "CLI tool to interact with Gitea servers"
license = "MIT"
url = "https://gitea.com/gitea/tea"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f509de217ac0e57491ffdab2750516e8c505780881529ee703b9d0c86cc652a3"
# generates completions and manpage with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"tea.{shell}", "w") as o:
            self.do("build/tea", "completion", shell, stdout=o)

    with open(self.cwd / "tea.1", "w") as o:
        self.do("build/tea", "man", stdout=o)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"tea.{shell}", shell)
    self.install_man("tea.1")
    self.install_license("LICENSE")

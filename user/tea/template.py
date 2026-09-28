pkgname = "tea"
pkgver = "0.15.1"
pkgrel = 0
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
sha256 = "e242dd3589c31a36320d75e0de9eefa3fa429bd9b0af89d35af8585c7f514b9c"
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

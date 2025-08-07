pkgname = "hut"
pkgver = "0.6.0"
pkgrel = 15
build_style = "go"
hostmakedepends = ["go", "scdoc"]
pkgdesc = "CLI tool for sr.ht"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~xenrox/hut"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f6abe54b433c30557c49aa41d351ec97ef24b4bee3f9dbc91e7db8f366592f99"
# completions are generated with built artifact
options = ["!cross"]


def post_build(self):
    self.do("make", "doc/hut.1")

    for s in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hut.{s}", "w") as cf:
            self.do(f"{self.make_dir}/hut", "completion", s, stdout=cf)


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/hut.1")
    self.install_completion("hut.bash", "bash")
    self.install_completion("hut.zsh", "zsh")
    self.install_completion("hut.fish", "fish")

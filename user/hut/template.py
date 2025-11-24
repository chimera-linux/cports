pkgname = "hut"
pkgver = "0.7.0"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "CLI tool for sr.ht"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~xenrox/hut"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5975f940740dd816057ab3cf20cebde3ece3250891952a566f8555f73fb67b21"
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

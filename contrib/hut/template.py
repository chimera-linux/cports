pkgname = "hut"
pkgver = "0.4.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "scdoc"]
pkgdesc = "CLI tool for sr.ht"
maintainer = "Hugo Machet <mail@hmachet.com>"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~emersion/hut"
source = f"https://git.sr.ht/~emersion/hut/archive/v{pkgver}.tar.gz"
sha256 = "f25ab4452e4622f404a6fa5713e8505302bfcee4dd3a8dfe76f1fc4c05688c09"
# !cross: completions are generated with built artifact
options = ["!debug", "!cross"]


def post_build(self):
    self.do("make", "doc/hut.1")

    for s in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hut.{s}", "w") as cf:
            self.do(
                self.make_dir + "/hut",
                "completion",
                s,
                stdout=cf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/hut.1")
    self.install_completion("hut.bash", "bash")
    self.install_completion("hut.zsh", "zsh")
    self.install_completion("hut.fish", "fish")

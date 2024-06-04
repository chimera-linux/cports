pkgname = "hut"
pkgver = "0.5.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go", "scdoc"]
pkgdesc = "CLI tool for sr.ht"
maintainer = "Hugo Machet <mail@hmachet.com>"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~xenrox/hut"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0f78917a2da718b0317cd73307549f429340c7f5cac84c6356341e4fae800cc1"
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

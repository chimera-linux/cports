pkgname = "hugo"
pkgver = "0.124.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Static site generator"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "0beb0436f6bd90abb425523229a37f1d31e2e9c7ba9fac4556a72aab3b11bfef"
# tests require network access
# manpages and completions are generated with the resulting binary so no cross
options = ["!check", "!cross"]


def post_build(self):
    self.do(self.make_dir + "/hugo", "gen", "man")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hugo.{shell}", "w") as f:
            self.do(
                self.make_dir + "/hugo",
                "completion",
                shell,
                stdout=f,
            )


def post_install(self):
    self.install_man("man/*", glob=True)

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hugo.{shell}", shell)

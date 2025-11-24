pkgname = "hugo"
pkgver = "0.151.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    "-ldflags=-X github.com/gohugoio/hugo/common/hugo.vendorInfo=ChimeraLinux"
]
hostmakedepends = ["go"]
go_build_tags = ["extended"]
pkgdesc = "Static site generator"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "b41d6e3da741c8d5637e016a1fa98f36e47dbfa9e213ff2d73ced66fb5b770ea"
# tests require network access
# manpages and completions are generated with the resulting binary so no cross
options = ["!check", "!cross"]


def post_build(self):
    self.do(f"{self.make_dir}/hugo", "gen", "man")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hugo.{shell}", "w") as f:
            self.do(f"{self.make_dir}/hugo", "completion", shell, stdout=f)


def post_install(self):
    self.install_man("man/*", glob=True)

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hugo.{shell}", shell)

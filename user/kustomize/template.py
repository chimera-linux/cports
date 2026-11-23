pkgname = "kustomize"
pkgver = "5.8.3"
pkgrel = 0
build_wrksrc = "kustomize"
build_style = "go"
make_build_args = [
    f"-ldflags= -X sigs.k8s.io/kustomize/api/provenance.version={pkgver}",
    ".",
]
hostmakedepends = ["go"]
pkgdesc = "Customization of kubernetes YAML configurations"
license = "Apache-2.0"
url = "https://kustomize.io"
source = f"https://github.com/kubernetes-sigs/kustomize/archive/refs/tags/kustomize/v{pkgver}.tar.gz"
sha256 = "c823ae7b7e1461d82dfe7e592823796c6a98d9633cdbe33c64508b65c9911a57"


def prepare(self):
    with self.pushd(build_wrksrc):
        self.golang.mod_download()


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"kustomize.{shell}", "w") as outf:
            self.do("build/kustomize", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"kustomize.{shell}", shell)

pkgname = "kubectx"
pkgver = "0.11.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X main.version=v{pkgver}",
    "./cmd/kubectx",
    "./cmd/kubens",
]
hostmakedepends = ["go"]
pkgdesc = "Tools for switching Kubernetes contexts and namespaces"
license = "Apache-2.0"
url = "https://github.com/ahmetb/kubectx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1c8eb6b30c0067f89e5b2f9480865b0e3229a221fadddb644ce192d663c63907"


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        for prog in ["kubectx", "kubens"]:
            # zsh completion files are named _prog.zsh upstream
            src = f"_{prog}.zsh" if shell == "zsh" else f"{prog}.{shell}"
            self.install_completion(f"completion/{src}", shell, prog)

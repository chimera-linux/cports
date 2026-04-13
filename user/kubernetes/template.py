pkgname = "kubernetes"
pkgver = "1.35.0"
pkgrel = 0
build_style = "makefile"
make_env = {
    "FORCE_HOST_GO": "y",
}
make_build_env = {"GOLDFLAGS": "-extldflags=-static"}
hostmakedepends = ["bash", "go", "rsync"]
makedepends = [
    "dinit-chimera",
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "musl-devel-static",
]
depends = [
    "conntrack-tools",
    "cri-tools",
    "ethtool",
    "iproute2",
    "iptables",
    "socat",
]
pkgdesc = "Container scheduling and management platform"
license = "Apache-2.0"
url = "https://kubernetes.io"
source = f"https://github.com/kubernetes/kubernetes/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ed32a4da18f41f8cde7d8484afafc76b6a008915425f69440228d8e63d3f420d"
tool_flags = {"GOFLAGS": ["-buildmode=pie", "-v", "-tags=providerless"]}
# check: depends on networking, cross: needs host binary to generate completions
options = ["!check", "!cross"]
_cli = ["kubeadm", "kubectl"]
_supported_completions = ["bash", "zsh"]
_services = [
    "kube-apiserver",
    "kube-controller-manager",
    "kube-proxy",
    "kube-scheduler",
    "kubelet",
]


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_build(self):
    for completion in _supported_completions:
        for cli in _cli:
            with open(f"{self.cwd}/{cli}.{completion}", "w") as o:
                self.do(
                    f"_output/local/bin/linux/{self.profile().goarch}/{cli}",
                    "completion",
                    completion,
                    stdout=o,
                )


def install(self):
    for binary in [*_cli, *_services]:
        with self.pushd("_output/local/go/bin"):
            self.install_bin(binary)
    for service in _services:
        self.install_service(self.files_path / service)
    for completion in _supported_completions:
        for cli in _cli:
            self.install_completion(f"{cli}.{completion}", completion, name=cli)
    self.install_file(
        self.files_path / "sysctl.conf",
        "usr/lib/sysctl.d",
        name="30-kubernetes.conf",
    )
    self.install_file(
        self.files_path / "modprobe.conf",
        "usr/lib/modprobe.d",
        name="99-kubernetes.conf",
    )
    self.install_dir("etc/kubernetes")


@subpackage("kubeadm")
def _(self):
    self.subdesc = "Kubernetes cluster building CLI"
    return [
        "usr/bin/kubeadm",
        "usr/share/zsh/site-functions/_kubeadm",
        "usr/share/bash-completion/completions/kubeadm",
    ]


@subpackage("kubectl")
def _(self):
    self.subdesc = "Kubernetes node management CLI"
    return [
        "usr/bin/kubectl",
        "usr/share/zsh/site-functions/_kubectl",
        "usr/share/bash-completion/completions/kubectl",
    ]


@subpackage("kubernetes-recommends")
def _(self):
    self.depends = [
        "cri-o",
    ]
    self.subdesc = "recommended dependencies"
    self.install_if = [self.parent]
    self.options = ["empty"]
    return []


def post_install(self):
    self.install_license("LICENSE")

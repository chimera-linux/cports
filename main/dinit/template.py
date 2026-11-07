pkgname = "dinit"
pkgver = "0.23.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--default-auto-restart=on-failure",
    "--disable-strip",
    "--enable-capabilities",
    "--enable-cgroups",
    "--enable-initgroups",
    "--enable-ioprio",
    "--enable-oom-adj",
    "--enable-shutdown",
    "--platform=Linux",
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/v{pkgver}.tar.gz"
sha256 = "911ed52b78ce4950824623d58826b88a839748e18ef837a234d50db6d83972e2"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")

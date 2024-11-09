pkgname = "txr"
pkgver = "296"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "configure"
configure_args = ["--parallelmake", "--prefix=/usr"]
make_check_target = "tests"
hostmakedepends = ["bash"]
makedepends = ["libffi-devel", "zlib-ng-compat-devel"]
pkgdesc = "Data munging language"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:txr"
url = "https://www.nongnu.org/txr"
source = f"https://www.kylheku.com/cgit/txr/snapshot/txr-{pkgver}.tar.bz2"
sha256 = "753e74c1f11c109a5235856b5e5800912b8267e08257a1a26f17e74efd5c2917"
hardening = ["vis"]
# tests disabled on ppc
options = ["!cross", "!lto"]

match self.profile().arch:
    case "ppc64le":
        # weird corruption maybe due to UB? FIXME
        # in eval.c in env_vbind, env->e.vbindings
        # may be 0x4 instead of 0x0 once loaded into
        # the loc (due to how it deals with unions?)
        tool_flags = {"CFLAGS": ["-O1"]}
        # tests still fail FIXME
        options += ["!check"]
    case "ppc64":
        # tests also fail, FIXME
        options += ["!check"]


def init_configure(self):
    self.env["txr_shell"] = "/usr/bin/bash"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("METALICENSE")

    self.uninstall("usr/share/txr/LICENSE")
    self.uninstall("usr/share/txr/METALICENSE")

    # hardlinks
    for f in ["txrlisp", "txrvm"]:
        self.uninstall(f"usr/bin/{f}")
        self.install_link(f"usr/bin/{f}", "txr")

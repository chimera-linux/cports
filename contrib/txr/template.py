pkgname = "txr"
pkgver = "293"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "configure"
configure_args = ["--parallelmake", "--prefix=/usr"]
make_cmd = "gmake"
make_check_target = "tests"
hostmakedepends = ["bash", "gmake"]
makedepends = ["libffi-devel", "zlib-ng-compat-devel"]
pkgdesc = "Data munging language"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:txr"
url = "https://www.nongnu.org/txr"
source = f"https://www.kylheku.com/cgit/txr/snapshot/txr-{pkgver}.tar.bz2"
sha256 = "6fc21ae7332f98f97af35ad3ca1808d0043c4c85384c4e7bebcfce967e36fa5c"
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

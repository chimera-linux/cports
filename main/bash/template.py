pkgname = "bash"
pkgver = "5.2.21"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--without-bash-malloc",
    "--with-curses",
    "--with-installed-readline",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
make_check_target = "tests"
hostmakedepends = ["bison", "texinfo"]
makedepends = ["ncurses-devel", "readline-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU Bourne Again Shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bash"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c8e31bdc59b69aaffc5b36509905ba3e5cbb12747091d27b4b977f078560d5b8"
tool_flags = {
    "CFLAGS": [
        '-DSYS_BASHRC="/etc/bash/bashrc"',
        "-DNON_INTERACTIVE_LOGIN_SHELLS",
    ]
}
# FIXME cfi, int: testsuite failures
hardening = ["vis", "!cfi", "!int"]


def init_configure(self):
    tcap = self.profile().sysroot / "usr/lib/libncursesw.a"
    self.make_build_args += [f"TERMCAP_LIB={tcap}"]


def post_install(self):
    self.install_dir("etc/bash/bashrc.d", empty=True)

    # register with shells
    self.install_shell("/usr/bin/bash")

    self.uninstall("usr/share/doc")

    self.install_link("usr/bin/rbash", "bash")

    self.install_file(self.files_path / "bashrc", "etc/bash")
    self.install_file(self.files_path / "bash.sh", "etc/profile.d")

    # remove devel files
    self.uninstall("usr/lib")
    self.uninstall("usr/include")


configure_gen = []

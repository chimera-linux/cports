pkgname = "bash"
pkgver = "5.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-bash-malloc",
    "--with-curses",
    "--with-installed-readline",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
configure_gen = []
make_check_target = "tests"
hostmakedepends = ["bison", "texinfo"]
makedepends = ["ncurses-devel", "readline-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU Bourne Again Shell"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bash"
source = f"$(GNU_SITE)/bash/bash-{pkgver}.tar.gz"
sha256 = "0d5cd86965f869a26cf64f4b71be7b96f90a3ba8b3d74e27e8e9d9d5550f31ba"
tool_flags = {
    "CFLAGS": [
        '-DSYS_BASHRC="/etc/bash/bashrc"',
        "-DNON_INTERACTIVE_LOGIN_SHELLS",
    ]
}
# FIXME cfi, int: testsuite failures
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_tmpfiles("^/tmpfiles.conf")

    # register with shells
    self.install_shell("/usr/bin/bash")

    self.uninstall("usr/share/doc")

    self.install_link("usr/bin/rbash", "bash")

    self.install_file("^/bashrc", "etc/bash")
    self.install_file("^/bash.sh", "etc/profile.d")

    # remove devel files
    self.uninstall("usr/lib")
    self.uninstall("usr/include")

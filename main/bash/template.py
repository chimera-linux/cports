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
sha256 = "62dd49c44c399ed1b3f7f731e87a782334d834f08e098a35f2c87547d5dbb269"
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

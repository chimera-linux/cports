pkgname = "bash"
pkgver = "5.2.37"
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
configure_gen = []
make_check_target = "tests"
hostmakedepends = ["bison", "texinfo"]
makedepends = ["ncurses-devel", "readline-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU Bourne Again Shell"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bash"
source = f"$(GNU_SITE)/bash/bash-{pkgver}.tar.gz"
sha256 = "9599b22ecd1d5787ad7d3b7bf0c59f312b3396d1e281175dd1f8a4014da621ff"
tool_flags = {
    "CFLAGS": [
        '-DSYS_BASHRC="/etc/bash/bashrc"',
        "-DNON_INTERACTIVE_LOGIN_SHELLS",
    ]
}
# FIXME cfi, int: testsuite failures
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    # register with shells
    self.install_shell("/usr/bin/bash")

    self.uninstall("usr/share/doc")

    self.install_link("usr/bin/rbash", "bash")

    self.install_file(self.files_path / "bashrc", "etc/bash")
    self.install_file(self.files_path / "bash.sh", "etc/profile.d")

    # remove devel files
    self.uninstall("usr/lib")
    self.uninstall("usr/include")

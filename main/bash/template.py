pkgname = "bash"
pkgver = "5.1.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-bash-malloc",
    "--with-curses",
    "--without-installed-readline",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
make_check_target = "tests"
hostmakedepends = ["bison", "texinfo"]
makedepends = ["ncurses-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU Bourne Again Shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bash"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5bac17218d3911834520dad13cd1f85ab944e1c09ae1aba55906be1f8192f558"
tool_flags = {"CFLAGS": ["-DSYS_BASHRC=\"/etc/bash/bashrc\""]}

def init_configure(self):
    tcap = self.profile().sysroot / "usr/lib/libncursesw.a"
    self.make_build_args += [f"TERMCAP_LIB={tcap}"]

def post_install(self):
    self.install_dir("etc/bash/bashrc.d", empty = True)

    # register with shells
    self.install_shell("/usr/bin/bash")

    self.rm(self.destdir / "usr/share/doc", recursive = True, force = True)

    self.install_link("bash", "usr/bin/rbash")

    self.install_file(self.files_path / "bashrc", "etc/bash")
    self.install_file(self.files_path / "bash.sh", "etc/profile.d")

    # remove devel files
    self.rm(self.destdir / "usr/lib", recursive = True)
    self.rm(self.destdir / "usr/include", recursive = True)

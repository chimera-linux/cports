pkgname = "bash"
pkgver = "5.2"
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
sha256 = "a139c166df7ff4471c5e0733051642ee5556c1cc8a4a78f145583c5c81ab32fb"
tool_flags = {"CFLAGS": [
    "-DSYS_BASHRC=\"/etc/bash/bashrc\"",
    "-DNON_INTERACTIVE_LOGIN_SHELLS",
]}

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

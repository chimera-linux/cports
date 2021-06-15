from cbuild.util import make

def init_configure(self):
    self.make = make.Make(self, wrksrc = "build")

def do_configure(self):
    self.do(
        "meson", [
            "--prefix=/usr",
            "--libdir=/usr/lib",
            "--libexecdir=/usr/libexec",
            "--bindir=/usr/bin",
            "--sbindir=/usr/bin",
            "--includedir=/usr/include",
            "--datadir=/usr/share",
            "--mandir=/usr/share/man",
            "--infodir=/usr/share/info",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--sharedstatedir=/var/lib",
            "--buildtype=plain",
            "--auto-features=auto",
            "--wrap-mode=nodownload",
            "-Ddefault_library=both",
            "-Db_ndebug=true",
            "-Db_staticpic=true"
        ] + self.configure_args + [self.meson_dir, "build"], build = True
    )

def do_build(self):
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    self.make.install(default_args = False, env = {
        "DESTDIR": str(self.chroot_destdir)
    })

def use(tmpl):
    tmpl.build_style = "meson"
    tmpl.init_configure = init_configure
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
    tmpl.make_build_target = "all"
    tmpl.make_cmd = "ninja"

    tmpl.build_style_fields = [
        ("meson_dir", ".", str, False, False, False)
    ]
